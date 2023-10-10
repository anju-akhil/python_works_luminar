#check whether given number is in fibonacci series
num=int(input("Enter a number to check="))
start=1
prev=0
cnt=1
print(prev)
print(cnt)
is_present=False
sum=0
while(start <= num):
    sum=prev+cnt
    if sum==num:
        is_present=True
        break
    print(sum)
    prev=cnt
    cnt=sum
    

    start+=1
print(is_present)