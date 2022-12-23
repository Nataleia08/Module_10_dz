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
        UserDict.__init__(self)

    def add_record(self, name, phone):
        self.data[name] = []
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
            print(self.data.get(name))
        except:
            print("There is no user with this name!")

    def show_all(self):
        for k in self.data.keys():
            print(k, ":", " ".join(self.data.get(k)))


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
            name = Name(i.title())
            input_list.remove(i)
            phone = Phone(input_list)
            break
    if input_com == "hello":
        user_1.command_hello()
    elif (input_com == "close") or (input_com == "exit") or (input_com == "good bye"):
        user_1.command_exit()
    elif input_com == "add":
        try:
            address_book.add_record(name.name, phone.phone)
        except:
            print("Give me name and phone please!")
    elif input_com == "change":
        try:
            address_book.change_record(name.name, phone.phone)
        except:
            print("Give me name and phone please!")
    elif input_com == "phone":
        try:
            address_book.search_phone(name.name)
        except:
            print("Enter user name!")
    elif input_com == "show all":
        address_book.show_all()
    else:
        print("Command undefined! Try again!")
