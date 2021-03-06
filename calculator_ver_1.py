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

def clrbut():
    textin.set("")


def button_location():

    B_0 = Button(top, command=lambda:clickbut(0), text ="0", width=int(17.5), height=3, fg="red")
    B_0.place(x=17, y=432)

    B_1 = Button(top, command=lambda:clickbut(1), text = "1", width=8, height=3, fg = "red")
    B_1.place(x=17, y=352)

    B_2 = Button(top, command=lambda:clickbut(2), text = "2", width=8, height=3, fg = "red")
    B_2.place(x=100, y=352)

    B_3 = Button(top, command=lambda: clickbut(3), text="3", width=8, height=3, fg="red")
    B_3.place(x=182, y=352)

    B_4 = Button(top, command=lambda: clickbut(4), text="4", width=8, height=3, fg="red")
    B_4.place(x=17, y=272)

    B_5 = Button(top, command=lambda: clickbut(5), text="5", width=8, height=3, fg="red")
    B_5.place(x=100, y=272)

    B_6 = Button(top, command=lambda: clickbut(6), text="6", width=8, height=3, fg="red")
    B_6.place(x=182, y=272)

    B_7 = Button(top, command=lambda: clickbut(7), text="7", width=8, height=3, fg="red")
    B_7.place(x=17, y=192)

    B_8 = Button(top, command=lambda: clickbut(8), text="8", width=8, height=3, fg="red")
    B_8.place(x=100, y=192)

    B_9 = Button(top, command=lambda: clickbut(9), text="9", width=8, height=3, fg="red")
    B_9.place(x=182, y=192)

    B_10 = Button(top, command=lambda: clickbut(","), text=",", width=8, height=3, fg="blue")
    B_10.place(x=182, y=432)

    B_11 = Button(top, command=lambda: clickbut("*"), text="x", width=8, height=3, fg="blue")
    B_11.place(x=264, y=116)

    B_12 = Button(top, command=lambda: clickbut("/"), text="÷", width=8, height=3, fg="blue")
    B_12.place(x=182, y=116)

    B_13 = Button(top, command=lambda: clickbut("+"), text="+", width=8, height=3, fg="blue")
    B_13.place(x=264, y=272)

    B_14 = Button(top, command=lambda: clickbut("-"), text="-", width=8, height=3, fg="blue")
    B_14.place(x=264, y=192)

    B_15 = Button(top, command=equlbut, text="=", width=8, height=8, fg="blue")
    B_15.place(x=264, y=352)

    B_16 = Button(top, text="Clear (CE)", command=clrbut, width=17, height=3, fg="purple")
    B_16.place(x=17, y=116)


print(button_location())

def tick(my_widget, my_var):
    time_string = time.strftime("%H:%M:%S")
    my_var.set(time_string)
    my_widget.after(10, tick, my_widget, my_var)
    return tick



def rst():
    L1 = Label(top, font=("times", 18, "bold"), text="Result", fg="green")
    L1.place(x=150, y=42)
    E1 = Entry(top, textvar=textin, width=int(34.5), bd=5)
    E1.place(x=18, y=75)
    L2 = Label(top, text="Clock", fg="blue")
    L2.place(x=200, y=2)

    var = StringVar()
    E2 = Entry(top, textvariable=var, width=10, bd=1)
    E2.place(x=250, y=1)
    tick(E2, var)

print(rst())

def dialog():
    my_message = messagebox.showinfo("About calculator" ,"This calculator is made by Piotr Tatarski. \nIt is dedicated to my wife Natalie and my dog named Diesel.")

def my_quest():
    top_2 = Tk()
    top_2.geometry("200x200")

    global var1
    global var2
    Label(top_2, text="Your sex:").grid(row=0, sticky=W)
    var1 = IntVar()
    Checkbutton(top_2, text="male", variable=var1).grid(row=1, sticky=W)
    var2 = IntVar()
    Checkbutton(top_2, text="female", variable=var2).grid(row=2, sticky=W)
    Button(top_2, text='Quit', command=quit).grid(row=3, sticky=W, pady=4)
    Button(top_2, text='Show', command=my_quest).grid(row=4, sticky=W, pady=4)
    print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))


def options():
    menubar = Menu(top)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=top.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Delete", command=clrbut)
    menubar.add_cascade(label="Edit", menu=editmenu)


    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=dialog)
    helpmenu.add_checkbutton(label="Questionnaire", command=my_quest)
    menubar.add_cascade(label="Help", menu=helpmenu)

    top.config(menu=menubar)

print(options())


top.configure(bg="LightBlue")

top.mainloop()
