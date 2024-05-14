
import json

def show_students() :
    f = open("student.json","r")
    students_data = json.loads(f.read())
    for x in students_data :
           print(x)
    f.close()

show_students()
