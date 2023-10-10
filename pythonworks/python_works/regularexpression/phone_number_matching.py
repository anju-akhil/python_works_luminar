from re import*
phone=input("Enter phone number:")
rule="\d{10}"
m=fullmatch(rule,phone)
if(m==None):
    print("Invalid")
else:
    print("Valid")