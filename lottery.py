from tkinter import *
from PIL import Image, ImageTk 
from random import randint

root=Tk()
root.title("lottery")
root.geometry("500x500")

def pick():
    lst= [
        
        "p1",
        "p2",
        "p3",
        "p4",
        "p5",
        "p6",
        "p7",
        "p8",
        "p1",
        "p1",
        "p1",
        "p1",
     
    ]
    
    entry_set = set(lst)
    unique = list(entry_set)
    our_num = len((unique) -1)
    rand = randint(0, our_num)
    
winner_label=Label(root, text = unique [rand], font=("Helvetica", 20)).pack(pady=20)
    
poster_label=Label(root, text="RANDOM WINNER", font=("Arial Black", 25)).pack(padx=10, pady=10)
    
btn1=Button(root, text="PICK YOUR NUMBER", command=pick, font=("Arial", 30)).pack(pady=20)    
    
root.mainloop()