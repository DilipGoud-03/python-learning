# break statement example 
def basic_break_statement() :
    my_list = [1, 2, 3, 4]  
    count = 1  
    for item in my_list:  
        if item == 4:  
            print("Item matched")  
            count += 1  
            break  
    print("Found at location", count)  

#  Print numbers 
def print_numbers () : 
    i = 0;    
    while 1:    
        print(i," ",end=""),    
        i=i+1;    
        if i == 10:    
            break;    
    print("came out of while loop");   

# print table of any number 
def print_table() :
    n = 2  
    while True:  
        i = 1  
        while i <= 10:  
            print("%d X %d = %d\n" % (n, i, n * i))  
            i += 1  
        choice = int(input("Do you want to continue printing the table? Press 0 for no: "))  
        if choice == 0:  
            print("Exiting the program...")  
            break  
        n += 1  
    print("Program finished successfully.")