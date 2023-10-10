class Cloth:
    data=[
        {"id":1,"name":"skirt","color":"black","price":550},
        {"id":2,"name":"kurti","color":"white","price":780},
        {"id":3,"name":"jeans","color":"blue","price":1050},
        {"id":4,"name":"tshirt","color":"green","price":500},
        {"id":5,"name":"leggings","color":"white","price":350},
    ]   

#-1---------print all data-------------------------
    def get(self,*args,**kwargs):
        return self.data
    
#-2---------return one cloth details------------
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[c for c in self.data if c.get("id")==id ]
        return record
    
#-3---------add data-------------------------------
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

#-4---------remove one-----------------------------
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        des=[c for c in self.data if c.get("id")==id].pop()   # .pop() used to remove []
        self.data.remove(des)

obj=Cloth()
print(obj.get())

#print(obj.retrieve(id=2))

#obj.create(id=6,name="saree",color="yellow",price=3500)
#print(obj.get())

#obj.destroy(id=5)
#print(obj.get())