from tkinter import *
from tkinter import messagebox

cal = Tk()
cal.title("Simple Calculator")

def add():
    try:
        a = int(txt1.get())
        b = int(txt2.get())
        result = a + b
        print(result)
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def sub():
    try:
        a = int(txt1.get())
        b = int(txt2.get())
        result = a - b
        print(result)
        messagebox.showinfo("Result", f"The difference is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def multi():
    try:
        a = int(txt1.get())
        b = int(txt2.get())
        result = a * b
        print(result)
        messagebox.showinfo("Result", f"The product is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def div():
    try:
        a = int(txt1.get())
        b = int(txt2.get())
        if b == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero")
        else:
            result = a / b
            print(result)
            messagebox.showinfo("Result", f"The quotient is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

lbl1 = Label(cal, text="First Number", font=("Arial", 20))
lbl2 = Label(cal, text="Second Number", font=("Arial", 20))

btn1 = Button(cal, text="Addition", height=2, width=15, command=add)
btn2 = Button(cal, text="Subtraction", height=2, width=15, command=sub)
btn3 = Button(cal, text="Multiplication", height=2, width=15, command=multi)
btn4 = Button(cal, text="Division", height=2, width=15, command=div)

txt1 = Entry(cal, font=("Arial", 20), width=10)
txt2 = Entry(cal, font=("Arial", 20), width=10)

lbl1.pack(pady=10)
txt1.pack(pady=10)
lbl2.pack(pady=10)
txt2.pack(pady=10)
btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)

cal.mainloop()
