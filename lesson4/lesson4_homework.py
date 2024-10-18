from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)

        topFrame = ttk.Frame(self,borderwidth=3,relief='groove')

        topFrame.pack(padx=10,pady=(10,0),expand=True,fill='x')

        btn1 = ttk.Button(topFrame,text="按鈕1")

        btn1.pack(side='left',expand=True,fill='x',padx=10)

        btn2 = ttk.Button(topFrame,text="按鈕2")

        btn2.pack(side='left',expand=True,fill='x')

        btn3 = ttk.Button(topFrame,text="按鈕3")

        btn3.pack(side='left',expand=True,fill='x',padx=10)

        bottomFrame1 = ttk.Frame(self,borderwidth=3,relief='groove')

        bottomFrame1.pack(padx=10,pady=10,side='left')

        btn4 = ttk.Button(bottomFrame1,text="按鈕1")

        btn4.pack(expand=True,fill='x',padx=10)

        btn5 = ttk.Button(bottomFrame1,text="按鈕1")

        btn5.pack(expand=True,fill='x',padx=10,side='left')

        btn6 = ttk.Button(bottomFrame1,text="按鈕1")

        btn6.pack(expand=True,fill='x',padx=10)

        bottomFrame2 = ttk.Frame(self,borderwidth=3,relief='groove')

        bottomFrame2.pack(padx=10,pady=10,side='left')

        btn4 = ttk.Button(bottomFrame2,text="按鈕1")

        btn4.pack(expand=True,fill='x',padx=10)

        btn5 = ttk.Button(bottomFrame2,text="按鈕1")

        btn5.pack(expand=True,fill='x',padx=10)

        btn6 = ttk.Button(bottomFrame2,text="按鈕1")

        btn6.pack(expand=True,fill='x',padx=10)


        bottomFrame3 = ttk.Frame(self,borderwidth=3,relief='groove')

        bottomFrame3.pack(padx=10,pady=10)

        btn4 = ttk.Button(bottomFrame3,text="按鈕1")

        btn4.pack(expand=True,fill='x',padx=10)

        btn5 = ttk.Button(bottomFrame3,text="按鈕1")

        btn5.pack(expand=True,fill='x',padx=10)

        btn6 = ttk.Button(bottomFrame3,text="按鈕1")

        btn6.pack(expand=True,fill='x',padx=10)

def main():
    window = Window(theme="blue")
    window.mainloop()

if __name__ == '__main__':

    main()