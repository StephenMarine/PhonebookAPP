import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Define a contact class
class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Define the Phonebook class
class Phonebook:
    def __init__(self):
        self.contacts = []

    def insert_contact(self, name, phone, email=""):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)

    def search_contact(self, query):
        return [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]

    def delete_contact(self, query):
        self.contacts = [contact for contact in self.contacts if query.lower() not in contact.name.lower() and query not in contact.phone]

    def update_contact(self, old_query, new_name, new_phone, new_email=""):
        for contact in self.contacts:
            if old_query.lower() in contact.name.lower() or old_query in contact.phone:
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                return True
        return False

    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name)

    def display_contacts(self):
        return "\n".join([str(contact) for contact in self.contacts])

# GUI application with styling and colors
class PhonebookApp:
    def __init__(self, root):
        self.phonebook = Phonebook()
        self.root = root
        self.root.title("Phonebook Application")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")  # Dark blue-gray background color

        # Style definitions
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", background="#2c3e50", font=("Arial", 14), foreground="white")

        # Header Label
        self.label = tk.Label(root, text="Phonebook Application", font=("Arial", 18), bg="#3498db", fg="white", pady=10)
        self.label.pack(fill=tk.X)

        # Buttons with background colors
        self.btn_insert = tk.Button(root, text="Insert Contact", command=self.insert_contact, bg="#1abc9c", fg="white", font=("Helvetica", 12))
        self.btn_insert.pack(pady=10, ipadx=10, ipady=5)

        self.btn_search = tk.Button(root, text="Search Contact", command=self.search_contact, bg="#e67e22", fg="white", font=("Helvetica", 12))
        self.btn_search.pack(pady=10, ipadx=10, ipady=5)

        self.btn_display = tk.Button(root, text="Display Contacts", command=self.display_contacts, bg="#f39c12", fg="white", font=("Helvetica", 12))
        self.btn_display.pack(pady=10, ipadx=10, ipady=5)

        self.btn_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact, bg="#e74c3c", fg="white", font=("Helvetica", 12))
        self.btn_delete.pack(pady=10, ipadx=10, ipady=5)

        self.btn_update = tk.Button(root, text="Update Contact", command=self.update_contact, bg="#9b59b6", fg="white", font=("Helvetica", 12))
        self.btn_update.pack(pady=10, ipadx=10, ipady=5)

        self.btn_sort = tk.Button(root, text="Sort Contacts", command=self.sort_contacts, bg="#3498db", fg="white", font=("Helvetica", 12))
        self.btn_sort.pack(pady=10, ipadx=10, ipady=5)

        # Adding a footer
        self.footer = tk.Label(root, text="© 2024 Phonebook App", font=("Arial", 10), bg="#2c3e50", fg="white")
        self.footer.pack(side=tk.BOTTOM, pady=20)

    def insert_contact(self):
        name = simpledialog.askstring("Insert Contact", "Enter contact name:")
        phone = simpledialog.askstring("Insert Contact", "Enter contact phone:")
        email = simpledialog.askstring("Insert Contact", "Enter contact email (optional):")
        if name and phone:
            self.phonebook.insert_contact(name, phone, email)
            messagebox.showinfo("Success", f"Contact '{name}' added!")
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required!")

    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter name or phone to search:")
        if query:
            results = self.phonebook.search_contact(query)
            if results:
                messagebox.showinfo("Search Results", "\n".join([str(contact) for contact in results]))
            else:
                messagebox.showinfo("No Results", "No contacts found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a search query.")

    def display_contacts(self):
        contacts = self.phonebook.display_contacts()
        if contacts:
            messagebox.showinfo("All Contacts", contacts)
        else:
            messagebox.showinfo("No Contacts", "No contacts to display.")

    def delete_contact(self):
        query = simpledialog.askstring("Delete Contact", "Enter name or phone to delete:")
        if query:
            self.phonebook.delete_contact(query)
            messagebox.showinfo("Success", f"Contact '{query}' deleted (if it existed).")
        else:
            messagebox.showwarning("Input Error", "Please enter a name or phone number.")

    def update_contact(self):
        old_query = simpledialog.askstring("Update Contact", "Enter name or phone to update:")
        if old_query:
            new_name = simpledialog.askstring("Update Contact", "Enter new name:")
            new_phone = simpledialog.askstring("Update Contact", "Enter new phone:")
            new_email = simpledialog.askstring("Update Contact", "Enter new email (optional):")
            if self.phonebook.update_contact(old_query, new_name, new_phone, new_email):
                messagebox.showinfo("Success", f"Contact '{old_query}' updated!")
            else:
                messagebox.showwarning("Not Found", f"Contact '{old_query}' not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name or phone number.")

    def sort_contacts(self):
        self.phonebook.sort_contacts()
        messagebox.showinfo("Sorted", "Contacts sorted by name!")


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = PhonebookApp(root)
    root.mainloop()
