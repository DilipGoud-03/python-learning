from students_array import students

# Simple Student Management System
# Add a new student record with fields: name, age, and grade.
def create_student() :
    global students
    name = input("Enter your name : ")
    age = int(input ("Enter your age : "))
    grade = int(input("Enter your grade : "))
    if name and age and grade :
        new_student={"name":name,"age":age,"grade":grade}
        students.append(new_student)
        print("\t")
        print (f"Hello {name} your record submitted successfully")
    else :
        print("\t")
        print ("Fill all filleds")
    switch_functions()

# View all student records.
def show_student() :
    global students
    if students :
        print("Students Records")
        for student in students :
            if student :
                print(student)
    else :
        print("Not have students record")
    switch_functions()

# Update student records.
def update_student() :
    global students
    name = str(input('Enter your name : '))
    if name:
        for student in students :
            if student["name"]== name :
                student["name"]= input("Enter your new name : ")
                student["age"] = int(input ("Enter your new age : "))
                student["grade"]= int(input("Enter your new grade : "))
                print(f"your information has been updated {student}")
    else :
        print("Please enter only string value")
    switch_functions()

# Delete a student record.
def delete_student():
    name = str(input("Enter name: "))
    global students
    for student in students :
        if student["name"]== name :
            print(f"{name} records removed")
            students.remove(student)
    switch_functions()


# Search for a student by name.
def search_student():
    name = input("Enter your name: ")
    global students
    for student in students :
        if student["name"]==name :
            print(student)
    switch_functions()


# Calculate average grade of all students.
def average_grade():
    sum_grade=0
    for student in students :
        sum_grade += student["grade"]
    print(f"Average of students grade is : {sum_grade/len(students)}")
    switch_functions()


# Call the above  methods
def switch_functions():
    print("\t")
    print("""
    1. To create student
    2. To show students
    3. To update student
    4. To delete students 
    5. To search student
    6. To get average grade of students
    7. To exit
    """)
    
    print("\t")
    id =input("Enter you want to do : ")
    if id==str("1"):
        print("\t")
        create_student()
    elif id==str("2"):
        print("\t")
        show_student()
    elif id ==str("3"):
        print("\t")
        update_student()
    elif id == str("4") :
        print("\t")
        delete_student()
    elif id == str("5") :
        print("\t")
        search_student()
    elif id == str("6") :
        print("\t")
        average_grade()
    elif id == str("7") :
        print("\t")
        exit
    else:
        switch_functions()
        
switch_functions()
