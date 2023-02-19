import pickle
from copy import deepcopy, copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(self.name, self.email, self.phone, self.favorite)
        copy_obj.name = copy(self.name)
        copy_obj.email = copy(self.email)
        copy_obj.phone = copy(self.phone)
        copy_obj.favorite = copy(self.favorite)
        return copy_obj


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None, count_save=0, is_unpacking=False):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = count_save
        self.is_unpacking = is_unpacking

    def save_to_file(self):
        with open(filename, 'wb') as fh:
            pickle.dump(self, fh)

    def read_from_file(self):
        with open(filename, 'rb') as fh:
            self_unpack = pickle.load(fh)
            return self_unpack

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['count_save'] = self.count_save + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        value['is_unpacking'] = True

    def __copy__(self):
        copy_obj = Contacts(self.filename, self.contacts,
                            self.count_save, self.is_unpacking)
        copy_obj.filename = copy(self.filename)
        copy_obj.contacts = copy(self.contacts)
        copy_obj.count_save = copy(self.count_save)
        copy_obj.is_unpacking = copy(self.is_unpacking)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts,
                            self.count_save, self.is_unpacking)
        memo[id(copy_obj)] = copy_obj
        copy_obj.filename = deepcopy(self.filename)
        copy_obj.contacts = deepcopy(self.contacts)
        copy_obj.count_save = deepcopy(self.count_save)
        copy_obj.is_unpacking = deepcopy(self.is_unpacking)
        return copy_obj


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]
filename = r'12_module\user_class.txt'
person = Person('dadsd', 'dddd', 2222, False)
person_copy = copy(person)
person_copy.name = 'qqqqq'
print(person.name)
print(person_copy.name)
persons = Contacts(filename, contacts)
persons_deepcopy = deepcopy(persons)
persons_deepcopy.contacts[0].name = 'eeeee'
print(persons.contacts[0].name)
print(persons_deepcopy.contacts[0].name)
