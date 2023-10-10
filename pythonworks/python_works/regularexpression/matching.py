from re import *
text="ababdabab"
matcher=finditer("ab",text)
count=0
for m in matcher:
    ##print(m.start()) #start--->for position (like---0 2 4 6)
    ##print(m.group()) #==>for matched group(like----ab ab ab ab)
    print(m.start(),m.group())
    count+=1
print("Total count=",count)