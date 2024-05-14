# Tupple Basic
firstTupple = ("apple","banana","orange")
print (firstTupple)

# Tupple allow duplicate items 
secondTupple = ("apple","banana","orange","banana")
print(secondTupple)

# Find type of seconTuple variable
print (type(secondTupple))

# Access tupple 
print(secondTupple[1])

# This example returns the items from the beginning to, but NOT included, "orange":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:3])

# Check data present in tupple
fourthTupple = ("apple", "banana", "cherry")
if "apple" in fourthTupple:
  print("Yes, 'apple' is in the fruits tuple") 

