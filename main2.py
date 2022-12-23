import sys
from collections import UserDict


class Field():
    def __init__(self) -> None:
        pass


class Name(Field):
    def __init__(self, name) -> None:
        Field.__init__(self)
        self.name = name


class Phone(Field):
    def __init__(self, phone="") -> None:
        Field.__init__(self)
        self.phone = phone


class Record():
    def __init__(self, name, phone=[]) -> None:
        self.name = Name(name)
        self.phone = [Phone(phone)]


class AddressBook(UserDict):
    def __init__(self) -> None:
        self.data = Record()

    def add_record(self, name, phone):
        self.data.name = name
        for v in phone:
            self.data[name].append(v)
        return "Contact save fine!"

    def change_record(self, name, phone):
        for v in phone:
            self.data[name].append(v)
        return "Contact save fine!"

    def search_phone(self, name):
        try:
            print(self.data[name])
        except:
            print("Not found!")

    def show_all(self):
        print(self.data)


class User():
    def __init__(self):
        pass

    def command_hello(self):
        """Функція привітання"""
        return "How can I help you?"

    def command_exit(self):
        """Функція виходу"""
        sys.exit("Good bye!")


CONTACTS = AddressBook()
