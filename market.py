from tkinter import *
root=Tk()

root.title('bandaman')
root.geometry("400x400")

PRODUCT=[
    
    ('Microsoft Surface','Microsoft Surface'),
    ('Asus Zenfone','Asus Zenfone'),
    ('Google Pixel','Google Pixel'),
    ('Hp Omen','Hp Omen'),
    ('Apple iphone 14','Apple iphone 14')
       
]
choice = StringVar()
choice.set('Microsoft Surface')

for text,mode in PRODUCT:
     Radiobutton(root, text=text, variable=choice, value=mode).pack(anchor='w')
    
def clicked(value):
    mylabel=Label(root, text=value)
    mylabel.pack()
    
mybutton=Button(root, text='BUY NOW!!', bg='white', fg='green', command=lambda :clicked(choice.get()))
mybutton.pack()

root.mainloop()    
         