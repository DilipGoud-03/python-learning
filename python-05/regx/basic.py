import re

txt = "Python is the most powerfull language"

x = re.search("^Python.*language$",txt)
y = re.findall("th",txt)
z = re.sub("\o" ,"7" , 2)
if x :
    print("Yes , Its available")
else :
    print("No , Its not available")

print(y)
print(z)

