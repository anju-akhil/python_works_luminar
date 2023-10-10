from re import *
text="AD7 &r8/gSm"
#pattern="[a-zA-Z0-9]" #-------- all alphanumeric characters
#pattern="[A-Z]" #-------------- only capitals
#pattern="[^0-9]" #------------- except numbers
#pattern="[^a-zA-Z0-9]" #------- special character
pattern="[a-z]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())