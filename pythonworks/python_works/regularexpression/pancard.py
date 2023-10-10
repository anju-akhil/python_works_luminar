#first 3 characters must be any random uppercase alphabet
#in 4th place P,F,A,C,H,T
#in 5th place uppercase random alphabet
#4 digit
#in last place one random alphabet

from re import *
pan_id=input("Enter pancard:")
rule="[A-Z]{3}[PFACHT][A-Z]{1}\d{4}[A-Z]{1}"
m=fullmatch(rule,pan_id)
print("valid"if m!=None else"invalid")