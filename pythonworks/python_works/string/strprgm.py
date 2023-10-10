#string =>sequence of character
name="jh jhug gjh iyf hk"

#print(name.casefold())
#print(name.capitalize())    #converts first letter to uppercase
#print(name.count("i"))
#print(name.startswith("gh"))
#print(name.endswith("re"))
#print(name.isalpha())
#print(name.isdigit())
#print(name.isalnum())
#print(name.strip("jhug"))
#print(name.rstrip("hk"))
#print(name.lstrip("hk"))
#print(name.index("j"))


txt="python is a scripting language"
words=txt.split(" ")
for w in words:
    print (w)