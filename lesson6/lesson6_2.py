import datasource
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
sitename = datasource.get_sitenames()
print(sitename)
class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
        #==============style===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #============end style===============
        
        #==============top Frame===============

        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='空氣品質AQI(歷史資料)',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        
        #==============end topFrame===============

        #==============bottomFrame===============
        bottomFrame = ttk.Frame(self)
        sitename = datasource.get_sitenames()
        self.selected_site = tk.StringVar()
        sitename_cb = ttk.Combobox(bottomFrame,textvariable=self.selected_site,state='readonly',values=sitename)
        # sitename_cb.configurestate='readonly')
        self.selected_site.set('請選擇站點')
        sitename_cb.pack()

        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============
    
    def agreement_changed(self):
        showinfo(
            title='Agreement',
            message= self.agreement.get()

        )
    
    
        

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()