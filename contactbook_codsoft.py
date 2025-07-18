import tkinter as tk
from tkinter import messagebox

contact_list = []

def add_contact():
    name = name_input.get()
    phone = phone_input.get()
    email = email_input.get()
    address = address_input.get()
    
    if name and phone:
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contact_list.append(contact)
        show_all_contacts()
        clear_fields()
    else:
        messagebox.showwarning("warning", "Name and phone are required.")
        
def show_all_contacts():
    contact_display.delete(0, tk.END)
    for entry in contact_list:
        contact_display.insert(tk.END, f"{entry['name']} - {entry['phone']}")
        
def find_contact():
    word = search_input.get()
    contact_display.delete(0, tk.END)
    for entry in contact_list:
        if word.lower() in entry['name'].lower() or word in entry['phone']:
            contact_display.insert(tk.END, f"{entry['name']} - {entry['phone']}")
def remove_contact():
    selected = contact_display.curselection()
    if selected:
        index = selected[0]
        contact_list.pop(index)
        show_all_contacts()
def update_contact():
    selected = contact_display.curselection()
    if selected:
        index = selected[0]
        name = name_input.get()
        phone = phone_input.get()
        email = email_input.get()
        address = address_input.get()
        
        if name and phone:
            contact_list[index] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            
            show_all_contacts()
            clear_fields()
        else:
            messagebox.showerror("Error", "Name and Phone cannot be empty.")
def fill_from(event):
    selected = contact_display.curselection()
    if selected:
        index = selected[0]
        chosen = contact_list[index]
        name_input.delete(0, tk.END)
        name_input.insert(0, chosen['name'])
        phone_input.delete(0, tk.END)
        phone_input.insert(0, chosen['phone'])
        email_input.delete(0, tk.END)
        email_input.insert(0, chosen['email'])
        address_input.delete(0, tk.END)
        address_input.insert(0, chosen['address'])
        
        
def clear_fields():
    name_input.delete(0,tk.END)
    phone_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    address_input.delete(0, tk.END)
    search_input.delete(0,tk.END)
    
#setup gui
window = tk.Tk()
window.title("Contact Book")
window.geometry("500x500")
window.resizable(False, False)

#inputs and labels

tk.Label(window, text= "Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_input = tk.Entry(window, width=30)
name_input.grid(row=0, column=1)

tk.Label(window, text="Phone").grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_input = tk.Entry(window, width=30)
phone_input.grid(row=1, column=1)

tk.Label(window, text="Email").grid(row=2, column=0, padx=10,pady=5, sticky="w")
email_input = tk.Entry(window, width=30)
email_input.grid(row=2, column=1)

tk.Label(window, text="Address").grid(row=3, column=0, padx=10, pady=5, sticky="w")
address_input = tk.Entry(window, width=30)
address_input.grid(row=3, column=1)

#buttons
tk.Button(window, text="Add Contact", command=add_contact).grid(row=4, column=0, pady=10)
tk.Button(window, text="Update Contact", command= update_contact).grid(row=4, column=1, pady=10)
tk.Button(window, text="Delete Contact", command=remove_contact).grid(row=5, column=0, pady=5)
tk.Button(window, text="clear Fields", command =clear_fields).grid(row=5, column=1, pady=5)

#search box
tk.Label(window, text="search").grid(row=6, column=0, pady=5)
search_input = tk.Entry(window,  width=30)
search_input.grid(row=6, column=1)
tk.Button(window, text="Search", command= find_contact).grid(row=7, column=1, sticky="e", pady=5)

#contact list
contact_display = tk.Listbox(window, width=60, height=10)
contact_display.grid(row=8, column=0, columnspan= 2, padx=10, pady=10)
contact_display.bind("<<ListboxSelect>>", fill_from)

window.mainloop()