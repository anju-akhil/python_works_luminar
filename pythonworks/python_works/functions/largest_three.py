a=int(input("Enter a number="))
b=int(input("Enter a number="))
c=int(input("Enter a number="))
def largest(a,b,c):
    if(a>b)and(a>c):
        print(a," is largest")
    elif(b>a)and(b>c):
        print(b," is largest")
    elif(c>a)and(c>a):
        print(c," is largest")
largest(a,b,c)