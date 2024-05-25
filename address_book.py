import re
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
    def __init__(self, value):
        if not self.address_validation(value):
            raise ValueError("Адреса повинна містити: вулицю, номер будинку")
        super().__init__(value)
        
    def address_validation(self, address):
        parts = address.split(',')
        if len(parts) < 2:
            return False
        street, house_number = parts[:2]
        return bool(street.strip()) and bool(house_number.strip())


class Email(Field):
    def __init__(self, value):
        if not self.email_validation(value):
            raise ValueError("Неправильний формат електронної пошти")
        super().__init__(value)
    
    def email_validation(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None


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

    def birthdays(self, days):
        today = date.today()
        this_week = today + timedelta(days=days)
        upcoming_birthdays = []

        for name, contact in self.contacts.items():
            if contact.birthday:
                birthday_date = datetime.strptime(contact.birthday, '%d.%m.%Y').date()
                birthday_date = birthday_date.replace(year=today.year)
                if birthday_date < today:
                    birthday_date = birthday_date.replace(year=today.year + 1)
                if today <= birthday_date <= this_week:
                    upcoming_birthdays.append((name, birthday_date))

        if upcoming_birthdays:
            message = "Birthdays this week:\n"
            for name, birthday in upcoming_birthdays:
                message += f"{name}: {birthday.strftime('%Y-%m-%d')}\n"
        else:
            message = "There are no birthdays this week."
        return message
        
    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        address = self.address.value if self.address else "Адреса не вказана"
        email = self.email.value if self.email else "Електронна пошта не вказана"
        birthday = self.birthday.value if self.birthday else "Дата народження не вказана"
        return f"Ім'я контакту: {self.name.value}, телефони: {phones}, адреса: {address}, електронна пошта: {email}, дата народження: {birthday}"
