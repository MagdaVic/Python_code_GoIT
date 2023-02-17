
import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for i in contacts:
            writer.writerow({'name': i['name'], 'email': i['email'],
                            'phone': i['phone'], 'favorite': i['favorite']})


def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        contacts_new = [row for row in reader]
        for i in contacts_new:
            if i['favorite'] == 'False':
                i['favorite'] = False
            elif i['favorite'] == 'True':
                i['favorite'] = True
        return contacts_new

        # print(row['name'], row['email'], row['phone'],
        #       row['email'], row['favorite'])


contacts = [{"name": "Allen Raymond",
             "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792", "favorite": False}, {"name": "SSSS Raymond",   "email": "sssslla.ante@vestibul.co.uk",                                  "phone": "(002) 914-3792", "favorite": False}]

filename = '12_module\contacts.csv'
write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))
