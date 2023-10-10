name=input("Enter your name=")
n=int(input("Enter a number="))
if n<10:
    for i in range(1,n+1):
        print(name)
else:
    print("Too high")