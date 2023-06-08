# Third-Party Library Modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Local Application/Project-Specific Modules
import config

class SingletonChromeDriver:
    _instance = None


    @classmethod
    def get_instance(cls) -> webdriver.Chrome:
        """
        以 Singleton Pattern 取得 CromeDriver 的實例

        Returns
         - selenium.webdriver.Chrome: Chrome Driver
        """
        
        if cls._instance is None:
            # 開啟 google chrome driver
            service = Service(config.CHROME_DRIVER_DIR)
            d = DesiredCapabilities.CHROME
            d["goog:loggingPrefs"] = {"browser": "ALL"}
            cls._instance = webdriver.Chrome(service=service, desired_capabilities=d)
            
            # 設定當找不到網頁元素時的最長等待時間
            cls._instance.implicitly_wait(10)

        return cls._instance
