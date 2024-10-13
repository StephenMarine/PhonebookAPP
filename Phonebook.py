import time

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

    # Insert a contact
    def insert_contact(self, name, phone, email=""):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    # Search contact by name or phone
    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone]
        return results

    # Display all contacts
    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    # Delete a contact by name or phone
    def delete_contact(self, query):
        self.contacts = [contact for contact in self.contacts if query not in contact.name and query not in contact.phone]
        print(f"Contact {query} deleted successfully!")

    # Update an existing contact's details
    def update_contact(self, old_query, new_name, new_phone, new_email=""):
        updated = False
        for contact in self.contacts:
            if old_query in contact.name or old_query in contact.phone:
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                updated = True
                print(f"Contact {old_query} updated successfully!")
        if not updated:
            print(f"Contact {old_query} not found.")

    # Sort contacts by name
    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name)
        print("Contacts sorted by name!")

    # Analyze search efficiency (time complexity)
    def analyze_search_efficiency(self, query):
        start_time = time.time()
        results = self.search_contact(query)
        end_time = time.time()
        search_time = end_time - start_time
        print(f"Search took {search_time:.6f} seconds.")
        print(f"Time complexity is O(n) since we are doing a linear search.")
        if results:
            print(f"Found {len(results)} contact(s).")
        else:
            print("No contacts found.")


# Main program logic
def main():
    phonebook = Phonebook()

    while True:
        print("\nPhonebook Application:")
        print("1. Insert Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Sort Contacts")
        print("7. Analyze Search Efficiency")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email (optional): ")
            phonebook.insert_contact(name, phone, email)
        elif choice == "2":
            query = input("Enter name or phone to search: ")
            results = phonebook.search_contact(query)
            if results:
                print("Search Results:")
                for result in results:
                    print(result)
            else:
                print("No contacts found.")
        elif choice == "3":
            print("All Contacts:")
            phonebook.display_contacts()
        elif choice == "4":
            query = input("Enter name or phone to delete: ")
            phonebook.delete_contact(query)
        elif choice == "5":
            old_query = input("Enter name or phone to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email (optional): ")
            phonebook.update_contact(old_query, new_name, new_phone, new_email)
        elif choice == "6":
            phonebook.sort_contacts()
        elif choice == "7":
            query = input("Enter name or phone to search and analyze efficiency: ")
            phonebook.analyze_search_efficiency(query)
        elif choice == "8":
            print("Exiting Phonebook Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
