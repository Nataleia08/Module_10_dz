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
    def __init__(self, name, phone) -> None:
        self.name = Name(name)
        self.phone = []
        for p in phone:
            self.phone.append(p)


class AddressBook(UserDict):
    def __init__(self) -> None:
        pass

    def add_record(self, name, phone):
        self.data.name = name
        for v in phone:
            self.data[name].append(v)
        print("Contact save fine!")

    def change_record(self, name, phone):
        try:
            for v in phone:
                self.data[name].append(v)
            print("Contact save fine!")
        except:
            print("There is no user with this name!")

    def search_phone(self, name):
        try:
            print(self.data[name])
        except:
            print("There is no user with this name!")

    def show_all(self):
        print(self.data)


class User():
    def __init__(self):
        pass

    def command_hello(self):
        """Функція привітання"""
        print("How can I help you?")

    def command_exit(self):
        """Функція виходу"""
        sys.exit("Good bye!")


address_book = AddressBook()
user_1 = User()
command_list = ["hello", "add", "change",
                "phone", "show all", "close", "exit", "good bye"]
while True:
    command_string = input("Enter command:").lower()
    if command_string == ".":
        break
    find_command = False
    for k in command_list:
        if k in command_string:
            input_com = k
            attribute_sring = command_string.removeprefix(k).strip()
            find_command = True
            break
    if not find_command:
        print("Command undefined! Try again!")
        continue
    input_list = attribute_sring.split(" ")
    for i in input_list:
        if i.isalpha():
            name = i
            input_list.remove(name)
            phone = " ".join(input_list)
            break
    if command_string == "hello":
        user_1.command_hello()
    elif (command_string == "close") or (command_string == "exit") or (command_string == "good bye"):
        user_1.command_exit()
    elif command_string == "add":
        try:
            address_book.add_record(name, phone)
        except:
            print("Give me name and phone please!")
    elif command_string == "change":
        try:
            address_book.change_record(name, phone)
        except:
            print("Give me name and phone please!")
    elif command_string == "phone":
        try:
            address_book.search_phone(name)
        except:
            print("Enter user name!")
    elif command_string == "show all":
        address_book.show_all()