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
        sitename_cb.bind('<<ComboboxSelected>>', self.sitename_selected)
        sitename_cb.pack(side='left',expand=True,anchor='n')

        columns = ('data','county','aqi','pm25','status','lat','lon')

        self.tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')

        # define headings
        self.tree.heading('data', text='日期')
        self.tree.heading('county', text='縣市')
        self.tree.heading('aqi', text='AQI')
        self.tree.heading('pm25', text='PM25')
        self.tree.heading('status', text='status')
        self.tree.heading('lat', text='緯度')
        self.tree.heading('lon', text='經度')
        self.tree.column('data', width=150,anchor='center')
        self.tree.column('county', width=80,anchor='center')
        self.tree.column('aqi', width=50,anchor='center')
        self.tree.column('pm25', width=50,anchor='center')
        self.tree.column('status', width=50,anchor='center')
        self.tree.column('lat', width=100,anchor='center')
        self.tree.column('lon', width=100,anchor='center')
        self.tree.insert("",'end',values=('2024-10-28 9:00','屏東',17,6.5,'良好',22.260899,120.651472))

        # # generate sample data
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # # add data to the treeview
        # for contact in contacts:
        #     tree.insert('', tk.END, values=contact)
        self.tree.pack(side='right')
        #,expand=True,anchor='n'
        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============
    
    def sitename_selected(self,event):
        selected = self.selected_site.get()
        selected_data = datasource.get_selected_data(selected)
        for record in selected_data:
            self.tree.insert('','end',values=record)
        
    
    
        

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()