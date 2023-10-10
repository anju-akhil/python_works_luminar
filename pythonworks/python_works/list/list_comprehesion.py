
lst=[2,3,4,6,7,8]

#square
square=[n**2 for n in lst]
print("squre=",square)

#add with 2
add_two=[n+2 for n in lst]
print("add_two=",add_two)

#print all numbers greater than 5
num=[n<5 for n in lst]
print("<5=",num)

#print even
even=[n for n in lst if n%2==0]
print("even=",even)

#print odd
odd=[n for n in lst if n%2!=0]
print("odd=",odd)