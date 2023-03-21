from domains.Student import Student
from domains.Course import Course
import math
#Function to enter students' information
def input_students():
    import main as m
    n = int(input("Enter number of student: "))
    for i in range(0,n,1):
        #Put all inputted students' information into studentlist list
        m.studentlist.append(Student())

#Function to enter courses' information
def input_courses():    
    import main as m   
    coursenum= int(input("Enter the number of course: "))
    for i in range (0,coursenum,1):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = float(input("Enter course credit: "))
        #Put all inputted courses' information into courselist dict with index is the id of the course
        m.courselist[id] = Course(id,name,credit)

#Function to enter students' mark
def input_marks():
    import main as m
    course_id = input("Enter the course ID: ")
    try:
        #check if the inputted course's id exists in courselist
        m.courselist[course_id]
    except:
        print("Invalid course ID")
        return
    for i in range(0,len(m.studentlist),1):
        #put mark and course's id information into studentlist
        m.studentlist[i].set_courseid(course_id)
        mark= float(input("Enter the mark for "+m.studentlist[i].get_id()+" "+m.studentlist[i].get_name()+": "))
        mark = math.floor(mark*10)/10 #round-down student scores to 1-digit using floor()
        m.studentlist[i].set_mark(mark)