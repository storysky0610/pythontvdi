import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
from tkinter import Tk, Label
from PIL import Image, ImageTk  # 載入PIL庫
import csv

class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # ======= 基本設置 =======
        self.title("風扇貼標正確判斷")
        style = ttk.Style(self)
        style.configure("Topframe.Tabel", font=("Helvetica", 20))  # 標題樣式
        font1 = ("標楷體", 12)

        # ======= 讀取數據 =======
        self.df = pd.read_csv('Factoryworkstation.csv')  # 調整為你的檔案路徑
        self.data = pd.read_csv('virtual_data_with_permissions.csv')##
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
        self.date_cobox = ttk.Combobox(frame0, textvariable=self.date_county,values=self.get_date_values('Date'),state="readonly",width=10)
        self.date_cobox.set("請選擇日期")
        self.date_cobox.pack(side="left", padx=5)
        self.date_cobox.bind("<<ComboboxSelected>>", self.update_OrderID_options)
        # ================= date  =====================
        date=self.date_county.get()
        print(date)
        # ================= OrderID  =====================
        tk.Label(frame0, text="訂單號碼:", font=font1).pack(side="left", padx=5, pady=5)
        self.OrderID_county = tk.StringVar()
        self.OrderID_cobox = ttk.Combobox(frame0, textvariable=self.OrderID_county,state="readonly",width=10)
        self.OrderID_cobox.set("訂單號碼")
        self.OrderID_cobox.pack(side="left", padx=5)
        self.OrderID_cobox.bind("<<ComboboxSelected>>", self.update_Product_Quantity)  # 更新Product和Quantity選項
        # ================= OrderID  =====================
        # ================= Product  =====================
        tk.Label(frame0, text="訂單料號:", font=font1).pack(side="left", padx=5, pady=5)
        self.Product_county = tk.StringVar()
        self.Product_cobox = ttk.Combobox(
            frame0, textvariable=self.Product_county,state="readonly",width=15)
        self.Product_cobox.set("訂單料號")
        self.Product_cobox.pack(side="left", padx=5)
        # ================= Product  =====================
        # ================= Quantity  =====================        
        tk.Label(frame0, text="訂單數量:", font=font1).pack(side="left", padx=5, pady=5)
        self.Quantity_county = tk.StringVar()
        self.Quantity_cobox = ttk.Combobox(frame0, textvariable=self.Quantity_county,state="readonly",width=8)
        self.Quantity_cobox.set("訂單數量")
        self.Quantity_cobox.pack(side="left", padx=5)
        frame0.pack()
        # ================= Quantity  =====================
        # ================= Factory  =====================
        tk.Label(frame0, text="廠區:", font=font1).pack(side="left", padx=5, pady=5)
        self.Factory_county = tk.StringVar()
        self.Factory_cobox = ttk.Combobox(frame0, textvariable=self.Factory_county,values=self.get_unique_values('Plant'),state="readonly",width=10)
        self.Factory_cobox.set("請選擇廠區")
        self.Factory_cobox.pack(side="left", padx=5)
        self.Factory_cobox.bind("<<ComboboxSelected>>", self.update_workshop_options)
        # ================= Factory  =====================
        # ================= workshop  ====================
        tk.Label(frame0, text="車間:", font=font1).pack(side="left", padx=5, pady=5)
        self.workshop_county = tk.StringVar()
        self.workshop_cobox = ttk.Combobox(frame0, textvariable=self.workshop_county,state="readonly",width=10)
        self.workshop_cobox.set("請選擇車間")
        self.workshop_cobox.pack(side="left", padx=5)
        self.workshop_cobox.bind("<<ComboboxSelected>>", self.update_code_options)
        # ================= workshop  ====================
        # ================= workstation===================
        tk.Label(frame0, text="工站:", font=font1).pack(side="left", padx=5, pady=5)
        self.workstation_county = tk.StringVar()
        self.workstation_cobox = ttk.Combobox(frame0, textvariable=self.workstation_county,state="readonly",width=10)
        self.workstation_cobox.set("請選擇工站")
        self.workstation_cobox.pack(side="left", padx=5)
        # ================= workstation===================
        #=====================製造ID========================================================
        frame2 = ttk.Frame(midFrame)
        tk.Label(frame2, text="製造者ID:", font=font1).pack(side="left", padx=5, pady=5)
        self.manufacturer_id = tk.StringVar()
        self.manufacturer_cobox = ttk.Combobox(frame2, textvariable=self.manufacturer_id,state="readonly",width=15)
        self.manufacturer_cobox.set("請選擇製造者ID")
        self.manufacturer_cobox.bind("<<ComboboxSelected>>", self.update_manufacturer_name)
        self.manufacturer_cobox.pack(side="left", padx=5)
        self.update_manufacturer_options() 
        tk.Label(frame2, text="製造者:", font=font1).pack(side="left", padx=5, pady=5)
        self.manufacturer_name_id = tk.StringVar()  
        self.manufacturer_name_cobox = ttk.Combobox(frame2, textvariable=self.manufacturer_name_id,state="readonly",width=15)
        self.manufacturer_name_cobox.set("請選擇製造者ID") 
        self.manufacturer_name_cobox.pack(side="left", padx=5)
        #=====================製造ID========================================================
        #=====================品保ID========================================================
        tk.Label(frame2, text="品保ID:", font=font1).pack(side="left", padx=5, pady=5)
        self.quality_control_id = tk.StringVar()
        self.quality_control_cobox = ttk.Combobox(frame2, textvariable=self.quality_control_id,state="readonly",width=15)        
        self.quality_control_cobox.set("請選擇品保ID")
        self.quality_control_cobox.bind("<<ComboboxSelected>>", self.update_quality_control_name)
        self.quality_control_cobox.pack(side="left", padx=5)
        self.update_quality_control_options()
        tk.Label(frame2, text="品保:", font=font1).pack(side="left", padx=5, pady=5)
        self.quality_name_id = tk.StringVar()
        self.quality_name_cobox = ttk.Combobox(frame2, textvariable=self.quality_name_id,state="readonly",width=15)
        self.quality_name_cobox.set("請選擇品保ID")
        self.quality_name_cobox.pack(side="left", padx=5)
        #=====================品保ID========================================================
        #=====================組長ID========================================================
        tk.Label(frame2, text="組長ID:", font=font1).pack(side="left", padx=5, pady=5)
        self.team_leader_id = tk.StringVar()
        self.team_leader_cobox = ttk.Combobox(frame2, textvariable=self.team_leader_id,state="readonly",width=15)
        self.team_leader_cobox.set("請選擇組長ID")
        self.team_leader_cobox.bind("<<ComboboxSelected>>", self.update_team_leader_name)
        self.team_leader_cobox.pack(side="left", padx=5)
        self.update_team_leader_options()
        tk.Label(frame2, text="組長:", font=font1).pack(side="left", padx=5, pady=5)
        self.team_name_id = tk.StringVar()
        self.team_name_cobox = ttk.Combobox(frame2, textvariable=self.team_name_id,state="readonly",width=15)
        self.team_name_cobox.set("請選擇組長ID")
        self.team_name_cobox.pack(side="left", padx=5)    
        #=====================組長ID========================================================
        frame2.pack(pady=10)
        midFrame.pack(pady=20)
                # ======= 讀取圖片 =======
        self.img_path = r"C:\Users\user\Documents\GitHub\tivd\pythontvdi\241115\風扇良率判定資訊查詢系統\0_1_5.png"  # 請將此處的路徑替換為圖片的路徑
        self.image = Image.open(self.img_path)  # 打開圖片
        self.photo = ImageTk.PhotoImage(self.image)  # 將PIL圖像轉換為Tkinter兼容格式
        self.image = self.image.resize((400, int(400 * self.image.height / self.image.width)))
        self.photo = ImageTk.PhotoImage(self.image)
        # ======= 顯示圖片 =======
        self.label = Label(self, image=self.photo)  # 在Label中顯示圖片
        self.label.pack(padx=20, pady=20,side="left")
        self.button = tk.Button(self, text="切換圖片並寫入CSV", command=self.change_image_and_write_csv)
        self.button.pack(pady=10)

    def change_image_and_write_csv(self):
        # 開啟文件選擇對話框讓使用者選擇新圖片
        # date=self.date_county.get()# 日期 date  
        # OrderID=self.OrderID_county.get()# 訂單號碼 OrderID  
        # Product=self.Product_county.get()# 訂單料號 Product  
        # Quantity=self.Quantity_county.get()# 訂單數量 Quantity
        # Factory=self.Factory_county.get()# 廠區 Factory  
        # workstation=self.workstation_county.get()# 車間 workshop
        # manufacturer_id=self.manufacturer_id.get()# 製造ID manufacturer
        # manufacturer_name_id=self.manufacturer_name_id.get()# 製造者 manufacturer_name
        # quality_control_id=self.quality_control_id.get()# 品保ID quality_control_id
        # quality_name_id=self.quality_name_id.get()#品保者 quality_name_id
        # team_leader_id=self.team_leader_id.get()#組長ID team_leader_id
        # team_name_id=self.team_name_id.get()#組長 team_name_id

        # print(date,OrderID,Product,Factory,workstation,manufacturer_id,manufacturer_name_id,quality_control_id,quality_name_id,team_leader_id,team_name_id)
        # new_img_path = filedialog.askopenfilename(title="選擇圖片", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        # if new_img_path:
        #     # 更新圖片
        #     self.img_path = new_img_path
        #     self.image = Image.open(self.img_path)
        #     self.photo = ImageTk.PhotoImage(self.image)
        #     self.label.config(image=self.photo)  # 切換顯示的圖片

            # # 將圖片路徑與時間戳等數據寫入CSV
            # self.write_to_csv(self.img_path)
