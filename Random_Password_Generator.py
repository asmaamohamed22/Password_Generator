import string
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def low():
    entry.delete(0,END)
    
    lenght = var1.get()
    lower = "abcdefghijklmnoprstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz1234567890 !@#$%^&*()~"
    password = ""
    
    if var.get() == 1:
        for i in range(0,lenght):
            password = password + random.choice(lower)
        return password
    
    elif var.get() == 0:
        for i in range(0,lenght):
            password = password + random.choice(upper)
        return password
    
    elif var.get() == 3:
        for i in range(0,lenght):
            password = password + random.choice(digits)
        return password
    else:
        print("Please Choose an option")
   

def generate():
    password1 = low()
    entry.insert(10,password1)
    
def copyclip():
    random_password = entry.get()
    pyperclip.copy(random_password)
    
root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")
root.geometry("330x250")

Random_password = Label(root,text="Password")
Random_password.place(x=20,y=30)

entry = Entry(root)
entry.place(x=90,y=30)

c_label = Label(root,text="Length")
c_label.place(x=20,y=70)

copy_button = Button(root,text="Copy",command=copyclip)
copy_button.place(x=40,y=180,width=110)

generate_button = Button(root,text="Generate",command=generate)
generate_button.place(x=160,y=180,width=110)

radio_low = Radiobutton(root,text="Low",variable=var,value=1)
radio_low.place(x=50,y=120)

radio_med = Radiobutton(root,text="Medium",variable=var,value=0)
radio_med.place(x=120, y=120)

radio_strong = Radiobutton(root,text="Strong",variable=var,value=3)
radio_strong.place(x=200, y=120)

combo = Combobox(root,textvariable=var1)
combo['values']=(8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=90,y=70)

root.mainloop()
