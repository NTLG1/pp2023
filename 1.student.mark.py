studentlist=[]
courselist={}

#Function to enter students' information
def input_students():
    n=int(input(("Enter the number of students: ")))
    for i in range(0,n,1):
        #Put all inputted students' information into studentlist list
        studentlist.append({"id":input("Enter student's id: "), "name":input("Enter the student's name: "), "DoB":input("Enter student's DoB: "),"courseid": [], "mark": []})

#Function to enter courses' information
def input_courses():       
    coursenum= int(input("Enter the number of course: "))
    for i in range (0,coursenum,1):
        id =input("Enter course id: ")
        name=input("Enter course name: ")
        #Put all inputted courses' information into courselist dict with index is the id of the course
        courselist[id]={"id":id,"name":name}

#Function to enter students' mark
def input_marks():
    course_id = input("Enter the course ID: ")
    try:
        #check if the inputted course's id exists in courselist
        courselist[course_id]
    except:
        print("Invalid course ID")
        return
    for i in range(0,len(studentlist),1):
        #put mark and course's id information into studentlist
        studentlist[i]["courseid"].append(course_id)
        mark= float(input("Enter the mark for "+studentlist[i].get("id")+" "+studentlist[i].get("name")+": "))
        studentlist[i]["mark"].append(mark)

#Function to display courses
def show_courses():
    for element in (courselist):
        print(courselist[element].get("id")," ",courselist[element].get("name"))

#Function to display students
def show_students():
    for i in range(0,len(studentlist),1):
        print(studentlist[i].get("id")," ",studentlist[i].get("name")," DoB:",studentlist[i].get("DoB"))

#Function to display marks
def show_marks():
    course_id = input("Enter the course ID: ")
    try:
        #check if the inputted course's id exists in courselist
        courselist[course_id]
    except:
        print("Invalid course ID")
        return
    for i in range(0,len(studentlist),1):   
        try:
            #Search if student's mark exists and if it does then x is the index of mark list to point at
            x= studentlist[i]["courseid"].index(course_id)
            print(studentlist[i].get("id")," ",studentlist[i].get("name")," ",courselist[course_id].get("name"),"mark: ",studentlist[i].get("mark")[x])
        except:
            print(studentlist[i].get("id")," ",studentlist[i].get("name")," ",courselist[course_id].get("name"),"mark: N/A")

input_students()
input_courses()
#Menu
while True:
    print("Select an option")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given choice")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_marks()
    elif choice == "2":
        show_courses()
    elif choice == "3":
        show_students()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")