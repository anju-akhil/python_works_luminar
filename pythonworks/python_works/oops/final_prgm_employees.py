class Employee:
    data=[
        {"id":1,"name":"jhon","dept":"hr","salary":34000},
        {"id":2,"name":"hari","dept":"it","salary":24000},
        {"id":3,"name":"ravi","dept":"qa","salary":64000},
        {"id":4,"name":"vijay","dept":"hr","salary":74000},
        {"id":5,"name":"tom","dept":"it","salary":24000},
        {"id":6,"name":"vipin","dept":"qa","salary":14000},
    ]   

#-1---------print all data-------------------------
    def get(self,*args,**kwargs):
        return self.data
    
#-2---------return one employee details------------
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[emp for emp in self.data if emp.get("id")==id ][0]
        return record
    
#-3---------add data-------------------------------
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

#-4---------remove one-----------------------------
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        des=[e for e in self.data if e.get("id")==id].pop()  # .pop() used to remove []
        self.data.remove(des)

#-5---------updation-------------------------------
    def updation(self,id=None,*args,**kwargs):
        id=id
        obj=[emp for emp in self.data if emp.get("id")==id][0]
        obj.update(kwargs)
        print("employee object updated")

obj=Employee()
#print(obj.get())

#print(obj.retrieve(id=2))

#obj.create(id=7,name="sam",dept="hr",salary=28000)
#print(obj.get())

#obj.destroy(id=5)
#print(obj.get())

obj.updation(id=2,salary=15000)
print(obj.retrieve(id=2))
