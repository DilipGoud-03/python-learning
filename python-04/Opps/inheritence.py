from classes_object import MyfirstClass

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class ChildClass(MyfirstClass) :
    def __init__(self, name, age ,year):
        super().__init__(name, age)
        self.year =year
    
    def myfunction(self):
        return f"Hello {self.name} your age is {self.age} and you are passed in {self.year} \n"
    
p1 = ChildClass("Dilip", 23,2013)
p2 = ChildClass("Sandeep",24,2015)
p3 = ChildClass("Ranjit",19,2018)

print(p1.myfunction())
print(p2.myfunction())
print(p3.myfunction())