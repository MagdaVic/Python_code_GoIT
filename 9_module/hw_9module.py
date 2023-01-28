import sys
# x1 - first string after command
# x2 - second string after command


def hello(x1=None, x2=None):
    print("How can I help you?")


def add_name_phone(x1, x2):
    if {'name': x1.lower(), 'phone': x2.lower()} not in list_name_phone:
        list_name_phone.append({'name': x1, 'phone': x2})
        print(f'New contacts (name: {x1}, phone: {x2}) are added')


def change_phone(x1, x2):
    for i in list_name_phone:
        if x1 == i['name']:
            i['phone'] = x2
    print(f'New phone of {x1} is changed')


def main():
    COMMANDS = {'hello': hello, 'add': add_name_phone, 'change': change_phone}

    result_comand = COMMANDS[sys.argv[1]]
    result_comand(sys.argv[2] if len(sys.argv) >= 3 else None,
                  sys.argv[3] if len(sys.argv) >= 4 else None)


if __name__ == '__main__':
    list_name_phone = []
    main()
