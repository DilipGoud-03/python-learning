import json
from books import Books
import datetime 

class Members:

# 2 Add a new Member
    def add_new_members () :
        try : 
            f ="simple_library_management_system/members.json"
            try :    
                with open(f,'r+') as file:
                    first_name  = input("Enter Member first name : ")
                    last_name  = input("Enter Member last name : ")
                    age  = input("Enter Member age : ")
                    file_data = json.load(file)
                    id = 1
                    addedAt= datetime.datetime.now()
                    if file_data :
                        id= len(file_data)+1

                    new_data = {
                                "id":id,
                                "first_name":first_name,
                                "last_name":last_name,
                                "age":age,
                                "addedAt" : str(addedAt.date())
                                }
                    file_data.append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent = 7)
                    print(f"{first_name} {last_name} member has inserted successfully")
            except :
                print("Error to write data in file")
        except :
            print("Error to open file")
        Books.switch_function()

# 3 View all members
    def view_all_members () :
        try :
            f = open("simple_library_management_system/members.json","r+")
            try:
                meembers = json.load(f)
                print("\t")
                print("Available meembers are - ")
                for x in meembers :
                    print(x)
            except:
                print("Unable to load file")
        except :
            print ("Unable to open file")
        Books.switch_function()



