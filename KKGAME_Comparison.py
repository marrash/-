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
        self.chrome = webdriver.Chrome(r'C:/Users/marrash_kao/Desktop/tools/kkgame/chromedriver', chrome_options=options)
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
        password = self.chrome.find_element("xpath", "//body/div[@id='app']/div[1]/div[1]/section[1]/form[1]/div[2]/div[1]/div[1]/input[1]")
        
        # 應用send_keys()來模擬使用者輸入的資料
        user.send_keys('marrash_kao1')
        password.send_keys('0912263549')
        time.sleep(3)

        # 點擊登入
        login = self.chrome.find_element("xpath", "//body/div[@id='app']/div[1]/div[1]/section[1]/form[1]/div[3]/div[1]/button[1]")
        login.click()
        time.sleep(3)

    def test_02_opendemo(self):
        '''點擊遊戲DEMO功能''' 
        gamedemo = self.chrome.find_element("xpath", "//body/div[@id='app']/section[1]/section[1]/aside[1]/div[1]/div[1]/div[1]/ul[1]/a[2]/li[1]/div[1]")
        gamedemo.click()
        time.sleep(3)

    #--------------------------------------------------------
    def test_03_opengame(self):
        '''開啟真龍虎爭霸'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[22]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_dragon.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
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
    def test_04_opengame(self):
        '''開啟魔法糖果'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[17]/td[2]/div[1]/button[1]/span[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_candy.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''魔法糖果比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_candy.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/candy.png'
        pic = pictest.get_image_element_point(img1,img2)

        if pic >= 280:
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
    def test_05_opengame(self):
        '''開啟福祿壽'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[25]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_fuluso.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''福祿壽比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_fuluso.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/fuluso.png'
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
    def test_06_opengame(self):
        '''開啟深海历险'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_theocean.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''深海历险比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_theocean.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/theocean.png'
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
    def test_07_opengame(self):
        '''開啟封神榜'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[6]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Fengshen.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''封神榜比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Fengshen.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Fengshen.png'
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
    def test_08_opengame(self):
        '''開啟玛雅遗迹'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[7]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Mayan.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")

        '''玛雅遗迹比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Mayan.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Mayan.png'
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
    def test_09_opengame(self):
        '''開啟埃及艳后'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[8]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Cleopatra.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''埃及艳后比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Cleopatra.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Cleopatra.png'
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
    def test_10_opengame(self):
        '''開啟SuperStar'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[9]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_SuperStar.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''SuperStar比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_SuperStar.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/SuperStar.png'
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
    def test_11_opengame(self):
        '''開啟侏罗纪乐园'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[10]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Jurassic.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''侏罗纪乐园比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Jurassic.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Jurassic.png'
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
    def test_12_opengame(self):
        '''開啟西游大闹天宫'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[11]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_theWest.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''西游大闹天宫比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_theWest.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/theWest.png'
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
    def test_13_opengame(self):
        '''開啟聚宝盆'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[12]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_treasure.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''聚宝盆比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_treasure.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/treasure.png'
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
    def test_14_opengame(self):
        '''開啟亚瑟王'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[13]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_KingArthur.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''亚瑟王比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_KingArthur.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/KingArthur.png'
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
    def test_15_opengame(self):
        '''開啟福虎'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[18]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Fuhu.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''福虎比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Fuhu.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Fuhu.png'
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
    def test_16_opengame(self):
        '''開啟龙神'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[19]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_DragonGod.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''龙神比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_DragonGod.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/DragonGod.png'
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
    def test_17_opengame(self):
        '''開啟凤凰传奇'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[20]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Phoenix.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''凤凰传奇比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Phoenix.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Phoenix.png'
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
    def test_18_opengame(self):
        '''開啟龙虎争霸'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[21]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_tiger.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''龙虎争霸比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_tiger.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/tiger.png'
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
    def test_19_opengame(self):
        '''開啟动物王国'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[23]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_animalkingdom.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''动物王国比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_animalkingdom.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/animalkingdom.png'
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

    #--------------------------------------------------------
    def test_21_opengame(self):
        '''開啟武圣传'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[26]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_WuSheng.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''武圣传比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_WuSheng.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/WuSheng.png'
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
    def test_22_opengame(self):
        '''開啟闪亮水果盘'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[27]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_shinyfruit.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''闪亮水果盘比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_shinyfruit.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/shinyfruit.png'
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
    def test_23_opengame(self):
        '''開啟燥起来'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[35]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_dryup.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''燥起来比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_dryup.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/dryup.png'
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
    def test_24_opengame(self):
        '''開啟印度之心'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[36]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_India.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''印度之心比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_India.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/India.png'
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
    def test_25_opengame(self):
        '''開啟抢庄牛牛'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_GrabZhuangNiuNiu.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''抢庄牛牛比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_GrabZhuangNiuNiu.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/GrabZhuangNiuNiu.png'
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
    def test_26_opengame(self):
        '''開啟通比牛牛'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_TumblrNiuNiu.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''通比牛牛比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_TumblrNiuNiu.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/TumblrNiuNiu.png'
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
    def test_27_opengame(self):
        '''開啟三公'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[4]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Sangong.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''三公比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Sangong.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Sangong.png'
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
    def test_28_opengame(self):
        '''開啟正宗抢庄牛牛'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[28]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_AuthenticRobZhuangNiuNiu.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''正宗抢庄牛牛比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_AuthenticRobZhuangNiuNiu.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/AuthenticRobZhuangNiuNiu.png'
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
    def test_29_opengame(self):
        '''開啟正宗通比牛牛'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[29]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_AuthenticTongbiNiuNiu.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''正宗通比牛牛比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_AuthenticTongbiNiuNiu.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/AuthenticTongbiNiuNiu.png'
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
    def test_30_opengame(self):
        '''開啟正宗三公'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[30]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_AuthenticSanGong.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''正宗三公比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_AuthenticSanGong.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/AuthenticSanGong.png'
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
    def test_31_opengame(self):
        '''開啟大众麻将'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        pyautogui.moveTo(392,649)
        pyautogui.click()
        time.sleep(5)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_PopularMahjong.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''大众麻将比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_PopularMahjong.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/PopularMahjong.png'
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
    def test_32_opengame(self):
        '''開啟红中麻将'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[14]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        pyautogui.moveTo(392,649)
        pyautogui.click()
        time.sleep(5)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_RedChineseMahjong.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''红中麻将比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_RedChineseMahjong.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/RedChineseMahjong.png'
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
    def test_33_opengame(self):
        '''開啟血流成河'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[15]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        pyautogui.moveTo(392,649)
        pyautogui.click()
        time.sleep(5)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_riverofblood.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''血流成河比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_riverofblood.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/riverofblood.png'
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
    def test_34_opengame(self):
        '''開啟血战到底'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[16]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        pyautogui.moveTo(392,649)
        pyautogui.click()
        time.sleep(5)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_bloodybattle.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''血战到底比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_bloodybattle.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/bloodybattle.png'
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
    def test_35_opengame(self):
        '''開啟温州麻将'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[31]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        pyautogui.moveTo(392,649)
        pyautogui.click()
        time.sleep(5)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_WenzhouMahjong.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''温州麻将比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_WenzhouMahjong.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/WenzhouMahjong.png'
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
    def test_36_opengame(self):
        '''開啟上海麻将'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[32]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        pyautogui.moveTo(392,649)
        pyautogui.click()
        time.sleep(5)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_ShanghaiMahjong.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''上海麻将比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_ShanghaiMahjong.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/ShanghaiMahjong.png'
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
    def test_37_opengame(self):
        '''開啟麻将来了'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[34]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Mahjongcoming.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''麻将来了比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Mahjongcoming.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Mahjongcoming.png'
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
    def test_38_opengame(self):
        '''開啟富贵捕鱼'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[37]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_richfishing.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''富贵捕鱼比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_richfishing.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/richfishing.png'
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
    def test_39_opengame(self):
        '''開啟猜硬币'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[38]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_coin.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''猜硬币比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_coin.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/coin.png'
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
    def test_40_opengame(self):
        '''開啟骰子游戏'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[39]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_dicegame.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''骰子游戏比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_dicegame.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/dicegame.png'
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
    def test_41_opengame(self):
        '''開啟百家乐'''
        dragon = self.chrome.find_element("xpath", "//body[1]/div[1]/section[1]/section[1]/main[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[33]/td[2]/div[1]/button[1]")
        dragon.click()
        time.sleep(20)
        game_title = self.chrome.title
        print("------------------------")
        print("game_title :",game_title)
        print("------------------------")

        '''擷取主畫面'''
        save_path = os.path.join(os.path.expanduser('~'), "C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data", "background_Baccarat.png")
        self.chrome.find_element("xpath", "//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)
        time.sleep(5)
        print("------------------------")
        print("擷取主畫面 :成功")
        print("------------------------")
    
        '''百家乐比對'''
        img1 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC_data/background_Baccarat.png'
        img2 = r'C:/Users/marrash_kao/Desktop/tools/kkgame/kkgame_PIC/Baccarat.png'
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

# 啟動自動化指令，在終端機輸入: & C:/Users/你的使用者帳號/AppData/Local/Programs/Python/Python39/python.exe d:/auto_test/firstCase.py