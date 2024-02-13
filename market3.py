from tkinter import *
root=Tk()

root.title('bandaman')
root.geometry('500x500')

def function():
    label1=Label(frame,text='Hello user!', fg='blue')
    label1.grid(row=10, column=10)
    
frame=LabelFrame(root, text='Its a frame', padx=100, pady=100)
frame.grid(padx=20, pady=20)

b1=Button(frame, text='CLICK ME', command=function)
b1.grid(row=0, column=1)

b2=Button(frame,text='EXIT', command=root.quit())
b2.grid(row=0, column=3)

root.mainloop()

    
