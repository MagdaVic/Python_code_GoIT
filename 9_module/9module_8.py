def get_emails(list_contacts):
    list_email = list(map(lambda i: i['email'], list_contacts))
    return list_email


list_contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},    {"name": "Allen Raymond",
       "email": "nulla.ante@ve66666666stibul.co.uk",
       "phone": "(992) 914-3792",
       "favorite": False}]

print(get_emails(list_contacts))
