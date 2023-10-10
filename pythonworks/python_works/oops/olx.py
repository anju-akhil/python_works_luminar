class Olx:
    vehicles=[
        {"id":1,"name":"passionpro","year":2010,"selling_price":34000,"color":"black","location":"ekm"},
        {"id":2,"name":"cbz","year":2015,"selling_price":28000,"color":"red","location":"tsr"},
        {"id":3,"name":"alto","year":2000,"selling_price":100000,"color":"silver","location":"tsr"},
        {"id":4,"name":"reclassic350","year":2018,"selling_price":120000,"color":"grey","location":"ekm"},
        {"id":5,"name":"activa","year":2010,"selling_price":24000,"color":"black","location":"ekm"},
        {"id":6,"name":"herohondasd","year":2000,"selling_price":80000,"color":"red","location":"tsr"},
    ]

#-1----------------add-------------------------------    
    def create(self,*args,**kwargs):
        self.vehicles.append(kwargs)
        print("Vehicle added successfully")
        return kwargs
    
#-2----------------list-------------------------------
    def get(self,*args,**kwargs):
        return self.vehicles
    
#-3----------------retrieve one item------------------
    def retrieve(self,id=None,*args,**kwargs):
        obj=[veh for veh in self.vehicles if veh.get("id")==id][0]
        return obj
    
#-4-----------------remove one------------------------
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        des=[e for e in self.vehicles if e.get("id")==id].pop()  # .pop() used to remove []
        self.vehicles.remove(des)
        print("Item deleted")

#-5---------updation-------------------------------
    def updation(self,id=None,*args,**kwargs):
        id=id
        obj=[emp for emp in self.vehicles if emp.get("id")==id][0]
        obj.update(kwargs)
        print("vehicle object updated")

obj=Olx()

#  1
#print(obj.create(id=7,name="nano",year=2000,selling_price=24000,color="yellow",location="tvm"))

#  2
#print(obj.get())

#  3
#print(obj.retrieve(id=2))

#  4
#obj.destroy(id=2)
#print(obj.get())

#  5
obj.updation(id=2,color="white")
print(obj.retrieve(id=2))
