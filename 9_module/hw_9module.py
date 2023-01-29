import sys
# x1 - command string
# x2 - first string after command (name)
# x3 - second string after command (phone)


def hello(output_list):
    print("How can I help you?")


def add_name_phone(output_list):
    x2, x3, *x0 = output_list
    if {'name': x2, 'phone': x3} not in list_name_phone:
        list_name_phone.append({'name': x2, 'phone': x3})
        print(f'New contacts (name: {x2}, phone: {x3}) are added')


def change_phone(output_list):
    x2, x3, *x0 = output_list
    for i in list_name_phone:
        if x2 == i['name']:
            i['phone'] = x3
    print(f'New phone of {x2} is changed')


def phone(output_list):
    x2, *x0 = output_list
    for i in list_name_phone:
        if x2 == i['name']:
            print(f"Phone of {x2} is {i['phone']}")


def show_all(output_list):
    for i in list_name_phone:
        print(f"name: {i['name']}, phone: {i['phone']}")


def exit_from_chat(output_list):
    sys.exit('Good bye!')


def main():
    COMMANDS = {'hello': hello, 'add': add_name_phone,
                'change': change_phone, 'phone': phone, 'show all': show_all, 'good bye': exit_from_chat, 'close': exit_from_chat, 'exit': exit_from_chat}
    while True:
        commands_string = input(
            'Enter your command (hello, add, change, phone, show all, good bye, close, exit):').lstrip()
        for i in COMMANDS.keys():
            if commands_string.lower().startswith(i):
                command = commands_string[:len(i)].lower()
                command_parametres_list = commands_string[len(i)+1:].split()
                COMMANDS[command](command_parametres_list)
                break
        print(list_name_phone)


if __name__ == '__main__':
    list_name_phone = []
    main()
