class ContactList():
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_to_add):
        self.contacts.append(contact_to_add)

    def display_contacts(self):
        for c in self.contacts:
            print(c)