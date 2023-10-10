#print total sum of all odd_numbers and even_numbers from given start to end range
start=10
end=20
odd_sum=0
even_sum=0
while(start<=end):
    if start %2==0:
        #print("even",start)
        even_sum=even_sum+start
        
    else:
        #print("odd",start)
        odd_sum=odd_sum+start
    start+=1
print("Even Sum=",even_sum)
print("Odd Sum=",odd_sum)
