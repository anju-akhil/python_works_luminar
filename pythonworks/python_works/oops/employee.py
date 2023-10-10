class Employee:
    id:int
    name:str
    department:str
    gender:str
#-------------------20 ravi  hr  male
    def create(self,id,name,dept,gender):
        #initializing attributes
        self.id=id
        self.name=name
        self.department=dept
        self.gender=gender
    def display_emp(self):
        print(self.id,self.name,self.department,self.gender)

obj=Employee()
obj.create(1000,"hari","hr","male")
obj.display_emp()