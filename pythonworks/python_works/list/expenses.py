expenses=[12000,13000,14000,15000,20000,22000]
#for i in expenses:
 #   if i>15000:
  #      print(i)

#-----total expenses-------
total=0
for e in expenses:
    total=total+e
print("Total expenses=",total) 

#----highest expenses-----
max=0
for i in expenses:
    if i>max:
        max=i

print("highest expense",max)

#------cheapest expenses---------
min=expenses[0]
for i in expenses:
    if i<min:
        min=expenses[i]
print("cheapest expenses",min)

