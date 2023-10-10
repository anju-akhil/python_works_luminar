#NUBER SWAPPING

num1=11
num2=22
print(f"before swapping num1={num1} num2={num2}")
 ##using temp
#temp=num1
#num1=num2
#num2=temp
#print(f"after swap ---- num1={num1} num2={num2}")

 ##without using third variable
#num1,num2=num2,num1
#print(f"after swap ---- num1={num1} num2={num2}")

 ##using operator
num1=num1+num2 #22+11=33
num2=num1-num2 #22-11=11
num1=num1-num2 #33-11=22
print(f"After swapping num1={num1} num2={num2}")