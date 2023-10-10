#starting with an alphabwt k,l,m
#second place that must be a digit and that digit must be / by 3
#followed by any number of character

from re import *
variable=input("Enter variable name:")
rule="[klm][369][\w]*"
m=fullmatch(rule,variable)
print("Invalid"if m==None else"valid")