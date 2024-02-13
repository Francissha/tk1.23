from tkinter import*
root=Tk()
root.title('Bandaman')
root.geometry('500x500')

def open():
    mylabel=Label(root, text=click.get())
    mylabel.grid(row=2, column=2, padx=10, pady=10, ipadx=30)
    

options=[
    'iPhone XR',
    'iPhone X',
    'iPhone SE',
    'iPhone X MAX',
    'iPhone Pixel'  
]

clicked=StringVar()
clicked.set(options[0])    

drop=OptionMenu(root, clicked, *options)
drop.grid(row=0, column=1, padx=10, pady=10)

mybuttton=Button(root, text='SUBMIT',  command=open)
mybuttton.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()