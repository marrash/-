結合openCV+selenium+beatifulreport
使用工具 (可依據需求進行使用)
python
Selenium介紹及應用
BeautifulReport測試報告介紹及應用
系統
Windows
測試裝置
 1.桌機

Selenium介紹及應用
介紹 : Selenium 是為瀏覽器自動化（Browser Automation）需求所設計的一套工具集合，讓程式可以直接驅動瀏覽器進行各種網站操作。



常用語法 : 

# 引用webdriver

chrome = webdriver.Chrome(r'webdriver位置', chrome_options=options)

--------------------------------------------------------------------------------------

# 開啟要爬的網址

chrome.get('網址')

--------------------------------------------------------------------------------------

# 取得網站的title

title = chrome.title

--------------------------------------------------------------------------------------

# 退出瀏覽器

chrome.quit()

--------------------------------------------------------------------------------------

# 應用find_element_by_ 來建立物件

user = self.chrome.find_element_by_xpath('xpath')

password = self.chrome.find_element_by_xpath("xpath")

--------------------------------------------------------------------------------------

# 應用send_keys()來模擬使用者輸入的資料

user.send_keys('user')

password.send_keys('password')

--------------------------------------------------------------------------------------

# click點擊滑鼠

a.chrome.find_element_by_xpath("xpath")

a.click()

--------------------------------------------------------------------------------------

# 移動滑鼠座標pyautogui.moveTo

pyautogui.moveTo(x,y)

--------------------------------------------------------------------------------------

# 返回上一頁back

chrome.back()

--------------------------------------------------------------------------------------

# 截取瀏覽器畫面

save_path = os.path.join(os.path.expanduser('~'), "截圖存放路徑", "檔案名稱")

self.chrome.find_element_by_xpath("//div[@id='Cocos2dGameContainer']//canvas[1]").screenshot(save_path)

BeautifulReport介紹及應用
介紹 : 測試用例模板,可以把測試中的結果整合成一個可視化的HTML測試報告

![image](https://user-images.githubusercontent.com/47851007/187381975-70290dda-ee48-4410-a6f5-100fc24b4109.png)


應用 : 



filename → 測試報告綁案名稱。

description -> 用例名稱。

1.測試類 : 會依照class名稱來命名。

2.測試方法 : 會依照def名稱來命名，每一個def表是一個測試方法，10個def測試報告就會有10個測試放法。

3. 用例描述 : 會依照'''XXX'''中內容來命名。

'''開啟深海历险'''

4.操作 : 會依照print結果呈現。

5.報告結果
![image](https://user-images.githubusercontent.com/47851007/187382085-5340b73f-dc26-4e9c-ac0e-4cb14e5502bd.png)







可能碰到的問題
--------------------------------------------------------------------------------------

Selenium 4.3以上版本

# 應用find_element_by_ 來建立物件，會遇到此用法已無法使用

目前一律都修改為 find_element(byXXXX, 'xx')

需要額外import    from selenium.webdriver.common.by import By

所以會修改為

user = self.chrome.find_element("xpath", "實際的path")
password = self.chrome.find_element("xpath","實際的path")



--------------------------------------------------------------------------------------

Beatifulreport報告顯示異常



沒有顯示圖片與結果
![image](https://user-images.githubusercontent.com/47851007/187382191-032d15a2-73b4-4cf7-9081-913abca3215d.png)



先前往 C:\Users\XXXX\AppData\Local\Programs\Python\Python39\Lib\site-packages\BeautifulReport\template   進行修正

將檔案template開啟

![image](https://user-images.githubusercontent.com/47851007/187382251-7ba6618f-7037-4de8-8d21-a7150be97b0f.png)




將cdn.bootcss.com修改為cdnjs.cloudflare.com/ajax/libs/

顯示異常主要問題為 cdn網址失效，需要更換一個CDN，更換後重新執行一次測試案例，所產出報告即可正常顯示
![image](https://user-images.githubusercontent.com/47851007/187382311-a02aabbf-cb65-4311-988c-ec2ec4794738.png)







腳本提供
執行腳本前需變更webdriver、原圖及截圖存放路徑，且需建立報告及圖片存放的資料夾
