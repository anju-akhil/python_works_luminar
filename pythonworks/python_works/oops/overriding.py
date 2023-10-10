class Bike:
    def start(self):
        print("Kicker start")
    def breaking(self):
        print("Drum break")
class HeroHondaSplender(Bike):
    def start(self):
        print("self start")
    def breaking(self):
        print("abs breaking")

hobj=HeroHondaSplender()
hobj.breaking()