import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Define the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Define button functions
def click_button(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(item))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create buttons
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=10, height=3, command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, width=10, height=3, command=clear_entry)
    else:
        btn = tk.Button(root, text=button, width=10, height=3, command=lambda x=button: click_button(x))
    
    btn.grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
# RUnthe app
## Run the application
# Run the application
# Run the application
# Run the application
