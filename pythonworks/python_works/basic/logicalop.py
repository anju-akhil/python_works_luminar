#   and operator
"""num1=10
print(num1>0)
print(num1>15)
print(num1<0 and num1>15)

#print the height and weight ratio => height<157,weight<55 =>true
height=150
weight=54
print(height<157)   #true
print(weight<55)    #true
print(height<157 and weight<55) #true
print("")

print(height>157)   #false
print(weight>55)    #false
print(height>157 and weight>55) #false
print("")

print(height<157)   #true
print(weight>55)    #false
print(height<157 and weight>55) #false
print("")

print(height>157)   #false
print(weight<55)    #true
print(height>157 and weight<55) #false """""

        # or operator
    #either greater than 20 or negative
num1=25
num2=-5
print(num1>20) #true
print(num2<0) #true
print(num1>20 or num2<0) #true
print("")

print(num1<20) #false
print(num2>0) #false
print(num1<20 or num2>0) #false
print("")

print(num1>20) #true
print(num2>0) #false
print(num1>20 or num2>0) #true
print("")

print(num1<20) #false
print(num2<0) #true
print(num1<20 or num2<0) #true
print("")

        # not operator

print(not num1>20)#false
print(not num1<20)#true