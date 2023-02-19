import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


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
persons = Contacts(filename, contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True
