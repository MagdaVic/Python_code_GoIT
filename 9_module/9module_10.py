def get_favorites(contacts):
    list_favourite = list(filter(lambda i: i["favorite"], contacts))
    return list_favourite


contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},    {"name": "Allen Raymond",
       "email": "nulla.ante@ve66666666stibul.co.uk",
       "phone": "(992) 914-3792",
       "favorite": True}]

print(get_favorites(contacts))
