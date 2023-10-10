num=324
#o/p=9(4+2+3)
last_digit=0
sum=0
while(num!=0):
    
    last_digit=num%10 #0=324%10 which means last_digit=4
    #print(last_digit)
    sum=sum+last_digit
    num=num//10
    
print(sum)
    