class Mobile:
    model:str
    color:str
    brand:str
    price:int

    def __init__(self,model,color,brand,price):
        self.model=model
        self.color=color
        self.brand=brand
        self.price=price
    def get(self):
        print(self.model,self.color,self.brand,self.price)
obj1=Mobile("a57","black","samsung","24000")
obj1.get()