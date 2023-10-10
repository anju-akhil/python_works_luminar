n=int(input("How many people="))

if n<10:
    for i in range(1,n+1):
        name=input("Enter the name=")
        print(name,"has been invited")
    
else:
    print("Too many people")