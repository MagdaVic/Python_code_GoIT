# x1 - command string
# x2 - first string after command (name)
# x3 - second string after command (phone)


def hello(x2=None, x3=None):
    print("How can I help you?")


def add_name_phone(list):
    x2, x3, *x0 = list
    # assert isinstance(x2, str)
    # assert isinstance(x3, str)
    if {'name': x2, 'phone': x3} not in list_name_phone:
        list_name_phone.append({'name': x2, 'phone': x3})
        print(f'New contacts (name: {x2}, phone: {x3}) are added')


def change_phone(x2, x3):
    assert isinstance(x2, str)
    assert isinstance(x3, str)
    for i in list_name_phone:
        if x2 == i['name']:
            i['phone'] = x3
    print(f'New phone of {x2} is changed')


def phone(x2, x3=None):
    assert isinstance(x2, str)
    for i in list_name_phone:
        if x2 == i['name']:
            list_name_phone: print(f"Phone of {x2} is {i['phone']}")


def show_all(x2=None, x3=None):
    for i in list_name_phone:
        print(f"name: {i['name']}, phone: {i['phone']}")


def main():
    COMMANDS = {'hello': hello, 'add': add_name_phone,
                'change': change_phone, 'phone': phone, 'show all': show_all}
    flag = True
    while flag:
        commands_list = input('Enter your command:').split()
        try:
            commands_list[0]
        except IndexError:
            commands_list = input('Enter your command:').split()
        else:
            if commands_list[0] == 'exit':
                flag = False
            result_comand = COMMANDS[commands_list[0].lower()]
            commands_list.pop(0)
            result_comand(commands_list)
            print(list_name_phone)


if __name__ == '__main__':
    list_name_phone = []
    main()
