from tkinter import*
from PIL import Image, ImageTk
import matplotlib.pyplot as plt  
import numpy as np

root=Tk()
root.title("pie chart")

root.geometry("500x500")

def pie():
    values=[500, 400, 2500, 2000, 1200]
    labels=["internet", "power","rent","food", "others"]
    plt.pie(values, labels ,radius=3.5)
    plt.axis("equal")
    plt.show()
    

b1=Button(root, text="click for result", command="pie").pack()

root.mainloop()