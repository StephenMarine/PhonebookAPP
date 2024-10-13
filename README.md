# PhonebookAPP
Project Description
The Phonebook Application is a simple desktop-based application that allows users to manage their contacts efficiently. The application provides functionalities to insert, search, display, delete, update, sort contacts, and analyze the efficiency of search operations. It is built using Python and Tkinter for the graphical user interface (GUI), ensuring a user-friendly experience.

Features:
Insert Contact: Add new contacts with name, phone number, and email.
Search Contact: Search for contacts by name or phone number.
Display Contacts: View all saved contacts.
Delete Contact: Remove a contact from the phonebook.
Update Contact: Update the details of an existing contact.
Sort Contacts: Sort contacts alphabetically by name.
Analyze Search Efficiency: Measure and display the efficiency of search operations.
Modules and Functions
1. Contact Class
This class defines the structure for each contact in the phonebook.

Attributes:

name: The contact's name.
phone: The contact's phone number.
email: (Optional) The contact's email address.
Methods:

__init__(self, name, phone, email=""): Initializes a new contact with a name, phone, and optional email.
__str__(self): Returns a formatted string representation of the contact.
2. Phonebook Class
The core functionality of the phonebook is handled by this class, which stores and manages the contact list.

Attributes:
contacts: A list that stores all the Contact objects.
Methods:
insert_contact(self, name, phone, email=""): Adds a new contact to the phonebook.
search_contact(self, query): Searches for a contact by name or phone number.
delete_contact(self, query): Deletes a contact by name or phone number.
update_contact(self, old_query, new_name, new_phone, new_email=""): Updates an existing contact's information.
sort_contacts(self): Sorts the contacts alphabetically by name.
display_contacts(self): Returns a formatted string of all contacts for display.
3. PhonebookApp Class
This class handles the GUI using Tkinter. It creates the buttons, dialog boxes, and other graphical elements that allow users to interact with the phonebook.

Methods:
__init__(self, root): Initializes the GUI components and links them to the Phonebook functions.
insert_contact(self): Opens a dialog to input contact details and inserts them into the phonebook.
search_contact(self): Prompts the user for a search query and displays the results.
display_contacts(self): Shows all contacts stored in the phonebook.
delete_contact(self): Prompts the user for a contact to delete and removes it from the phonebook.
update_contact(self): Prompts the user for contact details to update an existing entry.
sort_contacts(self): Sorts and displays the contacts.
analyze_search_efficiency(self): (Planned feature) Analyzes the time complexity of the search operation.
How to Run the Application
Prerequisites:
Python 3.x must be installed on your machine.
Tkinter (comes pre-installed with Python).
