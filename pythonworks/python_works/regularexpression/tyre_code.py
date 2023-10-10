#3digit
#/
#2digit
#R
#2digit
#/
#min 2 max 3 digit
#alphabet

from re import *
tyre=input("Enter tyre code:")
rule="\d{3}[/]\d{2}[R]\d{2}[/]/d{2,3}[A-Z]"
m=fullmatch(rule,tyre)
print("valid"if m!=None else"invalid")