start=1
prev=0
crnt=1
print(prev)
print(crnt)
while(start<=10):
    sum=prev+crnt
    print(sum)
    prev=crnt
    crnt=sum
    start+=1

