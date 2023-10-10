text=input("Enter the text=")
v_count=0
c_count=0
for ch in text:
    if ch in ['a','e','i','o','u']:
        v_count +=1
    else:
        c_count +=1
print("Vowels count=",v_count)

print("Consanant count=",c_count)