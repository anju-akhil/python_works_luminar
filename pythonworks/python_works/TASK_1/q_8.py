start=int(input("Enter starting number="))
n=int(input("Enter ending number="))
print("Even numbers")
for i in range(start,n+1):
    if i%2==0:
        print(i)