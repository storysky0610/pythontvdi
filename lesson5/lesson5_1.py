from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

class Window (ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #====== ST style ==============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #====== End style==============
        #====== ST TopFrame ==============
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame, text='個人資料輸入:', style='TopFrame.TLabel').pack() 
        topFrame.pack(padx=20,pady=20)
        #====== End TopFrame==============
        #====== ST buttomFrame ==============
        bottomFrame = ttk.Frame(self)
        bottomFrame.columnconfigure(index=0,weight=1)
        bottomFrame.columnconfigure(index=1,weight=9)

        ttk.Label(bottomFrame,text='UserName:').grid(column=0,row=0,sticky='E')#行列
        self.username = tk.StringVar()
        ttk.Entry(bottomFrame,textvariable=self.username).grid(column=1,row=0,pady=10,padx=10)

        ttk.Label(bottomFrame,text='Passwork:').grid(column=0,row=1,sticky='E')#行列
        self.passwork = tk.StringVar()
        ttk.Entry(bottomFrame,textvariable=self.passwork,show='*').grid(column=1,row=1,pady=10,padx=10)
        #=================row2============
        radioFrame = ttk.Frame(bottomFrame).grid(column=1,row=2)
        sizes = (('small','S'),('Medium','M'),('Large','L'),('Extra Large','XL'),('Extra Extra Large','XXL'))
        label = ttk.Label(radioFrame,text="what's tour t-shirt size?")
        #=================end row2========
        cancel_btn = ttk.Button(bottomFrame,text="取消",command=self.cancel_click)
        cancel_btn.grid(column=0,row=3,pady=10,padx=10)


        ok_btn = ttk.Button(bottomFrame,text='確認',command=self.ok_click)
        ok_btn.grid(column=1,row=3,pady=10,padx=10,sticky='E')

        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20))
        #====== End buttomFrame ==============
    def cancel_click(self):
        self.username.set("")
        self.passwork.set("")
    def ok_click(self):
        username=self.username.get()
        passwork=self.passwork.get()
        showinfo(title="使用者輸入:",message=f'"使用者名稱:"{username}\n使用者密碼:{passwork}')
def main():
    window = Window(theme="arc")
    # window.username.set("這裡放姓名")
    # window.passwork.set('這裡打password')
    window.mainloop()
    
if __name__ == '__main__':
    main()
