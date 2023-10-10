items=[
    {"id":1,"name":"sugar","price":60,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":0},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":0},
    {"id":5,"name":"potatto","price":55,"avl_qty":0},
    {"id":6,"name":"carrot","price":80,"avl_qty":5},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hide and seek","price":50,"avl_qty":50}
]
#-------------------print all product names
#for i in items:
       #print(i.get("name"))
all_product_names=[i.get("name") for i in items]
print("Product names=",all_product_names)
print("-----------")

#------------------product name available under rs50
#for i in items:
    #if i.get("price")<50:
        #print(i.get("name"))
price_filter=[i.get("name")for i in items if i.get("price")<=50]
print("price <50=",price_filter)
print("-----------")

#-----------------------print total number of products
print(len(items))
print("-----------------")

#-----------------print all in stock product name
#for i in items:
    #if i.get("avl_qty")>0:
        #print(i.get("name"))
in_stock=[i.get("name") for i in items if i.get("avl_qty")>0]
print("in stock product=",in_stock)
print("-----------")

#-----------------product name available in range of rs20 - rs50
#for i in items:
 #   if i.get("price")in range(20,51):
  #      print(i.get("name"))
range_filter=[i.get("name")for i in items if i.get("price")in range(20,51)]
print("range of rs20 - rs50=",range_filter)
print("-----------")

#-------------------costly product
costly=max(items,key=lambda i:i.get("price"))
print("costly product=",costly)
print("-----------")

#-----------sort
sort=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
print("product sort=",sort)
print("-----------")

#-------------------minimum
min=min(items,key=lambda i:i.get("price"))
print("min product=",min)