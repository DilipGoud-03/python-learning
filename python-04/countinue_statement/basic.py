# Python code to show example of continue statement  

# Printing numbers from 10 to 20 except 15 can be done using continue statement and for loop. The following code is an example of the above scenario:

# looping from 10 to 20  
def looping_from_10_to_20():
    for iterator in range(10, 21):  
   
    # If iterator is equals to 15, loop will continue to the next iteration  
        if iterator == 15:  
            continue  
        # otherwise printing the value of iterator  
        print( iterator )  

#  String  in for loop
def string_trough_while_loop () :
    string ="HelloDilip"
    i =0
    while i <= len(string) :
        if string[i] == "D" :
            continue
        print(string[i])
        i +=1

string_trough_while_loop()