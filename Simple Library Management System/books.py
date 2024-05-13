import json
from members import *
import datetime

class Books :
    # 1 Add a new book.
    def add_new_books () :
        try :
            f = "Simple Library Management System/books.json"
            try :    
                book_name = input("Enter books name : ")
                if book_name :
                    with open(f,'r+') as books:
                        books_data = json.load(books)
                        id = 1
                        date = datetime.datetime.now()
                        if books_data :
                            id= len(books_data)+1
                        new_data = {
                                    "id":id,
                                    "name":book_name,
                                    "isChecked": 0,
                                    "addedAt":str(date.date()),
                                    "isCheckedAt" : ""
                                    }
                        books_data.append(new_data)
                        books.seek(0)
                        json.dump(books_data, books, indent = 7)
                        print(f"{book_name} books has inserted successfully")
                    
            except : 
                print("Unable to write file")
        except :
            print("Unable to open file")
        Books.switch_function()

    # 4 View available books.
    def view_available_books () :

        try :
            f = open("Simple Library Management System/books.json","r+")
            books = json.load(f)
            if books :
                print("\t")
                print("Available Books are - ")
                for x in books :
                    if x["isChecked"] == 0 :
                        print(x)
            else :
                print("There is no books available")
        except :
            print ("Something went wrong")
        Books.switch_function()

    # 5 Check in book
    def checked_in_books():

        try :
            f = "Simple Library Management System/books.json"
            library_file = "Simple Library Management System/library.json"
            try :
                print("You want to checked In : ")
                book_name = input("Enter book name  : ")
                member_name = input("Enter member name  : ")

                if book_name and member_name :
                    with open(f,'r+') as book  :
                        book_data = json.load(book)
                        isChecked = 1
                        date = datetime.datetime.now()
                        for x in book_data :
                            if x["name"] == book_name :
                                x["isChecked"] = isChecked
                                x["isCheckedAt"] = str(date.date())
                        book.seek(0)
                        json.dump(book_data, book, indent = 7)

                    with open(library_file,'r+') as library  :
                        library_data = json.load(library)
                        id = 1
                        isChecked=1
                        date = datetime.datetime.now()
                        if library_data :
                            id= len(library_data)+1
                        new_data = {
                                    "id":id,
                                    "book_name":book_name,
                                    "member_name":member_name,
                                    "isChecked": isChecked,
                                    "addedAt":str(date.date()),
                                    }
                        library_data.append(new_data)
                        library.seek(0)
                        json.dump(new_data, library, indent = 7)
                        print(f"{book_name} has checked successfully")
            except : 
                print("Unable to write file")
        except :
            print("Unable to open file")
        Books.switch_function()

    # 6 Check out book
    def checked_out_books():

        try :
            f = "Simple Library Management System/books.json"
            library_file = "Simple Library Management System/library.json"
            try :
                print("You want to checked Out : ")
                book_name = input("Enter book name  : ")
                member_name = input("Enter member name  : ")
                with open(f,'r+') as file:
                    book_data = json.load(file)
                    isChecked = 0
                    for x in book_data :
                        if x["name"] == book_name :
                            x["isChecked"] = isChecked
                            x["isCheckedAt"] = 0
                    file.seek(0)
                    json.dump(book_data, file, indent = 8)

                with open(library_file,'r+') as file:
                    library_data = json.load(file)
                    for x in library_data :
                        if x["book_name"] == book_name and x["member_name"] == member_name :
                            library_data.pop(x)
                    print(f"{book_name} has checked out successfully")
            except : 
                print("Unable to write file")
        except :
            print("Unable to open file")
        Books.switch_function()


    # 7 View checked In books
    def show_checked_books () :

        try :
            f = open("Simple Library Management System/books.json","r+")
            books = json.load(f)
            if books: 
                print("\t")
                print("Checked books - ")
                for x in books :
                    if x["isChecked"] == 1 :
                        print (x)
            else :
                print("No books available")
        except :
            print ("Something went wrong")
        Books.switch_function()

    # switch to any method
    def switch_function ():

        try :
            print("\t")
            print("""
        Library Management system : 
            1. To Add new books
            2. To Add new member
            3. To View all members 
            4. To View all available books
            5. To Check In book
            6. To Check Out book
            7. To View Checked In books
            8. To Exit
                  
            """)
            print("\t")
            choice = input("Enter any one of above option : ")
            if choice == "1" :
                Books.add_new_books()
            elif choice == "2" :
                Members.add_new_members()
            elif choice == "3" :
                Members.view_all_members()
            elif choice == "4" :
                Books.view_available_books()
            elif choice == "5" :
                Books.checked_in_books()
            elif choice == "6" :
                Books.checked_out_books()
            elif choice == "7" :
                Books.show_checked_books()
            elif choice == "8" :
                exit
            else :
                Books.switch_function()
        except:
            print("")
Books.switch_function()
