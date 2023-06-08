# Standard Library Modules
import os
import shutil
import time
import unittest

# Third-Party Library Modules
import matplotlib.pyplot as plt

from BeautifulReport import BeautifulReport
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Local Application/Project-Specific Modules
import config
import image_similarity
import util
import report_template

from chrome_driver import SingletonChromeDriver


class G4Tester(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.GAME_ID = "4" # 遊戲編號
        cls.WEBDRIVER_TIMEOUT = 10 # WebDriverWait 的條件等待時間
        cls.LOADING_DELAY = 5 # 載入等待時間
        cls.SPIN_DEALY = 5 # 下注表演等待時間
        cls.PANNEL_HEIGHT_RATIO = (0.41, 0.75) # 老虎機面板範圍 (以百分比表示艱鉅)
        cls.SIMILARITY = 0.95 # 比對相似度閥值

        cls.chrome = SingletonChromeDriver.get_instance()
        cls.cheat_table = {
            "params": {
                "key": f"{config.KK_ADMIN_USER}-{cls.GAME_ID}",
                "data": {
                    "baseGame": [15, 46, 93, 100, 94],
                    "longWildIndex": -1,
                    "cheatCase": 0
                }
            }
        }


    @classmethod
    def tearDownClass(cls):
        # 所有 case 跑完後就退出瀏覽器
        # cls.chrome.quit()
        pass


    def test_01_update_cheat_table(self):
        """
        TestCase 更新配牌器
        """
        resp = util.update_slot_cheat_table(config.KK_WEBTOOL_URL, self.cheat_table)
        if resp == "":
            raise RuntimeError("配牌器更新失敗")


    def test_02_open_kkgame(self):
        """
        TestCase 進入 KKGame 指定遊戲, 進行下注後對螢幕截圖
        """

        # 取得操作 KKGame 管理後台的操作憑證
        token = util.get_kkgame_admin_access_token(
            config.KK_ADMIN_URL,
            config.KK_ADMIN_USER,
            config.KK_ADMIN_PASSWORD,
        )

        # 取得指定遊戲連結
        url = util.get_kkgame_game_url(
            config.KK_ADMIN_URL,
            token,
            self.GAME_ID,
            config.KK_ADMIN_ECSITE,
            config.KK_ADMIN_LANG,
        )

        # 跳轉到指定遊戲
        self.chrome.get(url)
        
        # 等待遊戲加載完成
        WebDriverWait(self.chrome, self.WEBDRIVER_TIMEOUT).until(util.waiting_cocos_loading)

        # 跳轉場景過程沒辦法用其他方式判斷, 只能強制等待
        time.sleep(self.LOADING_DELAY)

        # 取得 Cocos Creator 的 canvas metadata
        canvas = self.chrome.find_element(By.ID, "GameCanvas")
        canvas_width = canvas.size["width"]
        canvas_height = canvas.size["height"]

        # 點擊 spin
        spin_x_offset = 0
        spin_y_offset = (canvas_height/2) - (canvas_height - (canvas_height*0.9))

        actions = ActionChains(self.chrome)
        actions.move_to_element_with_offset(canvas, spin_x_offset, spin_y_offset).click().perform()
        
        # 沒辦法知道 spin 過程是否已經結束, 只能強制等待
        time.sleep(self.SPIN_DEALY)

        # 擷取畫面
        save_path = os.path.join(config.REPORT_GEN_DIR, f"G{self.GAME_ID}_screenshot.png")
        canvas.screenshot(save_path)


    def test_03_image_matching(self):
        """
        TestCase 圖片比對
        """

        # 取得用來比較特徵點的 screenshot 與 ground truth
        screenshot_path = os.path.join(config.REPORT_GEN_DIR, f"G{self.GAME_ID}_screenshot.png")
        ground_truth_path = os.path.join(config.GROUND_TRUTU_DIR, f"G{self.GAME_ID}_ground_truth.png")
        
        # 複製 ground truth 到輸出報告的目錄底下
        shutil.copyfile(ground_truth_path, os.path.join(config.REPORT_GEN_DIR, f"G{self.GAME_ID}_ground_truth.png"))
        
        # 比對 screenshot 與 ground truth 的相似度後保存比對結果
        similarity, difference_image = image_similarity.calculate_image_similarity(
            image_similarity.Algorithm.P_HASH, 
            screenshot_path, 
            ground_truth_path,
            self.PANNEL_HEIGHT_RATIO,
        )
        difference_image_path = os.path.join(config.REPORT_GEN_DIR, f"G{self.GAME_ID}_difference.png")
        plt.imsave(difference_image_path, difference_image)

        html_output = report_template.image_similarity_html_template.format(
            result_msg = "成功, 有符合的圖像" if similarity >= self.SIMILARITY else "失敗, 實際畫面與原圖不符",
            similarity = similarity,
            game_id = self.GAME_ID
        )

        print(html_output)

        if similarity < self.SIMILARITY:
            raise RuntimeError("圖片比對失敗")


if __name__ == '__main__':
    # 檢查所需資料夾是否存在
    if not os.path.exists(config.GROUND_TRUTU_DIR):
        os.mkdir(config.GROUND_TRUTU_DIR)
    if not os.path.exists(config.REPORT_ROOT_DIR):
        os.mkdir(config.REPORT_ROOT_DIR)
    
    # 建立這次測試的報告路徑
    os.mkdir(config.REPORT_GEN_DIR)
    
    # 載入用例
    testunit = unittest.TestSuite()
    # testunit.addTest(G4Tester('case_enable_slot_cheat_table'))
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(G4Tester))
    
    # 輸出結果報告
    BeautifulReport(testunit).report(
        filename = f"kkgame_report_{config.DATE}", 
        description = f"KKGAME_測試報告({config.DATE})", 
        log_path= config.REPORT_GEN_DIR
    )
