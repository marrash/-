# KKGame Slot Regression Testing Tool

- [KKGame Slot Regression Testing Tool](#kkgame-slot-regression-testing-tool)
  - [Summary](#summary)
  - [TO DO](#to-do)
  - [Quick Start](#quick-start)
    - [安裝 Python Modules](#安裝-python-modules)
    - [啟動自動化腳本](#啟動自動化腳本)
  - [Add Tester](#add-tester)
      - [Step.1 複製範本](#step1-複製範本)
      - [Step.2-1 修改參數](#step2-1-修改參數)
      - [Step.2-2 修改流程](#step2-2-修改流程)
      - [Step.3 添加測試流程](#step3-添加測試流程)
  - [Project Layout](#project-layout)
  - [Documentations](#documentations)
  - [References](#references)

--- 

## Summary

針對 KKGame 老虎機類型遊戲進行畫面評測的自動化整合測試工具  

---

## TO DO

基礎框架已經開發完畢，以下是框架未來可以繼續迭代的方向:  
 - `unittest.TestCase` 抽取成父類別，所有遊戲的測試模組繼承後僅調整需要部分
 - 驗證內容不僅只包含盤面結果，而是包含動畫特效驗證
   - `ground_truth` 保存一段長時間影片，驗證過程中錄下轉動過程後與 `ground_truth` 比對匹配程度
   - i.e. 錄影為子集合，理論上應該要 100% 連續出現在 `ground_truth` 中的某個部分
 - 測試報告內容擴充
   - 載入時間紀錄
   - Console 錯誤訊息紀錄

---

## Quick Start

### 安裝 Python Modules

首次下載該專案時，可以執行該指令安裝該專案所需使用到的第三方模組

```shell
make install_requirements
```

### 啟動自動化腳本

執行該指令後，會開始執行老虎機整合測試流程

```shell
make run
```

---

## Add Tester

新增一款新遊戲測試模組的最小流程，依照各遊戲不同可能還需額外調整  
這裡只說明最基礎的流程，以新增一款 `G7封神榜` 為例

#### Step.1 複製範本

複製 `g4_tester.py` 後將檔案更名成 `g7_tester.py`

#### Step.2-1 修改參數

打開 `g7_tester.py` 的檔案，在 `setUpClass` 函式裡管理所有測試流程會使用到的基本參數，如下

```python
...

@classmethod
def setUpClass(cls):
  cls.GAME_ID = "4" # 遊戲編號
  cls.WEBDRIVER_TIMEOUT = 10 # WebDriverWait 的條件等待時間
  cls.LOADING_DELAY = 5 # 載入等待時間
  cls.SPIN_DEALY = 5 # 下注表演等待時間
  cls.PANNEL_HEIGHT_RATIO = (0.39, 0.75) # 老虎機面板範圍 (以百分比表示艱鉅)
  cls.SIMILARITY = 0.95 # 比對相似度閥值

  cls.chrome = SingletonChromeDriver.get_instance()
  cls.cheat_table = {
    "params": {
      "key": f"{config.KK_ADMIN_USER}-{cls.GAME_ID}", 
      "data": {
        "baseGame": [3, 1, 1, 1, 13], 
        "longWildIndex": -1, 
        "cheatCase": 0
      }
    }
  }

...
```

- `cls.GAME_ID` 改成 `"7"`
- `cls.PANNEL_HEIGHT_RATIO` 根據不同遊戲的盤面高度不同，需要使用工具確認高度範圍後修改 **(註1)**
- 其餘參數根據情境而定，可以自行調整

**註1:**  

確認盤面高度範圍可以使用 `image_similarity.py` 裡面的函式 `preview_cropped_image` 來調整並預覽擷取範圍  
範例如下:

```python
if __name__ == '__main__':
  image_path = r'./KKGAME_PIC/G7_ground_truth.png'
  height_range = (0.39, 0.75)
  width_range = (0, 1)

  preview_cropped_image(image_path, height_range, width_range)
```

#### Step.2-2 修改流程

如果遊戲類型與你想複製的不同 (e.g. 直橫版) 時，可能會遇到自動化流程點擊不到 spin 按鈕的問題  
這時可以在對應的 `testcase` 內修改操作流程，範例如下:

```python
def test_02_open_kkgame(self):
  
  ...

  # 點擊 spin
  spin_x_offset = 0
  spin_y_offset = (canvas_height/2) - (canvas_height - (canvas_height*0.9))

  actions = ActionChains(self.chrome)
  actions.move_to_element_with_offset(canvas, spin_x_offset, spin_y_offset).click().perform()

  ...
```

可以在這個地分調整滑鼠位移的偏移量 *(offset)* 以滿足需求

#### Step.3 添加測試流程

完成一款遊戲的測試模組 *(unittest.TestCase)* 後，需要把測試模組加入主流程 `slot_testflow.py`  
請在程式碼內添加你的測試模組，範例如下:  

```python
testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(G7Tester))
```

以上，就是新增一款遊戲測試模組的最小流程

---

## Project Layout

```text
KKGame Slot Regression Testing Tool
 ├─ BIN/                 # 保存所有可供使用的第三方執行檔
 ├─ KKGAME_PIC/          # 保存各遊戲用來提供影像辨識比對的圖片 (ground truth)
 ├─ KKGAME_REPORT/       # 保存每次整合測試的結果報告
 ├─ .gitignore           #
 ├─ chrome_driver.py     # Selenium ChromeDriver 單例模式
 ├─ config.py            # 整合測試時引用的參數檔
 ├─ g{gameid}_tester.py  # 每款遊戲各自的測試流程
 ├─ ..                   #
 ├─ image_similarity.py  # 圖片相似度比對函式庫
 ├─ makefile             # 
 ├─ README.md            # 
 ├─ report_template.py   # 輸出報告使用的 HTML 格式模板
 ├─ requirements.txt     # 該專案所依賴的 python 第三方模組列表
 ├─ slot_testflow.py     # 老虎機整合測試流程
 └─ util.py              # 輔助工具函式庫
```

---

## Documentations

施工中 ...

---

## References

施工中 ...
