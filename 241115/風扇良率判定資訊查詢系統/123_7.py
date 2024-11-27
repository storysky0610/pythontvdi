import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd

class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # ======= 基本設置 =======
        self.title("風扇貼標正確判斷")
        style = ttk.Style(self)
        style.configure("Topframe.Tabel", font=("Helvetica", 20))  # 標題樣式
        font1 = ("標楷體", 16)

        # ======= 讀取數據 =======
        self.df = pd.read_csv('Factoryworkstation.csv')  # 調整為你的檔案路徑
        self.data = pd.read_csv('virtual_data_with_permissions.csv')  ##
        self.frame0_data = pd.read_csv('orders_large.csv')

        # ======= 標題部分 =======
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame, text="風扇貼標歪斜檢測", font=("Helvetica", 40)).pack(padx=20, pady=20)
        topFrame.pack()

        # ======= 中間選項部分 =======
        midFrame = ttk.Frame(self)
        frame0 = ttk.Frame(midFrame)

        # ================= date  =====================
        tk.Label(frame0, text="日期:", font=font1).pack(side="left", padx=5, pady=5)
        self.date_county = tk.StringVar()
        self.date_cobox = ttk.Combobox(
            frame0, textvariable=self.date_county,
            values=self.get_date_values('Date'),
            state="readonly",
            width=15
        )
        self.date_cobox.set("請選擇日期")
        self.date_cobox.pack(side="left", padx=5)
        self.date_cobox.bind("<<ComboboxSelected>>", self.update_OrderID_options)
        # ================= date  =====================

        # ================= OrderID  =====================
        tk.Label(frame0, text="訂單號碼:", font=font1).pack(side="left", padx=5, pady=5)
        self.OrderID_county = tk.StringVar()
        self.OrderID_cobox = ttk.Combobox(
            frame0, textvariable=self.OrderID_county,
            state="readonly",
            width=15
        )
        self.OrderID_cobox.set("訂單號碼")
        self.OrderID_cobox.pack(side="left", padx=5)
        self.OrderID_cobox.bind("<<ComboboxSelected>>", self.update_Product_Quantity)  # 更新Product和Quantity選項

        # ================= OrderID  =====================

        # ================= Product  =====================
        tk.Label(frame0, text="訂單料號:", font=font1).pack(side="left", padx=5, pady=5)
        self.Product_county = tk.StringVar()
        self.Product_cobox = ttk.Combobox(
            frame0, textvariable=self.Product_county,
            state="readonly",
            width=15
        )
        self.Product_cobox.set("訂單料號")
        self.Product_cobox.pack(side="left", padx=5)

        # ================= Quantity  =====================
        tk.Label(frame0, text="訂單數量:", font=font1).pack(side="left", padx=5, pady=5)
        self.Quantity_county = tk.StringVar()
        self.Quantity_cobox = ttk.Combobox(
            frame0, textvariable=self.Quantity_county,
            state="readonly",
            width=6
        )
        self.Quantity_cobox.set("訂單數量")
        self.Quantity_cobox.pack(side="left", padx=5)
        frame0.pack()

        # ================= frame1  =====================
        # 第一排 (廠區、車間、工站)
        frame1 = ttk.Frame(midFrame)
        tk.Label(frame1, text="廠區:", font=font1).pack(side="left", padx=5, pady=5)
        self.Factory_county = tk.StringVar()
        self.Factory_cobox = ttk.Combobox(
            frame1, textvariable=self.Factory_county,
            values=self.get_unique_values('Plant'),
            state="readonly",
            width=10
        )
        self.Factory_cobox.set("請選擇廠區")
        self.Factory_cobox.pack(side="left", padx=5)
        self.Factory_cobox.bind("<<ComboboxSelected>>", self.update_workshop_options)

        tk.Label(frame1, text="車間:", font=font1).pack(side="left", padx=5, pady=5)
        self.workshop_county = tk.StringVar()
        self.workshop_cobox = ttk.Combobox(
            frame1, textvariable=self.workshop_county,
            state="readonly",
            width=10
        )
        self.workshop_cobox.set("請選擇車間")
        self.workshop_cobox.pack(side="left", padx=5)
        self.workshop_cobox.bind("<<ComboboxSelected>>", self.update_code_options)

        tk.Label(frame1, text="工站:", font=font1).pack(side="left", padx=5, pady=5)
        self.workstation_county = tk.StringVar()
        self.workstation_cobox = ttk.Combobox(
            frame1, textvariable=self.workstation_county,
            state="readonly",
            width=10
        )
        self.workstation_cobox.set("請選擇工站")
        self.workstation_cobox.pack(side="left", padx=5)

        frame1.pack(pady=10)

        # 第二排 (製造ID、品保ID、組長ID)
        frame2 = ttk.Frame(midFrame)
        tk.Label(frame2, text="製造者ID:", font=font1).pack(side="left", padx=5, pady=5)
        self.manufacturer_id = tk.StringVar()
        self.manufacturer_cobox = ttk.Combobox(
            frame2, textvariable=self.manufacturer_id,
            state="readonly",
            width=15
        )
        self.manufacturer_cobox.set("請選擇製造者ID")
        self.manufacturer_cobox.pack(side="left", padx=5)

        # 品保ID (代號 2)
        tk.Label(frame2, text="品保ID:", font=font1).pack(side="left", padx=5, pady=5)
        self.quality_control_id = tk.StringVar()
        self.quality_control_cobox = ttk.Combobox(
            frame2, textvariable=self.quality_control_id,
            state="readonly",
            width=15
        )
        self.quality_control_cobox.set("請選擇品保ID")
        self.quality_control_cobox.pack(side="left", padx=5)

        # 組長ID (代號 3)
        tk.Label(frame2, text="組長ID:", font=font1).pack(side="left", padx=5, pady=5)
        self.team_leader_id = tk.StringVar()
        self.team_leader_cobox = ttk.Combobox(
            frame2, textvariable=self.team_leader_id,
            state="readonly",
            width=15
        )
        self.team_leader_cobox.set("請選擇組長ID")
        self.team_leader_cobox.pack(side="left", padx=5)

        # 更新製造者ID、品保ID、組長ID選項
        self.update_manufacturer_options()  # 初始更新製造者ID選項
        self.update_quality_control_options()  # 初始更新品保ID選項
        self.update_team_leader_options()  # 初始更新組長ID選項

        frame2.pack(pady=10)
        frame3 = ttk.Frame(midFrame)
        tk.Label(frame3, text="製造者:", font=font1).pack(side="left", padx=5, pady=5)

        # 創建一個新的 StringVar() 用來綁定製造者名稱
        self.manufacturer_name_id = tk.StringVar()  
        self.manufacturer_name_cobox = ttk.Combobox(
            frame3, textvariable=self.manufacturer_name_id,  # 綁定新的 StringVar()
            state="readonly",
            width=15
        )
        self.manufacturer_name_cobox.set("請選擇製造者")  # 設置初始顯示文字為 "請選擇製造者"
        self.manufacturer_name_cobox.pack(side="left", padx=5)


        # 品保ID (代號 2)
        tk.Label(frame3, text="品保:", font=font1).pack(side="left", padx=5, pady=5)
        self.quality_name_id = tk.StringVar()
        self.quality_name_cobox = ttk.Combobox(
            frame3, textvariable=self.quality_control_id,
            state="readonly",
            width=15
        )
        self.quality_name_cobox.set("請選擇品保")
        self.quality_name_cobox.pack(side="left", padx=5)


        # 組長ID (代號 3)
        tk.Label(frame3, text="組長:", font=font1).pack(side="left", padx=5, pady=5)
        self.team_leader_name_id = tk.StringVar()
        self.team_leader_name_cobox = ttk.Combobox(
            frame3, textvariable=self.team_leader_id,
            state="readonly",
            width=15
        )
        self.team_leader_name_cobox.set("請選擇組長")  # 設置初始顯示文字為 "請選擇組長"
        self.team_leader_name_cobox.pack(side="left", padx=5)


        frame3.pack()

        midFrame.pack(pady=20)

    def get_date_values(self, column):
        return list(self.df[column].unique())  # 取出唯一的日期值

    def update_OrderID_options(self, event=None):
        date_value = self.date_county.get()  # 取得選中的日期
        if date_value != "請選擇日期":
            order_ids = self.df[self.df['Date'] == date_value]['OrderID'].unique()
            self.OrderID_cobox['values'] = order_ids.tolist()
            self.OrderID_cobox.set("訂單號碼")
        else:
            self.OrderID_cobox.set("請選擇訂單號碼")

    def update_Product_Quantity(self, event=None):
        order_value = self.OrderID_county.get()  
        if order_value != "訂單號碼":
            product_values = self.df[self.df['OrderID'] == order_value]['Product'].unique()
            quantity_values = self.df[self.df['OrderID'] == order_value]['Quantity'].unique()
            self.Product_cobox['values'] = product_values.tolist()
            self.Quantity_cobox['values'] = quantity_values.tolist()
            self.Product_cobox.set("訂單料號")
            self.Quantity_cobox.set("訂單數量")
        else:
            self.Product_cobox.set("請選擇訂單料號")
            self.Quantity_cobox.set("請選擇訂單數量")

    def update_workshop_options(self, event=None):
        factory_value = self.Factory_county.get()
        if factory_value != "請選擇廠區":
            workshop_values = self.data[self.data['Plant'] == factory_value]['WorkShop'].unique()
            self.workshop_cobox['values'] = workshop_values.tolist()
            self.workshop_cobox.set("請選擇車間")
        else:
            self.workshop_cobox.set("請選擇車間")

    def update_code_options(self, event=None):
        workshop_value = self.workshop_county.get()
        if workshop_value != "請選擇車間":
            workstation_values = self.data[self.data['WorkShop'] == workshop_value]['WorkStation'].unique()
            self.workstation_cobox['values'] = workstation_values.tolist()
            self.workstation_cobox.set("請選擇工站")
        else:
            self.workstation_cobox.set("請選擇工站")

    def update_manufacturer_options(self):
        manufacturer_values = self.data['ManufacturerID'].unique()
        self.manufacturer_cobox['values'] = manufacturer_values.tolist()

    def update_quality_control_options(self):
        quality_control_values = self.data['QualityControlID'].unique()
        self.quality_control_cobox['values'] = quality_control_values.tolist()

    def update_team_leader_options(self):
        team_leader_values = self.data['TeamLeaderID'].unique()
        self.team_leader_cobox['values'] = team_leader_values.tolist()

if __name__ == "__main__":
    app = Window()
    app.mainloop()
