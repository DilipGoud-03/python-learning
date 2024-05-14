#  python pass statement example 

# datas with for loop 
def for_datas() :
    datas = {1,2,3,4,5,6,7,8,9,}

    for data in datas :
        if data % 2==1 :
            pass
        else :
            print(data)


# datas with while loop 
def while_datas() :
    datas = {1,2,3,4,5,6,7,8,9}
    i=0
    while i < len(datas) :
        if (datas[i] ==5) :
            pass
        print(datas[i])
        i +=1

def strings() :
    strings = {"Hello","Ravi","You","Very","Close"}
    for string in strings :
        if string == "Ravi" :
            pass
        print (string)
        

# while_datas ()
strings ()