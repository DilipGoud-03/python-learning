# Python Data Types
print (" \n____________Python Data Types______________ \n")

# Check which type of variable 

print ("== Check which type of variable  ==")

# 1 string type Auto get type
a = "Hello Dilip"
b = 3
c = 2.4
d = 1j
e = ["apple" , "banana" , "mango"]
f = ("apple" , "banana" , "mango")
g = range(10)
h = {1:"id", 2:"Name", 3:"Age"}
i = frozenset({1:"id", 2:"Name", 3:"Age"})
j = True
k = b"hello"
l = bytearray(5)
m = memoryview(bytes(5))
n = None


print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print (type(f))
print (type(g))
print (type(h))
print (type(i))
print (type(j))
print (type(k))
print (type(l))
print (type(m))
print (type(n))

#  Specify data type of any variable
print (" \n____________Specify data type of any variable______________ \n")


a = str("Hello Dilip")
b = int(3)
c = float(2.4)
d = complex(1j)
e = list(("apple" , "banana" , "mango"))
f = tuple(("apple" , "banana" , "mango"))
g = range(10)
h = dict(id="1", Name="Dilip", Age="22")
i = frozenset(("apple" , "banana" , "mango"))
j = bool (5)
k = bytes(5)
l = bytearray(5)
m = memoryview(bytes(5))
n = (None)


print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print (type(f))
print (type(g))
print (type(h))
print (type(i))
print (type(j))
print (type(k))
print (type(l))
print (type(m))
print (type(n))


# Data Type Conversation 
print (" \n____________Data Type Conversation______________ \n")

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 


# Random numbers 
print ("Random numbers")

import random

print (random.randrange(1,10))


# Python Booleans
print (" \n_________Python Booleans_________ \n")
print(10>9)
print(10<9)
print(10==9)

a=10
b=9
if a<b :
   print ("It is True")
else :
   print ('It is False')

print(bool())
print(bool(100))