from tkinter import * 
import tkinter as tk

win = tk.Tk()

win.title("Calculator")

win.resizable(False, False) 

win.overrideredirect(True)

def button_press(num):
    global exp
    exp= input_text.get()
    exp= str(exp) + str(num)
    input_text.set(exp)


def button_oper(opr):
    global exp
    exp = input_text.get()
    exp= str(exp) + str(opr)
    input_text.set(exp)
    global oper
    oper = opr


def clr_scr():
    global exp
    input_text.set("")
    exp = ""


def equal(event):
    global display
    global oper
    global exp
    exp = input_text.get()
    input_text.set("")
    result = float(eval(exp))
    exp = result
    display.insert(0, result)
    input_text.set(result)


win.configure(bg="#C0C9B7")
labelMain = tk.Label(win, text="CalculatorX", justify="center")

display_frame = Label(win,  relief="groove" , background="#C0C9B7")
display_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


input_text = StringVar()

display = Entry(display_frame, font=('Helvetica', 18, 'bold'), textvariable=input_text, width=22, bg="#A0AD66", bd=0, justify=RIGHT)
display.pack(ipady= 12) 


button_1 = Button(win, padx=30, pady=30, text="1",fg="#ffffff", bg="#21241F", command=lambda: button_press(1))
button_2 = Button(win, padx=30, pady=30, text="2",fg="#ffffff", bg="#21241F", command=lambda: button_press(2))
button_3 = Button(win, padx=30, pady=30, text="3",fg="#ffffff", bg="#21241F", command=lambda: button_press(3))
button_4 = Button(win, padx=30, pady=30, text="4",fg="#ffffff", bg="#21241F", command=lambda: button_press(4))
button_5 = Button(win, padx=30, pady=30, text="5",fg="#ffffff", bg="#21241F", command=lambda: button_press(5))
button_6 = Button(win, padx=30, pady=30, text="6",fg="#ffffff", bg="#21241F", command=lambda: button_press(6))
button_7 = Button(win, padx=30, pady=30, text="7",fg="#ffffff", bg="#21241F", command=lambda: button_press(7))
button_8 = Button(win, padx=30, pady=30, text="8",fg="#ffffff", bg="#21241F", command=lambda: button_press(8))
button_9 = Button(win, padx=30, pady=30, text="9",fg="#ffffff", bg="#21241F", command=lambda: button_press(9))
button_0 = Button(win, padx=70, pady=30, text="0",fg="#ffffff", bg="#21241F", command=lambda: button_press(0))
button_add = Button(win, padx=30, pady=30, text="+",fg="#ffffff", bg="#21241F", command=lambda: button_oper("+"))
button_sub = Button(win, padx=30, pady=30, text="- ",fg="#ffffff", bg="#21241F", command=lambda: button_oper("-"))
button_div = Button(win, padx=30, pady=30, text="/ ",fg="#ffffff", bg="#21241F", command=lambda: button_oper("/"))
button_mul = Button(win, padx=30, pady=30, text="* ",fg="#ffffff", bg="#21241F", command=lambda: button_oper("*"))
button_equal = Button(win, padx=70, pady=30, text="=",fg="#ffffff", bg="#BD5828", command=lambda: equal(""))
button_clear = Button(win, padx=70, pady=30, text="C",fg="#ffffff", bg="#21241F", command=clr_scr)
button_dec = Button(win, padx=30, pady=30, text=" .",fg="#ffffff", bg="#21241F", command=lambda: button_press("."))


button_clear.grid(row=1,column = 1, columnspan=2)
button_dec.grid(row=1, column=3)
button_add.grid(row=1, column=4)

button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)
button_sub.grid(row=2, column=4)

button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)
button_div.grid(row=3, column=4)

button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)
button_mul.grid(row=4, column=4)


button_0.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=5, column = 3, columnspan=2)


win.bind("<Return>", equal)


win.mainloop()