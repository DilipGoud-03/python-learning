# A variable is only available from inside the region it is created. This is called scope.
def fisrtFunction():
    x= 300
    print(f"This is fisrtFunction data {x+1}")
fisrtFunction()

def seconFunction():
    x=300
    print(f"This is Secondfuntion data {x+2}")
    def thirdFunction():
        nonlocal x 
        x = 400
        print(f"This is thirdFunction data {x+3}")
    thirdFunction()
seconFunction()