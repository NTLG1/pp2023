import math
import numpy as np

studentlist=[]
courselist={}

#Create a class Student that contains student's information
class Student():
    def __init__(self):
        self.__id = input("Enter student's id: ")
        self.__name  = input("Enter the student's name: ")
        self.__DoB  = input("Enter student's DoB: ")
        self.__GPA = 0
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
    
    def get_GPA(self):
        return self.__GPA
    
    def set_courseid(self, courseid):
        self.__courseid.append(courseid)

    def set_mark(self, mark):
        self.__mark.append(mark)

    def set_GPA(self, GPA):
        self.__GPA = GPA

#Create a class Course that contains course's information
class Course():
    def __init__(self,id, name, credit):
        self.__id = id
        self.__name  = name
        self.__credit = credit
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_credit(self):
        return self.__credit

#Function to enter students' information
def input_students():
    n = int(input("Enter number of student: "))
    for i in range(0,n,1):
        #Put all inputted students' information into studentlist list
        studentlist.append(Student())

#Function to enter courses' information
def input_courses():       
    coursenum= int(input("Enter the number of course: "))
    for i in range (0,coursenum,1):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = float(input("Enter course credit: "))
        #Put all inputted courses' information into courselist dict with index is the id of the course
        courselist[id] = Course(id,name,credit)

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
        studentlist[i].set_courseid(course_id)
        mark= float(input("Enter the mark for "+studentlist[i].get_id()+" "+studentlist[i].get_name()+": "))
        mark = math.floor(mark*10)/10 #round-down student scores to 1-digit using floor()
        studentlist[i].set_mark(mark)

#Function to display courses
def show_courses():
    for element in (courselist):
        print(courselist[element].get_id()," ",courselist[element].get_name())

#Function to display students
def show_students():
    for Student in studentlist:
        print(f"{Student.get_id()} {Student.get_name()} DoB: {Student.get_DoB()}")

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
            x= studentlist[i].get_courseid().index(course_id)
            print(studentlist[i].get_id()," ",studentlist[i].get_name()," ",courselist[course_id].get_name(),"mark: ",studentlist[i].get_mark()[x])
        except:
            print(studentlist[i].get_id()," ",studentlist[i].get_name()," ",courselist[course_id].get_name(),"mark: N/A")
    
#Function to calculate and display students'GPA
def show_GPA():
    #put studentlist list into numpy array
    npstudentlist = np.array(studentlist)
    data = []
    #Convert courselist dict to data list
    for element in (courselist):
        data.append(courselist[element])
    #put data list into numpy array
    npcourselist = np.array(data)
    for Student in npstudentlist:
        #Calculate GPA
        GPA = 0
        credits = 0
        npmark = np.array(Student.get_mark())
        for i in range(0,len(npmark),1):
            for j in range(0,len(npcourselist),1):
                if (npcourselist[j].get_id() == Student.get_courseid()[i]):
                    x=j
                    break
            GPA = GPA + npcourselist[x].get_credit() * npmark[i]
            credits = credits + npcourselist[x].get_credit()
        if len(npmark) == 0:
            credits=1 #if no mark is inputted then credits must not be 0 or else there will be an error divided by 0
        GPA = GPA/credits
        Student.set_GPA(GPA) #Set student's GPA in class Student
    npstudentlist=sorted(npstudentlist,key=lambda x: x.get_GPA(), reverse=True) #Sort student list
    #display student list with GPA
    for Student in npstudentlist:
        print(f"{Student.get_id()} {Student.get_name()} DoB: {Student.get_DoB()} GPA: {Student.get_GPA()}")

input_students()
input_courses()
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
        input_marks()
    elif choice == "2":
        show_courses()
    elif choice == "3":
        show_students()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        show_GPA()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")