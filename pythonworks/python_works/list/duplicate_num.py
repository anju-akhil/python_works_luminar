#print duplicate numbers

lst=[2,3,5,4,5,7,2,8]
lst.sort()
print(lst)
dup_lst=[]
for i in range(0,len(lst)-1):
    current=lst[i]
    next=lst[i+1]
    if current==next:
        #print(current)
        if current not in dup_lst:
            dup_lst.append(current)
print(dup_lst)