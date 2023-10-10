#num=124    #not armstrong num
#num=370     # armstrong num
#o/p=36(1**3 + 2**3 + 3**3)
num=1634
last_digit=0
sum=0
original=num
while(num!=0):
    last_digit=num%10
    #print(last_digit)
    #last_digit=last_digit**3   #3 for 3digit number

    last_digit=last_digit**4
    #print(last_digit)
    sum=sum+last_digit
    num=num//10
    
print(sum)
if(original==sum):
    print("The given number is armstrong number")
else:
    print("The given number is not armstrong number")