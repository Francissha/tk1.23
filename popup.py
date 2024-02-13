from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("message box")
root.geometry("500x500")

def message():
    messagebox.showinfo("CALL ME") 

b1=Button(root, text="CLICK ME", command=message)
b1.pack()

root.mainloop()