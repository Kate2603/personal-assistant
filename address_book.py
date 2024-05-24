from datetime import datetime, date, timedelta

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


    def add_birthday(self, name, birthday):
        if name in self.contacts:
            self.contacts[name].birthday = birthday
            return f"Birthday for {name} added."
        return f"Contact {name} not found."

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Номер телефону повинен містити 10 цифр")
        super().__init__(value)


class Address(Field):
    pass


class Email(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Неправильний формат дати. Використовуйте ДД.ММ.РРРР")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    

    def add_address(self, address):
        self.address = Address(address)

    def add_email(self, email):
        self.email = Email(email)


    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Дата народження вже існує для цього контакту.")
        
    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        address = self.address.value if self.address else "Адреса не вказана"
        email = self.email.value if self.email else "Електронна пошта не вказана"
        birthday = self.birthday.value if self.birthday else "Дата народження не вказана"
        return f"Ім'я контакту: {self.name.value}, телефони: {phones}, адреса: {address}, електронна пошта: {email}, дата народження: {birthday}"
