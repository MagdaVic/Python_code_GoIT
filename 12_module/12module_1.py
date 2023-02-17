import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as fh:
        contacts_unpack = pickle.load(fh)
        return contacts_unpack


contacts = [{"name": "Allen Raymond",
             "email": "nulla.ante@vestibul.co.uk",
             "phone": "(992) 914-3792", "favorite": False, }, {"name": "SSSS Raymond",   "email": "sssslla.ante@vestibul.co.uk",                                  "phone": "(002) 914-3792", "favorite": False, }]
filename = '12_module\contacts.bin'
write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))
