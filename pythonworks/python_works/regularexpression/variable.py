from re import *
variable=input("Enter variable:")
rule="[a-zA-Z][\w_]*"
m=fullmatch(rule,variable)
print("valid"if m!=None else"invalid")