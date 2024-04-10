import math
import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def square(x):
    return x ** 2

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def submit():
    operation = operation_var.get()
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())

    if operation == "Add":
        result_label.config(text="Result: " + str(add(num1, num2)))
    elif operation == "Subtract":
        result_label.config(text="Result: " + str(subtract(num1, num2)))
    elif operation == "Multiply":
        result_label.config(text="Result: " + str(multiply(num1, num2)))
    elif operation == "Divide":
        result_label.config(text="Result: " + str(divide(num1, num2)))
    elif operation == "Power":
        result_label.config(text="Result: " + str(power(num1, num2)))
    elif operation == "Square":
        result_label.config(text="Result: " + str(square(num1)))

root = tk.Tk()
root.title("Scientific Calculator")

operation_var = tk.StringVar(root)
operation_var.set("Add")

operation_label = tk.Label(root, text="Operation:")
operation_label.grid(row=0, column=0)

operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide", "Power", "Square")
operation_menu.grid(row=0, column=1)

num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=1, column=0)

num1_entry = tk.Entry(root)
num1_entry.grid(row=1, column=1)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=2, column=0)

num2_entry = tk.Entry(root)
num2_entry.grid(row=2, column=1)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