# def data_writer():
    # 收集所有變數的值
        date = self.date_county.get()
        OrderID = self.OrderID_county.get()
        Product = self.Product_county.get()
        Quantity = self.Quantity_county.get()
        Factory = self.Factory_county.get()
        workstation = self.workstation_county.get()
        manufacturer_id = self.manufacturer_id.get()
        manufacturer_name_id = self.manufacturer_name_id.get()
        quality_control_id = self.quality_control_id.get()
        quality_name_id = self.quality_name_id.get()
        team_leader_id = self.team_leader_id.get()
        team_name_id = self.team_name_id.get()

        # 要寫入的資料
        data = [date, OrderID, Product, Quantity, Factory, workstation, manufacturer_id, manufacturer_name_id,
                quality_control_id, quality_name_id, team_leader_id, team_name_id]

        # 檔案名稱（可以自行更換）
        file_name = f'{OrderID}_{date}.csv'

        # 寫入 CSV 檔案
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # 如果是第一行，可以先寫入表頭（欄位名稱），如果檔案已經有資料則跳過
            if file.tell() == 0:  # 檔案是空的，寫入表頭
                writer.writerow(['Date', 'OrderID', 'Product', 'Quantity', 'Factory', 'Workstation', 'ManufacturerID',
                                'ManufacturerNameID', 'QualityControlID', 'QualityNameID', 'TeamLeaderID', 'TeamNameID'])

            # 寫入一行資料
            writer.writerow(data)

    def write_to_csv(self, img_path):
        # 這裡可以自定義要寫入的數據
        data = {
            '圖片路徑': img_path,
            '時間戳': '2024-11-27 15:30:00',  # 這裡可以根據需要自動生成或手動設定時間
            '其他數據': 'Sample Data'
        }
    # ======= 工具方法 =======
    def get_date_values(self, name):
        return self.frame0_data[name].dropna().unique().tolist()

    def update_OrderID_options(self, event):
        selected_date = self.date_county.get()
        if selected_date:
            filtered_OrderID = self.frame0_data[self.frame0_data['Date'] == selected_date]['OrderID'].unique().tolist()
            self.OrderID_cobox['values'] = filtered_OrderID

    def update_Product_Quantity(self, event):
        selected_date = self.date_county.get()  # 取得選擇的日期
        selected_order_id = self.OrderID_county.get()  # 取得選擇的訂單號碼
        
        if selected_date and selected_order_id:
            # 根據 Date 和 OrderID 篩選符合條件的 Product 和 Quantity
            filtered_data = self.frame0_data[
                (self.frame0_data['Date'] == selected_date) & 
                (self.frame0_data['OrderID'] == selected_order_id)
            ]
            
            # 更新訂單料號 (Product) 和 訂單數量 (Quantity) 選項
            products = filtered_data['Product'].unique().tolist()
            quantities = filtered_data['Quantity'].unique().tolist()

            self.Product_cobox['values'] = products
            self.Quantity_cobox['values'] = quantities

            if products:
                self.Product_cobox.set(products[0])  # 預設選擇第一個產品料號
            if quantities:
                self.Quantity_cobox.set(quantities[0])  # 預設選擇第一個訂單數量

    def get_unique_values(self, column_name):
        return self.df[column_name].dropna().unique().tolist()

    def update_workshop_options(self, event):
        selected_plant = self.Factory_county.get()
        if selected_plant:
            filtered_workstations = self.df[self.df['Plant'] == selected_plant]['Workstation Code'].unique().tolist()
            self.workshop_cobox['values'] = filtered_workstations
            self.workshop_cobox.set("請選擇車間")
            self.workstation_cobox.set("請選擇工站")
            self.workstation_cobox['values'] = []

    def update_code_options(self, event):
        selected_plant = self.Factory_county.get()
        selected_workstation = self.workshop_county.get()
        if selected_plant and selected_workstation:
            filtered_codes = self.df[
                (self.df['Plant'] == selected_plant) & 
                (self.df['Workstation Code'] == selected_workstation)
            ]['Code'].unique().tolist()
            self.workstation_cobox['values'] = filtered_codes
            self.workstation_cobox.set("請選擇工站")
    def update_manufacturer_options(self):# 假設此方法會更新製造者ID選項
        manufacturer_ids = self.data[self.data['權限代號'] == 1]['ID'].unique().tolist()# 更新製造者ID選項
        self.manufacturer_cobox['values'] = manufacturer_ids# 預設顯示文字
        self.manufacturer_cobox.set("請選擇製造者ID")
    def update_quality_control_options(self):# 假設此方法會更新品保ID選項
        quality_control_ids = self.data[self.data['權限代號'] == 3]['ID'].unique().tolist()# 更新品保ID選項
        self.quality_control_cobox['values'] = quality_control_ids# 預設顯示文字
        self.quality_control_cobox.set("請選擇品保ID")
    def update_team_leader_options(self):# 假設此方法會更新組長ID選項
        team_leader_ids = self.data[self.data['權限代號'] == 2]['ID'].unique().tolist()# 更新組長ID選項
        self.team_leader_cobox['values'] = team_leader_ids# 預設顯示文字
        self.team_leader_cobox.set("請選擇組長ID")
    def update_manufacturer_name(self, event):
        selected_id = self.manufacturer_id.get()  # 取得選擇的製造者 ID
        if selected_id:# 根據選擇的 ID 查詢對應的姓名
            filtered_name = self.data[self.data['ID'] == selected_id]['姓名'].tolist()
            if filtered_name:
                self.manufacturer_name_cobox.set(filtered_name[0])  # 設定對應的姓名
            else:
                self.manufacturer_name_cobox.set("未找到對應姓名")
    def update_quality_control_name(self, event):
        selected_id = self.quality_control_id.get()  # 取得選擇的品保 ID
        if selected_id:# 根據選擇的 ID 查詢對應的姓名
            filtered_name = self.data[self.data['ID'] == selected_id]['姓名'].tolist()
            if filtered_name:
                self.quality_name_cobox.set(filtered_name[0])  # 設定對應的姓名
            else:
                self.quality_name_cobox.set("未找到對應姓名")
    def update_team_leader_name(self, event):
        selected_id = self.team_leader_id.get()  # 取得選擇的組長 ID
        if selected_id:# 根據選擇的 ID 查詢對應的姓名
            filtered_name = self.data[self.data['ID'] == selected_id]['姓名'].tolist()
            if filtered_name:
                self.team_name_cobox.set(filtered_name[0])  # 設定對應的姓名
            else:
                self.team_name_cobox.set("未找到對應姓名")


if __name__ == "__main__":
    window = Window()
    window.mainloop()