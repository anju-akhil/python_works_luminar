#suggestions for nivin

all_users=["mohanlal","fahad","unni","mamooty","nivin","dq"]
nivin_frnds=["mohanlal","fahad","unni"]

suggetion_lst=[]
for i in all_users:
    if i not in nivin_frnds:
        suggetion_lst.append(i)
suggetion_lst.pop(suggetion_lst.index("nivin"))
print(suggetion_lst)