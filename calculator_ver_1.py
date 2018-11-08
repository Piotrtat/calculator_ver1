from tkinter import *
from tkinter import messagebox
import time

top = Tk()
top.title("Calculator")
top.geometry("350x550")

textin = StringVar()
operator = ""

def clickbut(number):
    print(str(number))
    global operator
    operator = operator + str(number)
    textin.set(operator)

def equlbut():
    global operator
    try:
        print(operator)
        div = str(eval(operator))
    except Exception:
        div = "ERROR"
    textin.set(div)
    operator = ""