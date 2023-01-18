import re
def token_parser(s):
    s=s.replace(' ','')
    lst_num=re.findall(r'\d+|[+*()/-]', s)
    return lst_num

s="2+ 34-5 * 3"
# "2+ 34-5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
print(token_parser(s))