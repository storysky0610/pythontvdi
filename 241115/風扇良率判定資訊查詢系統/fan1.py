import tkinter as tk
from tkinter import ttk
import pandas as pd
import csv

df = pd.read_csv('Factoryworkstation.csv')

plant_list = df['Plant'].dropna().unique().tolist()
WorkstationCode_list = (df[df['Plant'].isin(plant_list)]['Workstation Code'].dropna().unique().tolist())
Code_list = (df[df['Workstation Code'].isin(WorkstationCode_list)]['Code'].dropna().unique().tolist())


    # 讀取CSV檔案
data = pd.read_csv('virtual_data_with_permissions.csv')

    # 根據權限代號過濾各角色
roles = {
        "製造者": data[data['權限代號'] == 1].set_index('ID')['姓名'].to_dict(),
        "組長": data[data['權限代號'] == 2].set_index('ID')['姓名'].to_dict(),
        "品保員": data[data['權限代號'] == 3].set_index('ID')['姓名'].to_dict(),
    }