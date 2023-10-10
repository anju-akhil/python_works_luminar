from re import *
text="agdICeSUesd"
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text.casefold())
count=0
for m in matcher:
    #if m.group().isalpha():
    print(m.start(),m.group())
    count+=1
print("count",count)