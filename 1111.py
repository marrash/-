import logging
import os
import sys
import unittest
from xml.dom import DOMException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import BeautifulReport
from BeautifulReport import BeautifulReport
import pictest 
import pyautogui


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Selenium
        # 取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行
        options = Options()
        options.add_argument("--disable-notifications")
        # 引用webdriver
        self.chrome = webdriver.Chrome(r'C:/Users/marrash_kao/Desktop/tools/kkgame/chromedriver.exe', chrome_options=options)
        # 開啟要爬的網址
        self.chrome.get('http://egame.uat.kk168-01.com/Login')
        #self.chrome.maximize_window()

        # 取得網站的title
        title = self.chrome.title
        print("title :",title)
        time.sleep(3)

    @classmethod
    def tearDownClass(self):
        ## 所有case跑完後就退出瀏覽器
        self.chrome.quit()

    def test_01_login(self):
        '''登入'''
        # 應用find_element_by_id 來建立物件
        user = self.chrome.find_element("xpath", "//body/div[@id='app']/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/input[1]")
        password = self.chrome.find_element("xpath","//body/div[@id='app']/div[1]/div[1]/section[1]/form[1]/div[2]/div[1]/div[1]/input[1]")

        # 應用send_keys()來模擬使用者輸入的資料
        user.send_keys('marrash_kao1')
        password.send_keys('0912263549')
        print("登入 :成功")
        time.sleep(3)

        # 點擊登入
        login = self.chrome.find_element("xpath","//body/div[@id='app']/div[1]/div[1]/section[1]/form[1]/div[3]/div[1]/button[1]")
        login.click()
        time.sleep(3)

    def test_02_opendemo(self):
        '''點擊遊戲DEMO功能''' 
        gamedemo = self.chrome.find_element("xpath","//body/div[@id='app']/section[1]/section[1]/aside[1]/div[1]/div[1]/div[1]/ul[1]/a[2]/li[1]/div[1]")
        gamedemo.click()
        print("開啟demo :成功")
        time.sleep(3)

    #--------------------------------------------------------
    def test_03_opengame(self):
        '''開啟真龍虎爭霸'''
        dragon = self.chrome.find_element("xpath","//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[22]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_dragon.png")
        self.chrome.find_element("xpath","//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")

        '''真龍虎爭霸比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_dragon.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/dragon.png'
        pic = pictest.get_image_element_point(img1,img2)
        
        if pic >= 300:
            self.chrome.back()
        else:
            self.chrome.back()
            class DemoException(Exception):
                def __init__(self, message):
                    super().__init__(message)
            message = "遊戲比對 :失敗，找不到相符的畫面"
            raise DemoException(message)
        time.sleep(15)

    #--------------------------------------------------------
    def test_20_opengame(self):
        '''開啟森林舞会'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[24]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        pyautogui.moveTo(700,179)
        pyautogui.click()
        time.sleep(5)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_forestball.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''森林舞会比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_forestball.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/forestball.png'
        pic = pictest.get_image_element_point(img1,img2)

        if pic >= 300:
            self.chrome.back()
        else:
            self.chrome.back()
            class DemoException(Exception):
                def __init__(self, message):
                    super().__init__(message)
            message = "遊戲比對 :失敗，找不到相符的畫面"
            raise DemoException(message)
        time.sleep(15)

# 產出測試報告
basedir = "C:/Users/marrash_kao/Desktop/tools/kkgame/KKGAME_REPORT"
reportname = time.strftime('kkgame_report_%Y_%m_%d', time.gmtime())
if __name__ == '__main__':

    testunit = unittest.TestSuite()
    # 載入用例
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    result = BeautifulReport(testunit)
    result.report(filename=reportname, description='KKGAME_測試報告', log_path=basedir)

