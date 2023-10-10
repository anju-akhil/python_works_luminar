#multiple inheritance

class P1:
    def m1(self):
        print("inside p1 class m1 method")
    
class P2:
    def m1(self):
        print("inside p2 class m2 method")
        
class Child(P2,P1):
    def m3(self):
        print("inside child class m3 method")
        
ch=Child()
ch.m3()
ch.m1()