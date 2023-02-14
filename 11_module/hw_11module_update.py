from collections import UserDict
import re 
from datetime import datetime
import sys


class Field:
    def __init__(self):
        self._value = None


class Name(Field):
    def __init__(self, value):
        self.value=value
    
    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value





class Phone(Field):
    def __init__(self, value):
        self.value=value
    
    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if re.search(r'^\+?3?8?(0[\s\.-]?\d{2}[\s\.-]?\d{3}[\s\.-]?\d{2}[\s\.-]?\d{2})$',value):
            self._value = value
        else:
            raise Exception("Phone number must consist only from numbers and have format: +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX or without '+38'")
    


class Birthday(Field):
    def __init__(self, value):
        self.value=value

    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if re.search(r'\d{2}\.\d{2}\.\d{4}',value):
            self._value = value
        else:
            raise Exception ("Birthday must have format 'DD.MM.YYYY' and consist only from numbers")
    
class Record:
    def __init__(self, name:Name, phone:Phone=None, birthday:Birthday=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        if birthday:
            self.birthday=birthday

    def __repr__(self) -> str:
        return f'Name: {self.name}, Phones: {self.phones}'
        

    def add_phones(self, phone:Phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def change_phones(self, phone, phone_new:Phone):
        for count, ele in enumerate(self.phones):
            if ele.value == phone:
                self.phones[count] = phone_new
                break

    def remove_phones(self, phone):
        for count, ele in enumerate(self.phones):
            if ele.value == phone:
                self.phones.remove(ele)
                break

    def list_phones(self):
        return self.phones

    def days_to_birthday(self,birthday):
        self.birthday=datetime.strptime(birthday.value, '%d.%m.%Y')
        now = datetime.now()
        delta1 = datetime(now.year, self.birthday.month, self.birthday.day)
        delta2 = datetime(now.year+1, self.birthday.month, self.birthday.day)
        return ((delta1 if delta1 > now else delta2) - now).days

 
class AddressBook(UserDict):
    def __repr__(self):
        return f'{self.data}'

    def add_record(self, record:Record):
        self.data[record.name.value] = record
        return self.data
        
    def iterator(self, n=2):
        index = 0
        lst_temp = []
        for k, v in self.data.items():
            lst_temp.append(v)
            index = index + 1
            if index >= n: 
                yield lst_temp
                lst_temp.clear()
                index = 0
        if lst_temp:
            yield lst_temp    
    
    def show_all_limit(self, n=2):
        step = self.iterator(n)
        for i in range(len(self.data)):
            try:
                result = next(step)
                print(result)
                input('Press enter for next page: ')
            except StopIteration:
                break
            

# command  - command value
# name - first value after command (name)
# phone - second value after command (phone)
# phone_new - third value after command (phone_new for changing phones)
# n - quantity of viewes in adress book
# *other - possible value in the end of command string, that user can input

def input_error_name(func):
    def wrapper(output_list,address_book):
        try:
            name, *other = output_list
        except ValueError:
            print('Enter user name')
        else:
            return func(output_list,address_book)
    return wrapper

def input_error_name_phone(func):
    def wrapper(output_list,address_book):
        try:
            name, phone, *other = output_list
        except ValueError:
            print('Give me name and phone please')
        else:
            return func(output_list,address_book)
    return wrapper

def input_error_name_phone_phone_new(func):
    def wrapper(output_list,address_book):
        try:
            name, phone, phone_new, *other = output_list
        except ValueError:
            print('Give me name, phone and new phone please')
        else:
            return func(output_list,address_book)
    return wrapper

def hello(output_list, address_book:AddressBook):
    print("How can I help you?")


@input_error_name_phone
def add_name_phone(output_list, address_book:AddressBook):
    name, phone, *other = output_list
    record = address_book.get(name)
    if record:
        record.add_phones(Phone(phone))
        print(address_book)
        print(f'New phone {phone} of {name} is added')
    else:
        address_book.add_record(Record(Name(name),Phone(phone)))
        print(address_book)
        print(f'New contacts (name: {name}, phone: {phone}) are added')


@input_error_name_phone_phone_new
def change_phone(output_list, address_book:AddressBook):
    name, phone, phone_new, *other = output_list
    record = address_book.get(name)
    if record:
        record.change_phones(phone, Phone(phone_new))
        print(record)
        print(address_book)
        print(f'Phone {phone} of {name} is changed. New phone is {phone_new} ')

@input_error_name_phone       
def remove_phone(output_list, address_book:AddressBook):
    name, phone, *other = output_list
    record = address_book.get(name)
    if record:
        record.remove_phones(phone)
        print(address_book)
        print(f'Phone {phone} of {name} is removed')

# @input_error_name
# def phone(output_list):
#     x2, *x0 = output_list
#     for i in list_name_phone:
#         if x2 == i['name']:
#             print(f"Phone of {x2} is {i['phone']}")


def show_all(output_list, address_book:AddressBook):
    if output_list:
        n,*other=output_list
        address_book.show_all_limit(int(n))
    else:
        address_book.show_all_limit()



# def exit_from_chat(output_list):
#     sys.exit('Good bye!')


def main():
    address_book=AddressBook()
    

    COMMANDS = {'hello': hello, 'add': add_name_phone,'change': change_phone, 'remove phone': remove_phone,'show all': show_all} 
    # , 'good bye': exit_from_chat, 'close': exit_from_chat, 'exit': exit_from_chat}
    while True:
        commands_string = input(
            'Enter your command (hello, add, change, phone, show all, good bye, close, exit):').lstrip()
        for i in COMMANDS.keys():
            if commands_string.lower().startswith(i):
                command = commands_string[:len(i)].lower()
                command_parametres_list = commands_string[len(i)+1:].split()
                COMMANDS[command](command_parametres_list, address_book)
                break


if __name__ == '__main__':
    list_name_phone = []
    main()










