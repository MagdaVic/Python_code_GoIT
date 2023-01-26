from decimal import Decimal, getcontext
from statistics import mean


def decimal_average(number_list, signs_count):
    
    getcontext().prec = signs_count
    # decimal_avr=(mean([Decimal(i) for i in number_list]))
    decimal_avr=sum([Decimal(i) for i in number_list])/Decimal(len(number_list))

    return decimal_avr


number_list, signs_count=[3, 5, 77, 23, 0.57], 6
print(decimal_average(number_list, signs_count)) #21.714