# testing comment
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Bill Management System")
root.geometry("800x600")

# Define labels and entry widgets for item details
item_label = ttk.Label(root, text="Item")
item_label.grid(row=0, column=0, padx=10, pady=10)
item_entry = ttk.Entry(root)
item_entry.grid(row=0, column=1, padx=10, pady=10)

price_label = ttk.Label(root, text="Price")
price_label.grid(row=1, column=0, padx=10, pady=10)
price_entry = ttk.Entry(root)
price_entry.grid(row=1, column=1, padx=10, pady=10)

quantity_label = ttk.Label(root, text="Quantity")
quantity_label.grid(row=2, column=0, padx=10, pady=10)
quantity_entry = ttk.Entry(root)
quantity_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a Treeview to display the bill
bill_tree = ttk.Treeview(root, columns=("Item", "Price", "Quantity", "Total"), show='headings')
bill_tree.heading("Item", text="Item")
bill_tree.heading("Price", text="Price")
bill_tree.heading("Quantity", text="Quantity")
bill_tree.heading("Total", text="Total")
bill_tree.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Define functions for adding items and calculating total
def add_item():
    item = item_entry.get()
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())
    total = price * quantity

    bill_tree.insert('', 'end', values=(item, price, quantity, total))
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def calculate_total():
    total_cost = 0
    for child in bill_tree.get_children():
        total_cost += float(bill_tree.item(child)["values"][3])
    messagebox.showinfo("Total Cost", f"Total Bill Amount: ₹{total_cost}")

# Create buttons for adding items and calculating total
add_button = ttk.Button(root, text="Add Item", command=add_item)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

total_button = ttk.Button(root, text="Calculate Total", command=calculate_total)
total_button.grid(row=5, column=0, columnspan=4, pady=10)

# Run the application
root.mainloop()
