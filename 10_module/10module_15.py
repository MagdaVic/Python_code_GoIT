class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        res_contacts = list(filter(lambda i: i['id'] == id, self.contacts))
        return res_contacts[0] if len(res_contacts) > 0 else None

    # def get_contact_by_id(self, id):
    #     res_contacts = None
    #     for i in self.contacts:
    #         if i['id'] == id:
    #             res_contacts = i
    #     return res_contacts
