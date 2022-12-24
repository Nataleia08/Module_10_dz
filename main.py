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
    def __init__(self, phone) -> None:
        Field.__init__(self)
        self.phone = phone


class Record():
    def __init__(self, name, phone) -> None:
        self.name = Name(name)
        self.phone = []
        if type(phone) == str:
            self.phone.append(Phone(phone))
        elif type(phone) == list:
            for p in phone:
                self.phone.append(Phone(p))
        else:
            self.phone.append(Phone(str(phone)))

    def add_phone(self, phone_new):
        self.phone.append(Phone(phone_new))

    def change_phone(self, phone_new):
        self.phone.extend(Phone(phone_new))

    def delete_phone(self, phone_new):
        try:
            self.phone.remove(Phone(phone_new))
        except:
            print("This phone not found!")


class AddressBook(UserDict):
    def __init__(self) -> None:
        UserDict.__init__(self)

    def __setitem__(self, name, phone) -> None:
        self.data[name] = Record(name, phone)

    def add_record(self, name, phone):
        """Функція додання запису"""
        try:
            self.data[name] = Record(name, phone)
            print("Contact save fine!")
        except:
            print("Error!")

    def change_record(self, name, phone):
        """Функція зміни запису"""
        try:
            self.data[name].change_phone(phone)
            print("Contact save fine!")
        except:
            print("There is no user with this name!")

    def search_phone(self, name):
        """Функція пошуку телефону за ім'ям"""
        try:
            result = []
            for p in self.data.get(name).phone:
                result.append(p.phone)
            print(" ".join(result))
        except:
            print("There is no user with this name!")

    def show_all(self):
        """Функція відображення списку контактів"""
        try:
            result = []
            for key_name in self.data.keys():
                result.append(key_name.title())
                phone_l = self.data.get(key_name).phone
                for i in phone_l:
                    result.append(i.phone)
                result.append("\n")
            print(" ".join(result))
        except Exception as e:
            print("Error!", e.args)


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
    # ----------------------------Розпізнавання введених даних-----------------------
    command_string = input("Enter command:").lower()
    if command_string == ".":
        break
    find_command = False
    for k in command_list:
        if k in command_string:
            input_com = k
            attribute_sring = command_string.strip().replace(input_com, "")
            find_command = True
            break
    if not find_command:
        print("Command undefined! Try again!")
        continue
    input_list = attribute_sring.split(" ")
    # input_list.remove(input_com)
    for i in input_list:
        if i.isalpha():
            name = Name(i)
            input_list.remove(i)
            phone = Phone(input_list)
            break
    # ----------------------------Виконання команди--------------------------------------
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
