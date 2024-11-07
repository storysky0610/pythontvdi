# import sqlite3
# import json
# with open('lesson6/homework/data.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)
#     records_data = data['records']    
#     records = []
#     seen = set()
#     for entry in records_data:
#         if isinstance(entry, dict):  # 確保 entry 是字典
#             # 取得資料並處理空值
#             sitename = entry.get('sitename', '')
#             county = entry.get('county', '')
#             aqi = entry.get('aqi', '0')  # 預設為 0
#             status = entry.get('status', '')
#             pm25 = entry.get('pm2.5', '0.0')  # 預設為 0.0
#             datacreationdate = entry.get('datacreationdate', '')
#             latitude = entry.get('latitude', '0.0')  # 預設為 0.0
#             longitude = entry.get('longitude', '0.0')  # 預設為 0.0
            
#             # 將字符串轉換為適當的類型，並處理可能的轉換錯誤
#             try:
#                 record = (
#                     sitename,
#                     county,
#                     int(aqi),  # 將 AQI 轉換為整數
#                     status,
#                     float(pm25),  # 將 PM2.5 轉換為浮點數
#                     datacreationdate,
#                     float(latitude),  # 將 latitude 轉換為浮點數
#                     float(longitude)  # 將 longitude 轉換為浮點數
#                 )

#                 if record not in seen:
#                     records.append(record)
#                     seen.add(record)

#             except ValueError as e:
#                 print('')

#     # 匯入資料到 SQLite 資料庫
#     conn = sqlite3.connect("lesson6/homework/AQI.db")
#     cursor = conn.cursor()

#     # 批量插入數據到 records 表中
#     cursor.executemany('''
#         INSERT INTO records (sitename, county, aqi, status, pm25, date, lat, lon)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     ''', records)
#     conn.commit()
#     cursor.close()
#     conn.close()
#     print("數據已成功匯入到資料庫！")

import sqlite3
import json
with open('lesson6/homework/data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    records_data = data['records']    
    records = []
    seen = set()
    for entry in records_data:
        if isinstance(entry, dict):  # 確保 entry 是字典
            # 取得資料並處理空值
            sitename = entry.get('sitename', '')
            county = entry.get('county', '')
            aqi = entry.get('aqi', '0')  # 預設為 0
            status = entry.get('status', '')
            pm25 = entry.get('pm2.5', '0.0')  # 預設為 0.0
            datacreationdate = entry.get('datacreationdate', '')
            latitude = entry.get('latitude', '0.0')  # 預設為 0.0
            longitude = entry.get('longitude', '0.0')  # 預設為 0.0
            
            # 將字符串轉換為適當的類型，並處理可能的轉換錯誤
            try:
                record = (
                    sitename,
                    county,
                    int(aqi),  # 將 AQI 轉換為整數
                    status,
                    float(pm25),  # 將 PM2.5 轉換為浮點數
                    datacreationdate,
                    float(latitude),  # 將 latitude 轉換為浮點數
                    float(longitude)  # 將 longitude 轉換為浮點數
                )

                if record not in seen:
                    records.append(record)
                    seen.add(record)

            except ValueError as e:
                print('')

    # 匯入資料到 SQLite 資料庫
    conn = sqlite3.connect("lesson6/homework/AQI.db")
    cursor = conn.cursor()

    # 批量插入數據到 records 表中
    cursor.executemany('''
        INSERT INTO records (sitename, county, aqi, status, pm25, date, lat, lon)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', records)
    conn.commit()
    cursor.close()
    conn.close()
    print("數據已成功匯入到資料庫！")
