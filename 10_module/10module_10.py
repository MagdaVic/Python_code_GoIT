from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum


lst = AmountPaymentList([1, -3, 4])
print(lst.amount_payment())
