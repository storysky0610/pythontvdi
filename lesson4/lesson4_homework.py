from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('聽說用字體大小做')
        style = ttk.Style(self)

        topFrame = ttk.Frame(self,borderwidth=3,relief='groove')

        topFrame.pack(padx=10,pady=(10,0),expand=True,fill='x')

        btn1 = ttk.Button(topFrame,text="按鈕1")

        btn1.pack(side='left',expand=True,fill='x',padx=10)

        btn2 = ttk.Button(topFrame,text="按鈕2")

        btn2.pack(side='left',expand=True,fill='x')

        btn3 = ttk.Button(topFrame,text="按鈕3")

        btn3.pack(side='left',expand=True,fill='x',padx=10)

        ###############################################################
        style.configure('Main1.TButton',font=('Aeial',45))
        style.configure('Main2.TButton',font=('Aeial',26))
        style.configure('Main3.TButton',font=('Aeial',25))
        style.configure('Main4.TButton',font=('Aeial',38))
        style.configure('Main5.TButton',font=('Aeial',16))
        style.configure('Main6.TButton',font=('Aeial',38))
        style.configure('Main7.TButton',font=('Aeial',33))
        style.configure('Main8.TButton',font=('Aeial',30))
        style.configure('Main9.TButton',font=('Aeial',34))

        bottomFrame1 = ttk.Frame(self,borderwidth=3,relief='groove')

        bottomFrame1.pack(padx=10,pady=10,side='left')
        x=3
        
        btn4 = ttk.Button(bottomFrame1,text="4",style = 'Main1.TButton',width=x)

        btn4.pack(fill='x',padx=10,pady=(12,0))

        btn5 = ttk.Button(bottomFrame1,text="5",style = 'Main2.TButton',width=x)

        btn5.pack(fill='x',padx=10,pady=(6,0))

        btn6 = ttk.Button(bottomFrame1,text="6",style = 'Main3.TButton',width=x)

        btn6.pack(fill='x',padx=10,pady=(8,12))

        bottomFrame2 = ttk.Frame(self,borderwidth=3,relief='groove')

        bottomFrame2.pack(padx=10,pady=10,side='left')

        btn7 = ttk.Button(bottomFrame2,text="7",style = 'Main4.TButton',width=x)

        btn7.pack(fill='x',padx=10,pady=(12,0))

        btn8 = ttk.Button(bottomFrame2,text="8",style = 'Main5.TButton',width=x)

        btn8.pack(fill='x',padx=10,pady=(14,0))

        btn9 = ttk.Button(bottomFrame2,text="9",style = 'Main6.TButton',width=x)

        btn9.pack(fill='x',padx=10,pady=(8,12))


        bottomFrame3 = ttk.Frame(self,borderwidth=3,relief='groove')

        bottomFrame3.pack(padx=10,pady=10)

        btn10 = ttk.Button(bottomFrame3,text="10",style = 'Main7.TButton',width=x)

        btn10.pack(fill='x',padx=10,pady=(0,0))

        btn11 = ttk.Button(bottomFrame3,text="11",style = 'Main8.TButton',width=x)

        btn11.pack(fill='x',padx=10,pady=(8,0))

        btn12 = ttk.Button(bottomFrame3,text="12",style = 'Main9.TButton',width=x)

        btn12.pack(fill='x',padx=10,pady=(16,12))
def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':

    main()