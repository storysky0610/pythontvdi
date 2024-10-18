import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')#全域變數
        self.geometry('400x300')
        style = ttk.Style(self)

        style.configure('TLabel',font=("Helvetica",11))
        style.configure('Title.TLabel',font=('Helvetiva',30),background='blue',foreground = 'red')
        message = ttk.Label(self,text="使用ttk的Label",style='Title.TLabel')#區域變數
        
        
        self.bg_image = Image.open('lesson4\DvFS3xYUwAAUx0v.jfif')  # 替換成你的圖像路徑
        self.bg_image = self.bg_image.resize((300, 300), Image.LANCZOS)  # 調整圖像大小
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # 創建背景標籤
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)  # 填滿整個窗口
        print(message.winfo_class())
        message.pack()

        style.configure('Main.TButton',font=('Aeial',15))
        btn1 = ttk.Button(self,text="Button Demo",style='Main.TButton')
        btn1.pack(padx=10,pady=10,ipadx=20,ipady=40)

def main():
    window = Window(theme="arc")
    window.mainloop()
if __name__ == "__main__":
    main()
