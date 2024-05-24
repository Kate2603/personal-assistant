
class Contact:
    def __init__(self, name, phone, address=None, email=None, birthday=None):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}: Phone: {self.phone}, Address: {self.address}, Email: {self.email}, Birthday: {self.birthday}"

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, address=None, email=None, birthday=None):
        self.contacts[name] = Contact(name, phone, address, email, birthday)
        return f"Contact {name} added."
