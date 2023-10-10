#body mass index
height_cm=160
weight_kg=99

#height in meter=cm/100
#bmi=(weight(kg)/height(m^2))cm

height_in_m=height_cm/100
bmi=(weight_kg//height_in_m**2)
print("BMI=",bmi)

if(bmi<=19):
    print("Under weight")
elif(bmi<=25):
    print("Normal weight")
elif(bmi<=30):
    print("Over weight")
else:
    print("Obesity")
