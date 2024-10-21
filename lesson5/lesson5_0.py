from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):#class裡面一定要有self
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('聽說用字體大小做')
        global globalA
        globalA = 20
        print(globalA)

        style = ttk.Style(self)
        #===================TopFrame==============
        topFrame = ttk.Frame(self,borderwidth=3,relief='groove')        

        self.btn1 = ttk.Button(topFrame,text="按鈕1",command=self.user_click1)

        self.btn1.pack(side='left',expand=True,fill='x',padx=10)

        btn2 = ttk.Button(topFrame,text="按鈕2",command=self.user_click2)

        btn2.pack(side='left',expand=True,fill='x')

        btn3 = ttk.Button(topFrame,text="按鈕3",command=self.user_click3)

        btn3.pack(side='left',expand=True,fill='x',padx=10)

        topFrame.pack(padx=10,pady=(10,0),expand=True,fill='x')
        #===================end TopFrame==============
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
        #===================bottompack==============
        bottomFrame = ttk.Frame(self,borderwidth=3,relief='groove')
         #===================secction1===============
        secction1 = ttk.Frame(self,borderwidth=3,relief='groove')

        secction1.pack(padx=10,pady=10,side='left')
        x=3
        
        btn4 = ttk.Button(secction1,text="4",style = 'Main1.TButton',width=x)
        btn4.bind('<ButtonRelease>',self.btn4_botton_click)

        btn4.pack(fill='x',padx=10,pady=(12,0))

        btn5 = ttk.Button(secction1,text="5",style = 'Main2.TButton',width=x)

        btn5.pack(fill='x',padx=10,pady=(6,0))

        btn6 = ttk.Button(secction1,text="6",style = 'Main3.TButton',width=x)

        btn6.pack(fill='x',padx=10,pady=(8,12))
        #===================end secction1===========
        #===================secction2===============
        secction2 = ttk.Frame(self,borderwidth=3,relief='groove')

        secction2.pack(padx=10,pady=10,side='left')

        btn7 = ttk.Button(secction2,text="7",style = 'Main4.TButton',width=x)

        btn7.pack(fill='x',padx=10,pady=(12,0))

        btn8 = ttk.Button(secction2,text="8",style = 'Main5.TButton',width=x)

        btn8.pack(fill='x',padx=10,pady=(14,0))

        btn9 = ttk.Button(secction2,text="9",style = 'Main6.TButton',width=x)

        btn9.pack(fill='x',padx=10,pady=(8,12))
        #===================end secction1===========
        #===================secction3===============
        secction3 = ttk.Frame(self,borderwidth=3,relief='groove')

        secction3.pack(padx=10,pady=10,side='left')

        btn10 = ttk.Button(secction3,text="10",style = 'Main7.TButton',width=x)

        btn10.pack(fill='x',padx=10,pady=(0,0))

        btn11 = ttk.Button(secction3,text="11",style = 'Main8.TButton',width=x)

        btn11.pack(fill='x',padx=10,pady=(8,0))

        btn12 = ttk.Button(secction3,text="12",style = 'Main9.TButton',width=x)

        btn12.pack(fill='x',padx=10,pady=(16,12))
        #===================end secction3==============
        bottomFrame.pack(padx=10,pady=10)
        #===================end bottompack==============
    def user_click1(self):
        self.btn1.configure(text="被按了")
        print("Hollo!botton1")

    def user_click2(self):
        print("Hollo!botton2")

    def user_click3(self):
        print("Hollo!botton3")

    def btn4_botton_click(self,envnt):
        print(envnt.x)
        print(envnt.y)
        print(envnt.width)
        print(envnt.widget.configure(text='被按了'))
        


def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    globalA = 10
    main()