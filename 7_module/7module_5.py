
import re
def capital_text(s):
    new_s=s[0].upper()
    lst=[]
    pattern = r'(?<=[\n|\.|\!|\?])\s*[a-zа-яґєії0-9]'
    matches = re.finditer(pattern, s)
    for i in matches:
        start_i, end_i=i.span()
        lst.append(end_i-1)
    for i in range(1,len(s)):
        if i not in lst:
            new_s=new_s+s[i]
        else:
            new_s=new_s+s[i].upper()
    
    return new_s

# import re
# def capital_text(s):
#     result = re.findall(r'[\w\s]+[\n\.\!\?]+', s)
#     print (result)
#     result = ' '.join([i.strip().capitalize() for i in result])
#     return result


s='d\nahfhfjf jdj ffdjfdk \ndsjfdjfd.\n fsffff!     sfsgfhghg vggnn? hf' 
print(capital_text(s))

       
       
 



