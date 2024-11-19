import tkinter as tk
from tkinter import ttk
import pandas as pd
import csv

# 读取CSV文件，获取Plant、Workstation Code和Code数据
csv_file =  r'C:\Users\user\Documents\GitHub\tivd\pythontvdi\241115\Factoryworkstation.csv' # 请替换为你的实际路径
df = pd.read_csv(csv_file)
# print(df)  # 打印数据框以检查内容
# 提取Plant和Workstation Code列，去除重复值
plant_list = df['Plant'].dropna().unique().tolist()
Code_list = df['Code'].dropna().unique().tolist()
WorkstationCode_list = df['Workstation Code'].dropna().unique().tolist()

print(plant_list)
print(WorkstationCode_list)
print(Code_list)
