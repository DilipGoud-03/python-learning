# tupple = (1,2,3,4,5,6,7)
# myItter=iter(tupple)

# print(next(myItter))

# myString = "Banana"
# new = iter(myString)

# print(next(new))

# mytuple = ("apple", "banana", "cherry")

# for x in mytuple:
#   print(x) 

# mystr = "Banana"

# for x in myString:
#   print(x) 


class MyNumbers :
  def __iter__(self):
    self.a =1
    return self
  
  def __next__(self):
    # if self.a <= 10:
        x =self.a
        self.a +=1
        return x
    # else :
    #   raise StopIteration
  


myclass = MyNumbers()

myiter = iter(myclass)

for x in myiter:
  print(x)