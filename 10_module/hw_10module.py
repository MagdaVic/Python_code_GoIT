from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phones(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def change_phones(self, phone, phone_new):
        for count, ele in enumerate(self.phones):
            if ele == phone:
                self.phones[count] = phone_new
                break

    def remove_phones(self, phone):
        for count, ele in enumerate(self.phones):
            if ele == phone:
                self.phones.remove(ele)
                break

    def list_phones(self):
        return self.phones


name1 = Name('Bob')
print(name1.value)
phone1 = Phone('234637373')
print(phone1.value)
phone2 = Phone('3647474')
phone3 = Phone('364747555')
phone4 = Phone('1')
record1 = Record(name1, phone1)
print(record1.name)
record1.add_phones(phone2)
record1.add_phones(phone3)
print(record1.list_phones())
record1.change_phones(phone1, phone4)
print(record1.list_phones())
record1.remove_phones(phone4)
print(record1.list_phones())
