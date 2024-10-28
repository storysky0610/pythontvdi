import os
import requests
from datetime import datetime, timedelta
import sqltool

def download_file():
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    filename = 'lesson6/homework/data.json'  # 設定下載的檔案名稱
    download_time_file = 'lesson6/homework/download_time.txt'  # 記錄下載時間的檔案

    # 檢查是否有下載過的時間記錄
    if os.path.exists(download_time_file):
        with open(download_time_file, 'r') as f:
            last_download_time = datetime.fromisoformat(f.read().strip())
            print(f"上次下載時間: {last_download_time}")
    else:
        last_download_time = None
        print("未找到下載時間記錄。")

    # 計算現在時間
    current_time = datetime.now()
    print(f"現在時間: {current_time}")

    # 如果檔案不存在或已超過五秒，則刪除檔案並下載新的檔案
    if not os.path.exists(filename) or (last_download_time and current_time > last_download_time + timedelta(hours=1)):
        # 刪除舊檔案（如果存在）
        if os.path.exists(filename):
            os.remove(filename)
            sqltool.deleAOI()
            print(f"舊檔案 {filename} 已刪除。")

        response = requests.get(url)

        # 儲存檔案
        with open(filename, 'w', encoding='utf-8') as ff:
            ff.write(response.text)
            sqltool.addAQI()

        # 更新下載時間
        with open(download_time_file, 'w') as f:
            f.write(current_time.isoformat())

        print(f"檔案已下載並儲存為 {filename}")
    else:
        print("檔案已存在，且在一小時內不需要重複下載。")

# 測試下載函數
download_file()
