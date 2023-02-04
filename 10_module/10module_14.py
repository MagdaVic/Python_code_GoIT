class Contacts:
    current_id = 0

    def __init__(self):
        self.contacts = []

    def list_contacts(self):

        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        Contacts.current_id = Contacts.current_id+1
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite
        self.dict_contacts = {'id': Contacts.current_id,
                              'name': self.name, 'phone': self.phone, 'email': self.email, 'favorite': self.favorite}
        self.contacts.append(self.dict_contacts)


con1 = Contacts()
con1.add_contacts('Wylie Pope', '(692) 802-2949', 'est@utquamvel.net', True)
con1.add_contacts('Wyliesss', '(692) 80244444', 'estamvel.net', False)
print(con1.list_contacts())

[{'id': 1, 'name': 'Wylie Pope', 'phone': '(692) 802-2949', 'email': 'est@utquamvel.net', 'favorite': True}, {
    'id': 2, 'name': 'Cyrus Jackson', 'phone': '(501) 472-5218', 'email': 'nibh@semsempererat.com', 'favorite': False}]
