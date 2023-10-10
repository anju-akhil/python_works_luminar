class Student:
    id:int
    name:str
    age:int
    course:str

    def __init__(self,id,name,age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course
    def display_std(self):
        print(self.id,self.name,self.age,self.course)

    #def __str__(self) ->str:
    def __str__(self):
        return self.name

obj1=Student(1005,"abu",20,"bca")
obj1.display_std()

print(obj1)