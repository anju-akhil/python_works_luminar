foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":440,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},

]

#--------------------total number of items
print(len(foods))
print("--------------------------")

#---------------- print name whose category = veg
veg_filter=[i.get("name")for i in foods if i.get("category")=="veg"]
print("veg=",veg_filter)
print("--------------------------")

#----------------------- food names available under rs 100
price_filter=[i.get("name")for i in foods if i.get("price")<=100]
print("foods rate <100=",price_filter)
print("--------------------------")

#-------------------------- costly item
costly=max(foods,key=lambda i:i.get("price"))
print("costly product=",costly)
print("-----------")

# ------------------------costly non-veg food
non_vegf=[i for i in foods if i.get("category")=="non-veg"]
costly=max(non_vegf,key=lambda i:i.get("price"))
##single line code-----> non_veg=max(foods,key=lambda i:i.get("category")=="non-veg" and i.get("price"))
print("non_veg",costly)
print("---------------------")

#---------print all categories
categories={i.get("category")for i in foods}
print("categories=",categories)