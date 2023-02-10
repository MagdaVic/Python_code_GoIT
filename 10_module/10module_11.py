from collections import UserString


class NumberString(UserString):
    def number_count(self):
        numbercount = 0
        for i in self.data:
            if i.isdigit():
                numbercount = numbercount+1
        return numbercount


str1 = NumberString('dff34 fgg4')
print(str1.number_count())
