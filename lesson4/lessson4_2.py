import tkinter as tk

class window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('這是我的第一個視窗')
        self.geometry('800x300')
        message = tk.Label(self,text="Hollo!這是我的第一個視窗")
        message.pack()#放進去


def main():
    window1 = window()
    window1.mainloop()


if __name__ == '__main__':
    main()