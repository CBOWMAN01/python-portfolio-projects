import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "budget_data.json"

# Load data if it exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {"income": 0, "expenses": []}

# Functions
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_income():
    try:
        amount = float(entry_amount.get())
        data["income"] += amount
        label_income.config(text=f"Income: ${data['income']:.2f}")
        entry_amount.delete(0, tk.END)
        save_data()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

def add_expense():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get()
        name = entry_name.get()
        if not category: category = "Misc"
        if not name: name = "Expense"
        data["expenses"].append({"name": name, "amount": amount, "category": category})
        update_expense_label()
        entry_amount.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        save_data()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

def update_expense_label():
    total_expenses = sum(e["amount"] for e in data["expenses"])
    label_expense.config(text=f"Expenses: ${total_expenses:.2f}")

def show_report():
    total_expenses = sum(e["amount"] for e in data["expenses"])
    balance = data["income"] - total_expenses
    category_summary = {}
    for e in data["expenses"]:
        category_summary[e["category"]] = category_summary.get(e["category"], 0) + e["amount"]
    
    report_text = f"Income: ${data['income']:.2f}\nExpenses: ${total_expenses:.2f}\nBalance: ${balance:.2f}\n\nBy Category:\n"
    for cat, amt in category_summary.items():
        report_text += f"{cat}: ${amt:.2f}\n"
    
    messagebox.showinfo("Budget Report", report_text)

# GUI
root = tk.Tk()
root.title("Enhanced Budget Tracker")

tk.Label(root, text="Expense Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1)

tk.Label(root, text="Amount:").grid(row=2, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

tk.Button(root, text="Add Income", command=add_income).grid(row=3, column=0)
tk.Button(root, text="Add Expense", command=add_expense).grid(row=3, column=1)
tk.Button(root, text="Show Report", command=show_report).grid(row=4, column=0, columnspan=2)

label_income = tk.Label(root, text=f"Income: ${data['income']:.2f}")
label_income.grid(row=5, column=0)
label_expense = tk.Label(root, text="Expenses: $0.00")
label_expense.grid(row=5, column=1)
update_expense_label()

root.mainloop()
