
import json
import os

data_file = "contacts.json"

# Load existing contacts
if os.path.exists(data_file):
    with open(data_file, "r") as f:
        contacts = json.load(f)
else:
    contacts = []

def save_contacts():
    with open(data_file, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts yet.\n")
        return
    for i, c in enumerate(contacts):
        print(f"{i+1}. {c['name']} - {c['phone']} - {c['email']}")
    print()

def search_contact():
    term = input("Search by name: ").lower()
    found = [c for c in contacts if term in c['name'].lower()]
    if found:
        for c in found:
            print(f"{c['name']} - {c['phone']} - {c['email']}")
    else:
        print("No contacts found.")
    print()

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts()
            print(f"Deleted contact: {removed['name']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Invalid input.\n")

# Main menu
while True:
    print("=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")
