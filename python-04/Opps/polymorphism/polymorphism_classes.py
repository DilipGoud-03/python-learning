# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()

class Car :
    def __init__(self,brand,model) -> None:
        self.brand =brand
        self.model =model
    
    def move(self) :
        print (f"Your Car name is {self.brand} and its model  {self.model}")

class Boat :
    def __init__(self,brand,model) -> None:
        self.brand =brand
        self.model =model
    
    def move(self) :
        print (f"Your Boat name is {self.brand} and its model  {self.model}")
    
class Plane :
    def __init__(self,brand,model) -> None:
        self.brand =brand
        self.model =model
    
    def move(self) :
        print (f"Your Plane name is {self.brand} and its model  {self.model}") 
    

car = Car ("Thar","Mahindra")
boat = Boat ("Kive","sonar")
plane = Plane ("UA","American")

for x in (car,boat,plane) :
    x.move()

