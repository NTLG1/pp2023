import input as ip
import output as op
studentlist=[]
courselist={}

ip.input_students()
ip.input_courses()
#Menu
while True:
    print("Select an option")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given choice")
    print("5. Show student GPA")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ip.input_marks()
    elif choice == "2":
        op.show_courses()
    elif choice == "3":
        op.show_students()
    elif choice == "4":
        op.show_marks()
    elif choice == "5":
        op.show_GPA()
    elif choice == "6":
        exit()
    else:
        print("Invalid choice!")