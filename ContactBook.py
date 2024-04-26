class ContactManager:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts

    def add_contact(self, name, phone_number, email='', address=''):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print("Contact added successfully.")

    def view_contact_list(self):
        print("Contact List:")
        for name, info in self.contacts.items():
            print(f"Name: {name}, Phone: {info['phone_number']}")

    def search_contact(self, search_term):
        print("Search Results:")
        for name, info in self.contacts.items():
            if search_term in name or search_term in info['phone_number']:
                print(f"Name: {name}, Phone: {info['phone_number']}")

    def update_contact(self, name, phone_number, email='', address=''):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

# Sample usage:
contact_manager = ContactManager()
contact_manager.add_contact("SHIVANI CHAUDHARY", "8104839631", "shiva@example.com", "123 Main St")
contact_manager.add_contact("AKASH CHAUDHARY", "9136543410", "aka@example.com", "456 Elm St")
contact_manager.view_contact_list()

contact_manager.search_contact("SHIVANI")
contact_manager.search_contact("0987")

contact_manager.update_contact("SHIVANI CHAUDHARY", "8104896360")
contact_manager.delete_contact("SHIVANI CHAUDHARY")

contact_manager.view_contact_list()

# Additional examples:

# Adding a new contact
contact_manager.add_contact("AKASH CHAUDHARY", "9876543210")

# Viewing the updated contact list
contact_manager.view_contact_list()

# Searching for a contact by phone number
contact_manager.search_contact("9876")

# Updating a contact's email address
contact_manager.update_contact("VIKAS CHAUDHARY ", "9876543210", email="akash.chaudhary@example.com")

# Deleting a contact
contact_manager.delete_contact("AKASH CHAUDHARY")

# Viewing the final contact list
contact_manager.view_contact_list()
