from collections import UserDict
import re 


class Field:
    def __init__(self):
        self._value = None


class Name(Field):
    def __init__(self, value):
        self.value=value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value



class Phone(Field):
    def __init__(self, value):
        self.value=value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if re.search(r'^\+?3?8?(0[\s\.-]?\d{2}[\s\.-]?\d{3}[\s\.-]?\d{2}[\s\.-]?\d{2})$',value):
            self._value = value
        else:
            raise Exception ('Phone number must have format and consist only from numbers: +380 XX XXX XX XX')

# class Birthday:



class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phones(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def change_phones(self, phone, phone_new):
        for count, ele in enumerate(self.phones):
            if ele == phone:
                self.phones[count] = phone_new
                break

    def remove_phones(self, phone):
        for count, ele in enumerate(self.phones):
            if ele == phone:
                self.phones.remove(ele)
                break

    def list_phones(self):
        return self.phones


class AddressBook(UserDict):


    def add_record(self, record):
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
    
    def get_page(self, n=2):
        step = self.iterator(n)
        for i in range(len(self.data)):
            try:
                result = next(step)
                print(result)
                input('Press enter for next page: ')
            except StopIteration:
                break



name1=Name('Bob')
print(name1.value)
name2=Name('Ggg')
name3=Name('aaa')
phone1 = Phone('+380639579750')
print(phone1.value)
phone2 = Phone('0639579750')
phone3 = Phone('0639579000')







