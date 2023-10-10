student={"roll":4,"name":"abi","course":"django"}
print(student.get("name"))

#print(student.keys())
for k in student.keys():
    print(k)

print(student.values())

for k,v in student.items():
    print(k,v)
print(student.items())