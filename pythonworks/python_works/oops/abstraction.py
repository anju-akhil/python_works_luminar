# Hide and implimentation details

from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

class Swift(Car):
    def start(self):
        print("swift starts")

    def stop(self):
        print("swift stops")

    def accelerate(self):
        print("swift accelerate")

obj=Swift()
obj.start()
obj.stop()
obj.accelerate()