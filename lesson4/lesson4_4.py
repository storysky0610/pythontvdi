import tkinter as tk
from tkinter import ttk
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('使用ttk的套件')#全域變數
        self.geometry('400x300')
        message = ttk.Label(self,text="使用ttk的Label")#區域變數
        message.pack()
def main():
    window = Window()
    window.mainloop()
if __name__ == "__main__":
    main()
