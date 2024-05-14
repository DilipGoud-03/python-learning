

# get Output 
print ("____________Get Output______________ \n")

print("Hello World"),

# Variable Assigning 

x=2     # x will be 2
y=3     # y will be 3
z=x+y   # z will be 5
print(z),  


# Variable names 
print (" \n____________Variable names ______________ \n")

# 1 camal case 

firstWord='Hello this camal case variable name'

# 2 Pascal case variable name 

FirstWord= 'Hello this is Pascal case variable name'

# 3 snack Case variable name 

first_word = 'Hello this is snack case variable name '

#  look all variable is different because python is case senstive 
#  1 camal case 

print (firstWord)

# 2 pascal case 

print(FirstWord)

# 3 snack case

print (first_word)

# Python Variable Value 
print (" \n____________Python Variable Value ______________ \n")
# 1 Multiple variable to multiple value

firstWords,SecondWords,third_word = firstWord ,FirstWord , first_word

print("First Word = " +firstWord)
print ("Second word = " + SecondWords )
print ("Third word = " + third_word)


# 2 One value to multiple variable

x=y=z = "This Value have multiple variable"

print ( "x : "+x)
print ("y : "+y)
print ("z : "+z)

# 3 Unpacked values

fruits = [ 'Banana','Mango','Orange']
x , y , z =fruits

print("x : "+ x)
print("y : "+ y)
print("z : "+ z)


#  output of variable print () 
print("output of variable print ()")

print(x,y,z)

x=10
y=("times")

print (x,y)


#  Global Variable

# x = "awesome"   # this is Global Varible

def myfunc():
  global x
  x = "fantastic"
  print("Inside the Funtion : Python is " + x)

myfunc() 

print ("outside the Funtion : Python is " + x)


#  Variable Exercise
print (" \n____________Variable Exercise ______________ \n")

# Create a variable named carname and assign the value Volvo to it.
carname ='Volo'
print(carname)

# Create a variable named x and assign the value 50 to it.
x=50
print (x)

# Display the sum of 5 + 10, using two variables: x and y.
x=5
y=10
print (x+y) 

# Create a variable called z, assign x + y to it, and display the result. 
x=5
y=10
z=x+y
print(z)

# Insert the correct syntax to assign values to multiple variables in one line: 
x, y ,z = "Orange", "Banana", "Cherry"
print (x,y,z)



# Insert the correct syntax to assign the same value to all three variables in one code line.
x = y = z = "Orange"
print (x,y,z)

# Insert the correct keyword to make the variable x belong to the global scope. 
def myfunc():
    global x 
    x = "fantastic"




# Python Operators
print (" \n_________Python Operators _________ \n")

# 1 Python Arithmetic Operators
print (10+9)
print(10-9)
print(10*9)
print(10/9)
print(10%9)
print(10**9)
print(10//9)

# 2 Python Assignment Operators

x = 5
# x = 3
print(x :=3)