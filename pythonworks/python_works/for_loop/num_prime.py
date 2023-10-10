#chk given number is prime or not

num=11
is_prime=True
if num in [0,1]:
    is_prime=False
else:
    for i in range(2,num):
        if(num %i==0):
            is_prime=False
            break
print(is_prime)