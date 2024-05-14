# Python lists 
print ("________________ Python List __________________")

# How to create list 
fisrtList = ["Apple","Mango","Bannana","Orange","Graps"]
print(f"First List : {fisrtList}")
# Access list item
print (f"Fist item of the list is : {fisrtList[1:3]}")
# check list item is exist or not 
if "Apple" in fisrtList :
    print (f"Yes :{fisrtList[0]} is present ")

# change list item 
fisrtList[1:3] = ["blackcurrant", "watermelon"]
print(fisrtList)

# Add list Item
# This method add new item in the end 

fisrtList.append("Orange")
print(fisrtList)

# Add new item in the specific place
fisrtList.insert(1,"orange")
print(fisrtList)

# Remove Item of the any space the matched item
fisrtList.remove("Orange")
print(fisrtList)

# Remove item of specific place
fisrtList.pop(1)
print(fisrtList)

# for loop through the list item
for x in fisrtList :
    print(x)

# for loop Through the Index Numbers get list item
for i in range(len(fisrtList)):
    print(fisrtList[i])

# while loop through the index number get list item
i=0
while i < len(fisrtList) :
    print(fisrtList[i])
    i=i+1

[print(x) for x in fisrtList]
print(fisrtList)

# List comprehension
newList =[]
for x in fisrtList :
    if "t" in x :
        newList.append(x)
print(f"the new list is : {newList}")

# Python sort list
# This is always accending order
secondList =["Ram","Laxman","Vinod","Ranjit"]
secondList.sort()
print(secondList)

numberList = [100, 50, 65, 82, 23]
numberList.sort()
print(numberList)

# use short list in decending order
numberList.sort(reverse=True)
print(numberList)

def myList (n) :
    return abs(n-50)
numberList.sort(key=myList)
print (numberList)

#  Reverse the list items
numberList.reverse()
print(numberList)


# Python Copy
# Copy list copy method 
thisList = ["apple", "banana", "cherry"]
print (f"This is thisList : {thisList}")
mylist = thisList.copy()
print(f"This is my list : {mylist}")

# copy list list method
thirdList = list(thisList)
print (f"This is thirdList : {thisList}")

# Python Join List 
# Join two list using + operators
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(f"Using + Operator : {list3}")

# Join two list using + operators
for x in list2 :
    list1.append(x)
print(f"Using append method : {list1}")

