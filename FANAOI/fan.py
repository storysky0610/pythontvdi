import tkinter as tk
from tkinter import ttk
import pandas as pd

# 读取CSV文件，获取Plant、Workstation Code和Code数据
csv_file = r'FANAOI\Factoryworkstation.csv'  # 请替换为你的实际路径
df = pd.read_csv(csv_file)

# 提取Plant和Workstation Code列，去除重复值
plant_list = df['Plant'].dropna().unique().tolist()

# 创建GUI窗口
root = tk.Tk()
root.title("Factory Workstation Selector")
root.geometry("500x300")

# 标签
label_plant = tk.Label(root, text="Select Plant:")
label_plant.pack(pady=10)

# Plant下拉菜单
plant_combobox = ttk.Combobox(root, values=plant_list, state="readonly")
plant_combobox.pack(pady=10)

# 标签
label_workstation = tk.Label(root, text="Select Workstation Code:")
label_workstation.pack(pady=10)

# Workstation下拉菜单
workstation_combobox = ttk.Combobox(root, state="readonly")
workstation_combobox.pack(pady=10)

# 标签
label_code = tk.Label(root, text="Select Code:")
label_code.pack(pady=10)

# Code下拉菜单
code_combobox = ttk.Combobox(root, state="readonly")
code_combobox.pack(pady=10)

# 更新 Workstation Code 选项的函数
def update_workstation_options(event):
    selected_plant = plant_combobox.get()
    if selected_plant:
        # 根据选择的Plant，过滤出对应的Workstation Code
        filtered_workstations = df[df['Plant'] == selected_plant]['Workstation Code'].unique().tolist()
        workstation_combobox['values'] = filtered_workstations
        workstation_combobox.set('')  # 清空之前的选择
        code_combobox.set('')  # 清空Code选项

# 更新 Code 选项的函数
def update_code_options(event):
    selected_plant = plant_combobox.get()
    selected_workstation = workstation_combobox.get()
    if selected_plant and selected_workstation:
        # 根据选择的Plant和Workstation Code，过滤出对应的Code
        filtered_codes = df[(df['Plant'] == selected_plant) & 
                             (df['Workstation Code'] == selected_workstation)]['Code'].unique().tolist()
        code_combobox['values'] = filtered_codes
        code_combobox.set('')  # 清空Code选择

# 绑定Plant和Workstation Code下拉菜单的选择事件
plant_combobox.bind('<<ComboboxSelected>>', update_workstation_options)
workstation_combobox.bind('<<ComboboxSelected>>', update_code_options)

# 提交按钮，输出选择的Plant、Workstation Code和Code
def submit_selection():
    selected_plant = plant_combobox.get()
    selected_workstation = workstation_combobox.get()
    selected_code = code_combobox.get()
    if selected_plant and selected_workstation and selected_code:
        print(f"Selected Plant: {selected_plant}")
        print(f"Selected Workstation Code: {selected_workstation}")
        print(f"Selected Code: {selected_code}")
    else:
        print("Please select Plant, Workstation Code, and Code.")

# 提交按钮
submit_button = tk.Button(root, text="Submit", command=submit_selection)
submit_button.pack(pady=20)

# 运行GUI
root.mainloop()
