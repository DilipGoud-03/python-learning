class Vahical():
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model
    
    def move (self) :
        print("Your car can move")
        print(f"your Car name is {self.brand} and it model is {self.model}\n")


class Car(Vahical):
    pass
    
class Boat(Vahical):
    def __init__(self, brand, model) -> None:
        super().__init__(brand, model)
   
    def move(self):
        print("Your boat can swim")
        print(f"your Boat name is {self.brand} and it model is {self.model}\n")

class Plane(Vahical):
    def __init__(self, brand, model) -> None:
        super().__init__(brand, model)
   
    def move(self):
        print ("Your can plane can fly")
        print(f"your Plane name is {self.brand} and it model is {self.model}\n")
        
car = Car("Toyta", "Suzuki")
boat = Boat("IndianShip","Indian")
plane = Plane("Rifel","Gun")

for x in (car,boat,plane) :
    x.move()