# Standard Library Modules
import os
import unittest

# Third-Party Library Modules
from BeautifulReport import BeautifulReport

# Local Application/Project-Specific Modules
import config

from g4_tester import G4Tester
from g7_tester import G7Tester
from g8_tester import G8Tester
from g9_tester import G9Tester
from g10_tester import G10Tester

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
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(G4Tester))
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(G7Tester))
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(G8Tester))
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(G9Tester))
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(G10Tester))

    # 輸出結果報告
    BeautifulReport(testunit).report(
        filename = f"kkgame_report_{config.DATE}", 
        description = f"KKGAME_測試報告({config.DATE})", 
        log_path = config.REPORT_GEN_DIR
    )
