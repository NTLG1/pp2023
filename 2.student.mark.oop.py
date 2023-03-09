studentlist=[]
courselist={}

class Student():
    def __init__(self):
        self.__id = input("Enter student's id: ")
        self.__name  = input("Enter the student's name: ")
        self.__DoB  = input("Enter student's DoB: ")
        self.__courseid = []
        self.__mark = []

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_DoB(self):
        return self.__DoB
    
    def get_courseid(self):
        return self.__courseid
    
    def get_mark(self):
        return self.__mark
    
    def set_courseid(self, courseid):
        self.__courseid.append(courseid)

    def set_mark(self, mark):
        self.__mark.append(mark)

class Course():
    def __init__(self,id, name):
        self.__id = id
        self.__name  = name
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

def input_students():
    n = int(input("Enter number of student: "))
    for i in range(0,n,1):
        studentlist.append(Student())

def input_courses():       
    coursenum= int(input("Enter the number of course: "))
    for i in range (0,coursenum,1):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courselist[id] = Course(id,name)

def input_marks():
    course_id = input("Enter the course ID: ")
    try:
        courselist[course_id]
    except:
        print("Invalid course ID")
        return
    for i in range(0,len(studentlist),1):
        studentlist[i].set_courseid(course_id)
        mark= int(input("Enter the mark for "+studentlist[i].get_id()+" "+studentlist[i].get_name()+": "))
        studentlist[i].set_mark(mark)

def show_courses():
    for element in (courselist):
        print(courselist[element].get_id()," ",courselist[element].get_name())

def show_students():
    for Student in studentlist:
        print(f"{Student.get_id()} {Student.get_name()} DoB: {Student.get_DoB()}")

def show_marks():
    course_id = input("Enter the course ID: ")
    try:
        courselist[course_id]
    except:
        print("Invalid course ID")
        return
    for i in range(0,len(studentlist),1):   
        try:
            x= studentlist[i].get_courseid().index(course_id)
            print(course_id," ",studentlist[i].get_name()," ",courselist[course_id].get_name(),"mark: ",studentlist[i].get_mark()[x])
        except:
            print(course_id," ",studentlist[i].get_name()," ",courselist[course_id].get_name(),"mark: N/A")

input_students()
input_courses()
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