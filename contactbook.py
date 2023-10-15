import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contacts
contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        address_entry.delete(0, 'end')
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

def view_contacts():
    contact_list.delete(0, 'end')
    for name, info in contacts.items():
        contact_list.insert('end', f"{name}: {info['Phone']}")

def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, 'end')
    
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['Phone']:
            contact_list.insert('end', f"{name}: {info['Phone']}")

def update_contact():
    selected = contact_list.curselection()
    if selected:
        selected_contact = contact_list.get(selected)
        name, _ = selected_contact.split(":")
        name = name.strip()
        new_phone = new_phone_entry.get()
        new_email = new_email_entry.get()
        new_address = new_address_entry.get()
        
        if name in contacts:
            contacts[name]['Phone'] = new_phone
            contacts[name]['Email'] = new_email
            contacts[name]['Address'] = new_address
            view_contacts()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")
    else:
        messagebox.showerror("Error", "Select a contact to update.")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        selected_contact = contact_list.get(selected)
        name, _ = selected_contact.split(":")
        name = name.strip()
        
        if name in contacts:
            del contacts[name]
            view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")
    else:
        messagebox.showerror("Error", "Select a contact to delete.")

# Create the main application window
app = tk.Tk()
app.title("Contact Manager")

# Create input fields and buttons
name_label = tk.Label(app, text="Name:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

phone_label = tk.Label(app, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(app)
phone_entry.pack()

email_label = tk.Label(app, text="Email:")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

address_label = tk.Label(app, text="Address:")
address_label.pack()
address_entry = tk.Entry(app)
address_entry.pack()

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(app, text="Search:")
search_label.pack()
search_entry = tk.Entry(app)
search_entry.pack()

search_button = tk.Button(app, text="Search", command=search_contact)
search_button.pack()

contact_list = tk.Listbox(app, selectmode=tk.SINGLE)
contact_list.pack()

view_button = tk.Button(app, text="View Contacts", command=view_contacts)
view_button.pack()

new_phone_label = tk.Label(app, text="New Phone:")
new_phone_label.pack()
new_phone_entry = tk.Entry(app)
new_phone_entry.pack()

new_email_label = tk.Label(app, text="New Email:")
new_email_label.pack()
new_email_entry = tk.Entry(app)
new_email_entry.pack()

new_address_label = tk.Label(app, text="New Address:")
new_address_label.pack()
new_address_entry = tk.Entry(app)
new_address_entry.pack()

update_button = tk.Button(app, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.pack()

app.mainloop()
