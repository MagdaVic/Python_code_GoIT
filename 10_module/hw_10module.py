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
        # self.phone = phone
        self.phones = []
