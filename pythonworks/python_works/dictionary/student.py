student={"roll":4,"name":"abi","course":"django"}
print(student["course"])

if "total" in student:
    print("Present")
else:
    print("Not present")

student["grade"]="A"
print(student)