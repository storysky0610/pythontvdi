import tkinter as tk
def main():
    root = tk.Tk()
    print(type(root))
    root.title('這是我的第一個視窗')
    root.geometry('800x300')
    message = tk.Label(root,text="Hollo!這是我的第一個視窗")
    message.pack()#放進去
    root.mainloop()


if __name__ == '__main__':
    main()