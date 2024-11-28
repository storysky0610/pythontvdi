import tkinter as tk  # 載入 tkinter 用來建立圖形界面
from tkinter import ttk  # 載入 ttk 用來設置更美觀的控件
from ttkthemes import ThemedTk  # 載入 ttkthemes 用來設置主題
import pandas as pd  # 載入 pandas 用來處理數據
from tkinter import Tk, Label  # 載入 Tk 和 Label，用於顯示文字
from PIL import Image, ImageTk  # 載入 PIL 用來處理圖像

class Window(ThemedTk):  # 定義一個 Window 類，繼承 ThemedTk
    def __init__(self, *args, **kwargs):
        super().__init__()  # 初始化父類別
        # ======= 基本設置 =======
        self.title("風扇貼標正確判斷")  # 設定窗口標題
        style = ttk.Style(self)  # 創建一個樣式對象
        style.configure("Topframe.Tabel", font=("Helvetica", 20))  # 設定標題樣式
        font1 = ("標楷體", 12)  # 設定字體樣式

        # ======= 讀取數據 =======
        self.df = pd.read_csv('Factoryworkstation.csv')  # 讀取工廠工作站的數據
        self.data = pd.read_csv('virtual_data_with_permissions.csv')  # 讀取虛擬數據，包含權限
        self.frame0_data = pd.read_csv('orders_large.csv')  # 讀取訂單數據

        # ======= 標題部分 =======
        topFrame = ttk.Frame(self)  # 創建一個框架來放置標題
        ttk.Label(topFrame, text="風扇貼標歪斜檢測", font=("Helvetica", 40)).pack(padx=20, pady=20)  # 設置標題文字和字體
        topFrame.pack()  # 將標題框架加入視窗

        # ======= 中間選項部分 =======
        midFrame = ttk.Frame(self)  # 創建一個中間框架
        frame0 = ttk.Frame(midFrame)  # 創建一個內部框架

        # ================= date  =====================
        tk.Label(frame0, text="日期:", font=font1).pack(side="left", padx=5, pady=5)  # 添加日期標籤
        self.date_county = tk.StringVar()  # 創建一個變數來存儲日期選擇
        self.date_cobox = ttk.Combobox(frame0, textvariable=self.date_county, values=self.get_date_values('Date'), state="readonly", width=10)  # 創建下拉選單顯示日期
        self.date_cobox.set("請選擇日期")  # 預設顯示文字
        self.date_cobox.pack(side="left", padx=5)  # 將日期選項框放入框架
        self.date_cobox.bind("<<ComboboxSelected>>", self.update_OrderID_options)  # 綁定選擇事件來更新訂單號碼

        # ================= OrderID  =====================
        tk.Label(frame0, text="訂單號碼:", font=font1).pack(side="left", padx=5, pady=5)  # 添加訂單號碼標籤
        self.OrderID_county = tk.StringVar()  # 創建變數來存儲選擇的訂單號碼
        self.OrderID_cobox = ttk.Combobox(frame0, textvariable=self.OrderID_county, state="readonly", width=10)  # 創建訂單號碼的下拉選單
        self.OrderID_cobox.set("訂單號碼")  # 設置預設顯示文字
        self.OrderID_cobox.pack(side="left", padx=5)  # 放置訂單號碼選項框
        self.OrderID_cobox.bind("<<ComboboxSelected>>", self.update_Product_Quantity)  # 綁定事件來更新產品和數量

        # ================= Product  =====================
        tk.Label(frame0, text="訂單料號:", font=font1).pack(side="left", padx=5, pady=5)  # 添加訂單料號標籤
        self.Product_county = tk.StringVar()  # 存儲選擇的訂單料號
        self.Product_cobox = ttk.Combobox(frame0, textvariable=self.Product_county, state="readonly", width=15)  # 創建訂單料號下拉選單
        self.Product_cobox.set("訂單料號")  # 設置預設顯示文字
        self.Product_cobox.pack(side="left", padx=5)  # 放置訂單料號選項框

        # ================= Quantity  =====================
        tk.Label(frame0, text="訂單數量:", font=font1).pack(side="left", padx=5, pady=5)  # 添加訂單數量標籤
        self.Quantity_county = tk.StringVar()  # 存儲選擇的訂單數量
        self.Quantity_cobox = ttk.Combobox(frame0, textvariable=self.Quantity_county, state="readonly", width=8)  # 創建訂單數量下拉選單
        self.Quantity_cobox.set("訂單數量")  # 設置預設顯示文字
        self.Quantity_cobox.pack(side="left", padx=5)  # 放置訂單數量選項框
        frame0.pack()  # 放置訂單框架

        # ================= Factory  =====================
        tk.Label(frame0, text="廠區:", font=font1).pack(side="left", padx=5, pady=5)  # 添加廠區標籤
        self.Factory_county = tk.StringVar()  # 存儲選擇的廠區
        self.Factory_cobox = ttk.Combobox(frame0, textvariable=self.Factory_county, values=self.get_unique_values('Plant'), state="readonly", width=10)  # 創建廠區下拉選單
        self.Factory_cobox.set("請選擇廠區")  # 設置預設顯示文字
        self.Factory_cobox.pack(side="left", padx=5)  # 放置廠區選項框
        self.Factory_cobox.bind("<<ComboboxSelected>>", self.update_workshop_options)  # 綁定選擇廠區後的事件來更新車間選項

        # ================= workshop  ====================
        tk.Label(frame0, text="車間:", font=font1).pack(side="left", padx=5, pady=5)  # 添加車間標籤
        self.workshop_county = tk.StringVar()  # 存儲選擇的車間
        self.workshop_cobox = ttk.Combobox(frame0, textvariable=self.workshop_county, state="readonly", width=10)  # 創建車間下拉選單
        self.workshop_cobox.set("請選擇車間")  # 設置預設顯示文字
        self.workshop_cobox.pack(side="left", padx=5)  # 放置車間選項框
        self.workshop_cobox.bind("<<ComboboxSelected>>", self.update_code_options)  # 綁定車間選擇後的事件來更新工站選項

        # ================= workstation ===================
        tk.Label(frame0, text="工站:", font=font1).pack(side="left", padx=5, pady=5)  # 添加工站標籤
        self.workstation_county = tk.StringVar()  # 存儲選擇的工站
        self.workstation_cobox = ttk.Combobox(frame0, textvariable=self.workstation_county, state="readonly", width=10)  # 創建工站下拉選單
        self.workstation_cobox.set("請選擇工站")  # 設置預設顯示文字
        self.workstation_cobox.pack(side="left", padx=5)  # 放置工站選項框

        # ========================= 製造ID ================================
        frame2 = ttk.Frame(midFrame)  # 創建另一個框架來放製造者等選項
        tk.Label(frame2, text="製造者ID:", font=font1).pack(side="left", padx=5, pady=5)  # 添加製造者ID標籤
        self.manufacturer_id = tk.StringVar()  # 存儲製造者ID
        self.manufacturer_cobox = ttk.Combobox(frame2, textvariable=self.manufacturer_id, state="readonly", width=15)  # 創建製造者ID下拉選單
        self.manufacturer_cobox.set("請選擇製造者ID")  # 設置預設顯示文字
        self.manufacturer_cobox.pack(side="left", padx=5)  # 放置製造者ID選項框

        # ======================= 顯示框架 ============================
        midFrame.pack(padx=10, pady=10)  # 顯示中間框架

    # 以下是更新選項的函數，實現根據用戶的選擇更新其它選項
    def get_date_values(self, column_name):
        return sorted(self.df[column_name].unique())  # 返回日期的唯一值

    def update_OrderID_options(self, event=None):
        # 根據選擇的日期更新訂單號碼選項
        date = self.date_county.get()
        filtered_data = self.df[self.df['Date'] == date]
        self.OrderID_cobox['values'] = filtered_data['OrderID'].unique()

    def update_Product_Quantity(self, event=None):
        # 根據選擇的訂單號碼更新訂單料號和數量
        order_id = self.OrderID_county.get()
        filtered_data = self.df[self.df['OrderID'] == order_id]
        self.Product_cobox['values'] = filtered_data['Product'].unique()
        self.Quantity_cobox['values'] = filtered_data['Quantity'].unique()

    def update_workshop_options(self, event=None):
        # 根據選擇的廠區更新車間選項
        factory = self.Factory_county.get()
        filtered_data = self.df[self.df['Plant'] == factory]
        self.workshop_cobox['values'] = filtered_data['Workshop'].unique()

    def update_code_options(self, event=None):
        # 根據選擇的車間更新工站選項
        workshop = self.workshop_county.get()
        filtered_data = self.df[self.df['Workshop'] == workshop]
        self.workstation_cobox['values'] = filtered_data['Workstation'].unique()

# 執行應用程序
if __name__ == "__main__":
    window = Window()  # 創建窗口對象
    window.mainloop()  # 進入主循環
