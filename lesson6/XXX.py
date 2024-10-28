import datasource
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

# 获取站点名称
sitename = datasource.get_sitenames()
print(sitename)

# 确保将提示信息添加到站点名称列表
sitename = ['請選擇站點'] + sitename

class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
        
        # ==============样式===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel', font=('Helvetica', 20))
        # =============样式结束===============
        
        # ==============顶部框架===============
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame, text='空氣品質AQI(歷史資料)', style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20, pady=20)
        # ==============顶部框架结束===============
        
        # ==============底部框架===============
        bottomFrame = ttk.Frame(self)
        selected_site = tk.StringVar()  # 变量用于存储下拉框选项
        
        # 创建下拉框，确保第一个选项是提示信息
        sitename_cb = ttk.Combobox(bottomFrame, textvariable=selected_site)
        sitename_cb.configure(values=sitename, state='readonly')
        sitename_cb.current(0)  # 设定默认选项为第一个
        sitename_cb.pack(pady=10)  # 添加一些内边距以便更好地显示

        bottomFrame.pack(expand=True, fill='x', padx=20, pady=(0, 20), ipadx=10, ipady=10)
        # ==============底部框架结束===============

    def agreement_changed(self):
        showinfo(
            title='协议',
            message=self.agreement.get()
        )

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
