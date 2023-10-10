#fibonacci sequence up to a given number
n=int(input("Enter anumber="))
prev=0
cnt=1
print(prev)
print(cnt)
for i in range(1,n+1):
    sum=prev+cnt
    #print(sum)
    prev,cnt=cnt,sum
    if sum <=n:
        print(sum)
    else:
        break
    