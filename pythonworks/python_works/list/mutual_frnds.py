#list mutual friendname nivin compared with fahad
nivin_frnds=["mohanlal","fahad","unni"]
fahad_frnds=["mohanlal","mamooty","unni"]

mutual_lst=[]
for i in nivin_frnds:
    if i in fahad_frnds:
        mutual_lst.append(i)
print("Mutual friends:",mutual_lst)
