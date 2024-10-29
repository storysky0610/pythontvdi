from datetime import datetime, timedelta
import time
import json
import requests
import os
import download
download.download_file()
def get_sitename()->list[str]:
    with open('lesson6\homework\data.json',encoding='utf-8',newline='') as ff:
       data = json.load(ff)  # 讀取檔案的原始內容
       sitenames = set()
    for items in data['records']:
        sitenames.add(items['sitename'])
    sitenames = list(sitenames)
    return sitenames
    
def get_selected_data(sitename:str)->list[list]:
    with open('lesson6\homework\data.json',encoding='utf-8',newline='') as ff:
       data = json.load(ff)  # 讀取檔案的原始內容
       outerlist = []
       for items in data['records']:
            if items['sitename'] == sitename:
                innerlist = [items['datacreationdate'],items['county'],items['aqi'],items['pm2.5'],items['status'],items['latitude'],items['longitude']]
                outerlist.append(innerlist)       
       return outerlist

