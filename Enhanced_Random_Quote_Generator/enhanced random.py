import tkinter as tk
from tkinter import messagebox
import json
import os
import random

DATA_FILE = "quotes_data.json"

# Load quotes
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        quotes = json.load(f)
else:
    quotes = [
        {"quote": "Believe you can and you're halfway there.", "category": "Motivation"},
        {"quote": "Do what you can with what you have.", "category": "Motivation"},
        {"quote": "Be yourself; everyone else is already taken.", "category": "Life"}
    ]

favorites = []

def save_quotes():
    with open(DATA_FILE, "w") as f:
        json.dump(quotes, f, indent=4)

def show_quote():
    category = var_category.get()
    filtered = [q for q in quotes if q["category"] == category] if category != "All" else quotes
    if filtered:
        selected = random.choice(filtered)
        label_quote.config(text=selected["quote"])
    else:
        label_quote.config(text="No quotes in this category!")

def add_quote():
    text = entry_quote.get()
    category = var_new_category.get()
    if not text:
        messagebox.showwarning("Warning", "Enter a quote")
        return
    if not category:
        category = "Misc"
    quotes.append({"quote": text, "category": category})
    entry_quote.delete(0, tk.END)
    save_quotes()
    update_categories()
    messagebox.showinfo("Success", "Quote added!")

def add_favorite():
    if label_quote.cget("text"):
        favorites.append(label_quote.cget("text"))
        messagebox.showinfo("Favorite", "Quote added to favorites!")

def view_favorites():
    if favorites:
        fav_text = "\n".join(favorites)
        messagebox.showinfo("Favorites", fav_text)
    else:
        messagebox.showinfo("Favorites", "No favorite quotes yet.")

def update_categories():
    categories = set([q["category"] for q in quotes])
    categories = ["All"] + sorted(categories)
    menu_category["menu"].delete(0, "end")
    for c in categories:
        menu_category["menu"].add_command(label=c, command=tk._setit(var_category, c))

# GUI
root = tk.Tk()
root.title("Enhanced Random Quote Generator")

label_quote = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
label_quote.pack(pady=20)

# Show quote by category
var_category = tk.StringVar(value="All")
menu_category = tk.OptionMenu(root, var_category, "All")
menu_category.pack(pady=5)
tk.Button(root, text="Show Quote", command=show_quote).pack(pady=5)

# Add new quote
entry_quote = tk.Entry(root, width=50)
entry_quote.pack(pady=5)
var_new_category = tk.StringVar()
entry_category_label = tk.Label(root, text="Category:")
entry_category_label.pack()
tk.Entry(root, textvariable=var_new_category).pack(pady=5)
tk.Button(root, text="Add Quote", command=add_quote).pack(pady=5)

# Favorites
tk.Button(root, text="Add to Favorites", command=add_favorite).pack(pady=5)
tk.Button(root, text="View Favorites", command=view_favorites).pack(pady=5)

update_categories()
root.mainloop()
