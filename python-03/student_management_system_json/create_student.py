
import json
# student inputs records
name = input("enter your name")
age = input ("enter your age")
grade = input("enter your grade")


# Data to be written


f = "student.json"

def create_student() :
    with open(f,'r+') as file:
        file_data = json.load(file)
        if file_data :
            id= len(file_data)+1
            
        new_data = {
                    "id":id,
                    "name": name,
                    "age": age,
                    "grade": grade,
                    }
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        print(f"Hello mr. {name} you info has inserted successful")

create_student()