

def count(val):
    v_count=0
    c_count=0
    for ch in range(len(val)):
        if val[ch] in ['a','e','i','o','u']:
            v_count +=1
        else:
            c_count +=1
    print("Vowels count=",v_count)
    print("Consanant count=",c_count)
val=input("Enter the text=")
count(val)