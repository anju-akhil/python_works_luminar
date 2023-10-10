#starting with KL
#two digit
#alphabets minimum 1 max 2
#4 digits

from re import *
vehicle=input("Enter vehicle number:")
rule="(KL)-\d{2}-[A-Z]{1,2}-\d{4}"
m=fullmatch(rule,vehicle)
print("valid"if m!=None else"Invalid")