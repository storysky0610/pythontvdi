from tkinter import ttk
from ttkthemes import ThemedTk

class Window (ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame, text='個人資料輸入:', style='TopFrame.TLabel').pack() 
        topFrame.pack(padx=20,pady=20)
        


        buttomFrame = ttk.Frame(self)
        buttomFrame.pack()
        
def main():
    window = Window(theme="arc")
    window.mainloop()
    
if __name__ == '__main__':
    main()
