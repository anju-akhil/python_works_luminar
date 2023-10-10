numbers=[1,4,10,11,12]
even_list=[]
odd_list=[]
for i in numbers:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even list=",even_list)
print("Odd list=",odd_list)    