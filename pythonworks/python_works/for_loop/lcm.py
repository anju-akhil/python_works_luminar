# least common multiple
num1=36
num2=24

n=num1 if (num1>num2) else num2
for i in range(n,1+(num1*num2)):
    if i%num1 ==i%num2==0:
        lcm=i
        break
print(lcm)