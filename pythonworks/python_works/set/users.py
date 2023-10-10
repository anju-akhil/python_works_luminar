#print suggestion for sanju
all_users=["sachin","dhoni","kohli","rohit","sanju","padikkal"]
sanju_following=["padikkal","sachin"]

suggestions=list(set(all_users).difference(set(sanju_following)))
##suggestions.remove("sanju") -----using remove method
sanju_pos=suggestions.index("sanju")
suggestions.pop(sanju_pos)
print(suggestions)