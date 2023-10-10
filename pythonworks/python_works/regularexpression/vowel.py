from re import *
text="agdICeSUesd"
pattern="[aeiouAEIOU]"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print("count",count)