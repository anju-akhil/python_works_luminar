from re import *
text="gafgafhaaa"

#pattern="a+" #one or more occurance of a
#pattern="a*" #zero or more occurance of a
pattern="a{1,2}" #
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())