from re import*
f=open("C:\\Users\\HP\\Desktop\\pythonworks\\regularexpression\\data.txt")
phone_rule="\d{10}"
mail_rule="[\w]+@gmail.com"
phone_numbers=[]
mail_ids=[]
for line in f:
    words=line.rstrip("\n").split()  #--remove new line
    for w in words:
        matcher=fullmatch(phone_rule,w)
        email_matcher=fullmatch(mail_rule,w)
        if matcher!=None:
            phone_numbers.append(w)
        elif email_matcher!=None:
            mail_ids.append(w)
print(phone_numbers)
print(mail_ids)