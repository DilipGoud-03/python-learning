# Python string 
print (" \n____________Python string______________ \n")

print ("Hello this is string")
print("It's alright")

# assigning variable

x="Hii Dilip"
print (x)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

# string as array 

a = 'Dilip','Goud'
print (a[1])

# Looping trough the string 

for x in "Banana" :
   print(x)


# string lenght

a ="Hello Dilip"

print (len(a))

txt  = "Hello check the word exist or not"

if "Hello" not in txt :
   print ("Yes, this is not present ")
else :
   print ("No, this is present ")


# String Slicing 

print (" \n___________String Slicing____________ \n")
# print (variable[starting point:ending point])

b = "Hello , World"
print(b[0:5])
print(b[-2:-5])
print(b[8:])
print(b[:13])


#  Modify String 

print (" \n_________Modify String__________ \n")

a = "hello this is new string"
print(a.upper())
print(a.capitalize())
a = "HELLO THIS IS NEW STRING"
print(a.lower())

# strip()
a = "    hello this is new string"
print (a.strip())

# replace 
a = "hello this is new string"

b = a.replace('hello', 'Hii')
print (b)

c =a.split (" ")
print (c)


# Formate String 
print (" \n_____________Formate String _______________ \n")

age = 22
txt =f"Hii my age is : {age}"
print (txt)


price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt =f"It is very {'Expencive' if price >49 else 'cheap'}"
print (txt)

