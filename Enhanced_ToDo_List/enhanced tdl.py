import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "tasks_data.json"

# Load existing tasks
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

# Functions
def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    name = entry_task.get()
    priority = var_priority.get()
    if name:
        tasks.append({"task": name, "priority": priority, "done": False})
        update_task_list()
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task")

def mark_done():
    try:
        index = listbox_tasks.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_task_list()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "✗"
        listbox_tasks.insert(tk.END, f"[{status}] ({t['priority']}) {t['task']}")

# GUI
root = tk.Tk()
root.title("Enhanced To-Do List")

entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)

var_priority = tk.StringVar(value="Medium")
tk.Label(root, text="Priority:").pack()
tk.OptionMenu(root, var_priority, "High", "Medium", "Low").pack()

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Mark Done/Undone", command=mark_done).pack(pady=5)

listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.pack(pady=10)

update_task_list()
root.mainloop()
