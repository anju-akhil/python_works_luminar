tummy_size=int(input("Enter tummy size:"))
buttock_size=int(input("Enter buttock size:"))
gender=input("Enter gender:")
measurement=tummy_size/buttock_size
val=round(measurement,2)
print(val)
"""if(val<=0.80)and(gender=="women"):
    print("Health risk is LOW")
    print("Body shape is PEAR")
elif(val<=0.85)and(gender=="women"):
    print("Health risk is MODERATE")
    print("Body shape is AVOCADO")
elif(val>=0.85)and(gender=="women"):
    print("Health risk is HIGH")
    print("Body shape is APPLE")

elif(val<=0.95)and(gender=="men"):
    print("Health risk is LOW")
    print("Body shape is PEAR")
elif(val<=1.0)and(gender=="men"):
    print("Health risk is MODERATE")
    print("Body shape is AVOCADO")
elif(val>=1.0)and(gender=="men"):
    print("Health risk is HIGH")
    print("Body shape is APPLE")
"""
if gender=="male":
    if(val<0.95):
        print("Health risk is LOW")
        print("Body shape is PEAR")
    elif(val<1.0):
        print("Health risk is MODERATE")
        print("Body shape is AVOCADO")
    else:
        print("Health risk is HIGH")
        print("Body shape is APPLE")
elif gender=="female":
    if(val<0.80):
        print("Health risk is LOW")
        print("Body shape is PEAR")
    elif(val<0.85):
        print("Health risk is MODERATE")
        print("Body shape is AVOCADO")
    else:
        print("Health risk is HIGH")
        print("Body shape is APPLE")
else:
    print("please enter valid gender")
