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
