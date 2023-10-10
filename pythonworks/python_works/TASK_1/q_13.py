n=int(input("Enter a number="))
val=0
while(val!=n):
    if n<10:
        print("Too low\n","Try again")
        n=int(input("Enter a number again="))
    elif n>20:
        print("Too high\n","Try again")
        n=int(input("Enter a number again="))
    elif n>=10 and n<=20:
        print("Thank you")
        break