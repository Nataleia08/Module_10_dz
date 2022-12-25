from main import Field, Name, Phone, Record, AddressBook
if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phone, list)
    assert isinstance(ab['Bill'].phone[0], Phone)
    assert ab['Bill'].phone[0].value == '1234567890'

    print('All Ok)')
