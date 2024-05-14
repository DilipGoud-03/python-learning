id = input("enter id")

def delete_student(id):
    if students :
        for student in students :
            if student["id"]==id :
                students.remove(student)
                print("student has success fully removed")
            print ("student does not exist")
    else :
        print("Student does not exixt")

delete_student(id =id)