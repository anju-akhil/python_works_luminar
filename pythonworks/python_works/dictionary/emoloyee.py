employee={"name":"Anju","age":"25","id":1024,"designation":"software engineer"}
#print(employee["designation"])
#print(employee["name"])
#print(employee["id"])
#print(employee["age"])

#-------check whether key is present-------
if("designation" in employee):
    print("present")
else:
    print("not present")

#------adding new key and value-------
employee["salary"]=2000
print(employee["salary"])

#--------update value---------
employee["salary"]+=5000
print(employee)