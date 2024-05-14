# x=20
try :
    print(x)
except:
    print("Exception Error Occor")


try :
    print(x)
except NameError :
    print("Variable x is not define")
except:
    print("Variable else went wrong")


try :
    print ("Hello")
except :
    print("Something went wrong ")
else:
    print("Nothing went wrong")



try:
  f = open("python-05/try...except/demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  


x=-1

if x<0:
   raise Exception("Sorry no number below zero")