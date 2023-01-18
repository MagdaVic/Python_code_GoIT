def sequence_buttons(string):
    number_res=''
    dict_symbols={'1':'.,?!','2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8':'TUV','9':'WXYZ','0':' '}
    dict_reverse={v: k for k, v in dict_symbols.items()}
    print(dict_reverse)
    for let in string:
        for k,v in dict_reverse.items():
            if k.find(let.upper())!=-1:
                number_res=number_res+v*(k.find(let.upper())+1)
    return number_res
            

string='Hello, World!'
print(sequence_buttons(string))