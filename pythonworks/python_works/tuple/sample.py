#Check if all items in the tuple are the same


tuple=(1,1,5,1)
for i in tuple:
    if i==tuple[1]:
        t=True
    else:
        t=False
print(t)