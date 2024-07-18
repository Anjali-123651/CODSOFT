import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.config(bg="pink")

# Create and place widgets
label1 = tk.Label(root, text="Enter number 1:", bg="pink")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter number 2:", bg="pink")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

operation_label = tk.Label(root, text="Choose operation:", bg="pink")
operation_label.grid(row=2, column=0, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_var.set("+")  # default value

operations_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operations_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ", bg="pink")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
