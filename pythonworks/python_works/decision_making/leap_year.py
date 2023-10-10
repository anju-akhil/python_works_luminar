#A year is called a leap year if it contains an additional day which makes the number of the days in that year is 366. This additional day is added in February which makes it 29 days long.

#A leap year occurred once every 4 years.

year = int(input("Enter a year="))
if (year%400 == 0) or (year%4==0 and year%100!=0): #year variable is divisible by 400;year variable is divisible only by 4 and not 100.
  print("Leap Year")
else:
  print("Not a Leap Year") 

  #If given year is century year then it is divisible by 400

  #If given year is not a century year then it is divisible by 4

          # or
'''year = int(input("Enter a year="))
if(year%100==0 and year%400==0):
  print("Leap Year")
elif(year%100!=0 and year%4==0):
  print("Leap year")
else:
  print("Not a Leap Year") '''