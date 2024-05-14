
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# fisrt we import module
from modules import *

def sum () :
    number1 = int(input('Enter any number1 : '))
    number2 = int(input('Enter any number2 : '))
    sum = sums(number1,number2)
    print (f"The sum of {number1 , number2} is : {sum}")
    select_option()

def substract () :
    number1 = int(input('Enter any number1 : '))
    number2 = int(input('Enter any number2 : '))
    substract = substracts(number1,number2)
    print (f"The substract of {number1 , number2} is : {substract}")
    select_option()


def multiplication () :
    number1 = int(input('Enter any number1 : '))
    number2 = int(input('Enter any number2 : '))
    multiplication = multiplications(number1,number2)
    print (f"The multiplication of {number1 , number2} is : {multiplication}")
    select_option()


def devision () :
    number1 = int(input('Enter any number1 :  : '))
    number2 = int(input('Enter any number2 :  : '))
    devision = devisions(number1,number2)
    print (f"The devision of {number1 , number2} is : {devision}")
    select_option()

def square():
    number1 = int(input('Enter any number : '))
    square = squares(number1)
    print (f"The square of {number1} is : {square}")
    select_option()

def day () :
    year = int(input('Enter your born year : '))
    month = int(input('Enter your born month  number : '))
    date = int(input('Enter your born date number :  : '))
    day = day_name(year,month,date)
    print (f"your date of birth Date : {date} - {month} - {year} and  your  born Day : {day}")
    select_option()

def select_option():
    print("\t")

    print (
    """
    1. To Sum
    2. To Subtract
    3. TO Multiply
    4. To Division
    5. To Squre
    6. To Know your Born Day
    7. To Exit
    """)

    print("\t")
    option = input ('Enter any one of above option : ')
    print("\t")

    if option == "1":
        print("\t")
        sum()
    elif option == "2" :
        print("\t")
        substract()
    elif option == "3" :
        print("\t")
        multiplication()
    elif option == "4" : 
        print("\t")
        devision()
    elif option == "5" :
        print("\t")
        square()
    elif option == "6" :
        day()
    elif option == "7" :
        exit
    else :
        select_option()

select_option()