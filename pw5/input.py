from domains.Student import Student
from domains.Course import Course
import math
import os

#Function to enter students' information and read/write students from/to database
def input_students():
    import management as m
    n = int(input("Enter number of student: "))
    for i in range(0,n,1):
        id = input("Enter student's id: ")
        name = input("Enter the student's name: ")
        DoB = input("Enter student's DoB: ")
        s = id
        l = len(s)
        s = id+","+name+","+DoB
        write_to_txt("students.txt",s,id,l)
    if not os.path.exists("students.txt"):
        f = open("students.txt", 'x')
    f = open("students.txt", 'r')
    for line in f:
        index =0
        c = 0
        element=0
        while (True):
            try:
                if line[element]==',':
                    c=c+1
                    if c==1:
                        id = line[index:element]
                        index = element+1
                    if c==2:
                        name = line[index:element]
                        index = element+1
            except:
                DoB = line[index:element-1]
                break
            element=element+1
        m.studentlist.append(Student(id,name,DoB))
    f.close()

#Function to enter courses' information and read/write courses from/to database
def input_courses():    
    import management as m   
    coursenum= int(input("Enter the number of course: "))
    for i in range (0,coursenum,1):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = float(input("Enter course credit: "))
        cre_str=str(credit)
        s = id
        l = len(s)
        s = id+","+name+","+cre_str
        write_to_txt("courses.txt",s,id,l)
    if not os.path.exists("courses.txt"):
        f = open("courses.txt", 'x')
    f = open("courses.txt", 'r')
    for line in f:
        index =0
        c = 0
        element=0
        while (True):
            try:
                if line[element]==',':
                    c=c+1
                    if c==1:
                        id = line[index:element]
                        index = element+1
                    if c==2:
                        name = line[index:element]
                        index = element+1
            except:
                credit = float(line[index:element-1])
                break
            element=element+1
        m.courselist[id] = Course(id,name,credit)
    f.close()

#Function to enter students' mark and write marks to database
def input_marks():
    import management as m
    course_id = input("Enter the course ID: ")
    try:
        #check if the inputted course's id exists in courselist
        m.courselist[course_id]
    except:
        print("Invalid course ID")
        return
    all_inputted = 1
    for i in range(0,len(m.studentlist),1):
        try:
            #Check if mark for the inputted course is taken or not
            x= m.studentlist[i].get_courseid().index(course_id)
        except:
            all_inputted = 0
            #put mark and course's id information into studentlist
            m.studentlist[i].set_courseid(course_id)
            mark= float(input("Enter the mark for "+m.studentlist[i].get_id()+" "+m.studentlist[i].get_name()+": "))
            mark = math.floor(mark*10)/10 #round-down student scores to 1-digit using floor()
            m.studentlist[i].set_mark(mark)
            mark = str(mark)
            s= str(m.studentlist[i].get_id())+","+course_id+","+mark
            write_to_txt("marks.txt",s,"",0)
    if all_inputted==1:
        print("All marks for this course has been inputted")

#Function to write data to database     
def write_to_txt(filename, content,id, id_length):
    s=""
    with open(filename, 'a') as f, open(filename, 'r') as f_read:
        for line in f_read:
                s = s+ line[0:id_length] + "\n"
        if (filename == "students.txt") and (id not in s):
                f.write(f"{content}\n")
        elif (filename == "students.txt"):
                print(f"Student_id: {id} was already taken")
        elif (filename == "courses.txt") and (id not in s):
                f.write(f"{content}\n")
        elif (filename == "courses.txt"):
                print(f"Course_id: {id} was already taken")
        elif (filename == "marks.txt"):
                f.write(f"{content}\n")
    f.close()
    f_read.close()