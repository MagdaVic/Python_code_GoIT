import sys
# x1 - command value
# x2 - first value after command (name)
# x3 - second value after command (phone)
# *x0 - possible value in the end of command string, that user can input


def input_error_name(func):
    def wrapper(output_list):
        try:
            x2, *x0 = output_list
        except ValueError:
            print('Enter user name')
        else:
            return func(output_list)
    return wrapper


def input_error_name_phone(func):
    def wrapper(output_list):
        try:
            x2, x3, *x0 = output_list
        except ValueError:
            print('Give me name and phone please')
        else:
            return func(output_list)
    return wrapper


def hello(output_list):
    print("How can I help you?")


@input_error_name_phone
def add_name_phone(output_list):
    x2, x3, *x0 = output_list
    if {'name': x2, 'phone': x3} not in list_name_phone:
        list_name_phone.append({'name': x2, 'phone': x3})
        print(f'New contacts (name: {x2}, phone: {x3}) are added')


@input_error_name_phone
def change_phone(output_list):
    x2, x3, *x0 = output_list
    for i in list_name_phone:
        if x2 == i['name']:
            i['phone'] = x3
    print(f'New phone of {x2} is changed')


@input_error_name
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


if __name__ == '__main__':
    list_name_phone = []
    main()
