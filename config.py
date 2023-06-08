from datetime import datetime
import os

# 執行當下的時間
DATE = datetime.now().strftime("%Y%m%d_%H%M%S")

# 專案根目錄路徑
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# 提供比對圖片的保存路徑
GROUND_TRUTU_DIR = os.path.join(BASE_DIR, "KKGAME_PIC")

# 提供整合測試報告的根目錄路徑
REPORT_ROOT_DIR = os.path.join(BASE_DIR, "KKGAME_REPORT")

# 提供本次整合測試的保存路徑
REPORT_GEN_DIR = os.path.join(REPORT_ROOT_DIR, f"kkgame_report_{DATE}")

# Google Chrome Driver 路徑
CHROME_DRIVER_DIR = os.path.join(BASE_DIR, "BIN", "chromedriver.exe")

# KKGame 管理後台 URL
KK_ADMIN_URL = "http://egame.uat.kk168-01.com"

# KKGame 管理後台語系
KK_ADMIN_LANG = "zh-cn"

# KKGame 管理後台渠道
KK_ADMIN_ECSITE = "1"

# KKGame 管理後台使用者帳號
KK_ADMIN_USER = "brent_y"

# KKGame 管理後台使用密碼
KK_ADMIN_PASSWORD = "123456"

# KKGame 配牌器 URL
KK_WEBTOOL_URL = "http://webdevtool.uat.kk168-01.com"