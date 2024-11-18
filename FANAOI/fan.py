import tkinter as tk
from tkinter import ttk
import pandas as pd

# 读取CSV文件，获取Plant、Workstation Code和Code数据
csv_file = r'FANAOI\Factoryworkstation.csv'  # 请替换为你的实际路径
df = pd.read_csv(csv_file)  # 使用Pandas读取CSV文件并存储为DataFrame

# 提取Plant和Workstation Code列，去除重复值
plant_list = df['Plant'].dropna().unique().tolist()  # 获取唯一的厂区名称，去除空值并转换为列表

# 创建GUI窗口
root = tk.Tk()  # 创建根窗口
root.title("Factory Workstation Selector")  # 设置窗口标题
root.geometry("400x200")  # 设置窗口尺寸

# 设置窗口居中
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())  # 使窗口居中显示

# 设置grid布局
root.columnconfigure(0, weight=1, minsize=100)  # 第一列用于标签，设置最小宽度
root.columnconfigure(1, weight=2, minsize=150)  # 第二列用于输入框（下拉菜单）

# 统一的函数：创建和更新下拉菜单
def create_combobox(label_text, row, combobox_name, values=None, event=None):
    """
    创建一个带标签和下拉菜单的组合框
    """
    # 标签
    label = tk.Label(root, text=label_text)  # 创建标签
    label.grid(row=row, column=0, padx=10, pady=5, sticky="w")  # 将标签放置在指定位置

    # 下拉菜单
    combobox = ttk.Combobox(root, values=values, state="readonly")  # 创建下拉菜单，设为只读
    combobox.grid(row=row, column=1, padx=10, pady=5)  # 将下拉菜单放置在指定位置

    # 绑定选择事件（如果提供）
    if event:
        combobox.bind('<<ComboboxSelected>>', event)  # 绑定选择事件到指定的函数

    return combobox  # 返回创建的组合框

# 更新 Workstation Code 选项的函数
def update_workstation_options(event):
    """
    根据选择的Plant，更新Workstation Code下拉菜单的内容
    """
    selected_plant = plant_combobox.get()  # 获取选择的Plant值
    if selected_plant:  # 如果选择了厂区
        # 根据选择的Plant，过滤出对应的Workstation Code
        filtered_workstations = df[df['Plant'] == selected_plant]['Workstation Code'].unique().tolist()  
        workstation_combobox['values'] = filtered_workstations  # 更新Workstation Code的选项
        workstation_combobox.set('')  # 清空之前的选择
        code_combobox.set('')  # 清空Code选项

# 更新 Code 选项的函数
def update_code_options(event):
    """
    根据选择的Plant和Workstation Code，更新Code下拉菜单的内容
    """
    selected_plant = plant_combobox.get()  # 获取选择的Plant值
    selected_workstation = workstation_combobox.get()  # 获取选择的Workstation Code值
    if selected_plant and selected_workstation:  # 如果都已选择
        # 根据选择的Plant和Workstation Code，过滤出对应的Code
        filtered_codes = df[(df['Plant'] == selected_plant) & 
                             (df['Workstation Code'] == selected_workstation)]['Code'].unique().tolist()
        code_combobox['values'] = filtered_codes  # 更新Code的选项
        code_combobox.set('')  # 清空Code选择

# 创建Plant、Workstation Code和Code下拉菜单
plant_combobox = create_combobox("工廠:", 0, 'plant', plant_list, update_workstation_options)  # 创建Plant选择框
workstation_combobox = create_combobox("車間:", 1, 'workstation', event=update_code_options)  # 创建Workstation选择框
code_combobox = create_combobox("工站:", 2, 'code')  # 创建Code选择框

# 提交按钮，输出选择的Plant、Workstation Code和Code
def submit_selection():
    """
    提交选择的Plant、Workstation Code和Code，并输出到控制台
    """
    selected_plant = plant_combobox.get()  # 获取选择的Plant值
    selected_workstation = workstation_combobox.get()  # 获取选择的Workstation Code值
    selected_code = code_combobox.get()  # 获取选择的Code值
    if selected_plant and selected_workstation and selected_code:  # 确保所有值都已选择
        print(f"Selected Plant: {selected_plant}")  # 打印选择的Plant
        print(f"Selected Workstation Code: {selected_workstation}")  # 打印选择的Workstation Code
        print(f"Selected Code: {selected_code}")  # 打印选择的Code
    else:
        print("Please select Plant, Workstation Code, and Code.")  # 提示用户选择所有字段

# 提交按钮
submit_button = tk.Button(root, text="Submit", command=submit_selection)  # 创建提交按钮，点击时调用submit_selection函数
submit_button.grid(row=3, column=0, columnspan=2, pady=20)  # 将按钮放置在指定位置，跨越两列

# 运行GUI
root.mainloop()  # 启动GUI应用，进入主事件循环
