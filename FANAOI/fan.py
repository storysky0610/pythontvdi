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
root.geometry("400x200")

# 设置窗口居中
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

# 设置grid布局
root.columnconfigure(0, weight=1, minsize=100)  # 第一列用于标签，设置最小宽度
root.columnconfigure(1, weight=2, minsize=150)  # 第二列用于输入框（下拉菜单）

# 统一的函数：创建和更新下拉菜单
def create_combobox(label_text, row, combobox_name, values=None, event=None):
    # 标签
    label = tk.Label(root, text=label_text)
    label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

    # 下拉菜单
    combobox = ttk.Combobox(root, values=values, state="readonly")
    combobox.grid(row=row, column=1, padx=10, pady=5)

    # 绑定选择事件（如果提供）
    if event:
        combobox.bind('<<ComboboxSelected>>', event)

    return combobox

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

# 创建Plant、Workstation Code和Code下拉菜单
plant_combobox = create_combobox("工廠:", 0, 'plant', plant_list, update_workstation_options)
workstation_combobox = create_combobox("車間:", 1, 'workstation', event=update_code_options)
code_combobox = create_combobox("工站:", 2, 'code')

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
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# 运行GUI
root.mainloop()
