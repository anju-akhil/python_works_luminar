num=int(input("Enter the number="))
original=num
digit_count=len(str(num))
sum=0
while(num!=0):
    last_digit=num%10
    exponent=last_digit**digit_count
    sum=sum+exponent
    num=num//10

print("Armstrong number" if sum==original else "Not Armstrong number")