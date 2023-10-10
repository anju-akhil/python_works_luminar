#multiplication table of a given number
n=int(input("Enter anumber="))
for i in range(1,10+1):
    multi=i*n
    print(i,"*",n,"=",multi)