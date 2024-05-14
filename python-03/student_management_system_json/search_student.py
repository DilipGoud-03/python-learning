from student_array import students


name = input("enter your name")

def search_student(name):
    if students :
        for student in students :
            if student["name"]==name :
                print(student)
            else:
                print ("student does not exist")
    else :
        print ("students are empty")
        
search_student(name=name)