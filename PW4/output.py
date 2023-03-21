import numpy as np
#Function to display courses
def show_courses():
    import main as m
    for element in (m.courselist):
        print(m.courselist[element].get_id()," ",m.courselist[element].get_name())

#Function to display students
def show_students():
    import main as m
    for Student in m.studentlist:
        print(f"{Student.get_id()} {Student.get_name()} DoB: {Student.get_DoB()}")

#Function to display marks
def show_marks():
    import main as m
    course_id = input("Enter the course ID: ")
    try:
        #check if the inputted course's id exists in courselist
        m.courselist[course_id]
    except:
        print("Invalid course ID")
        return
    for i in range(0,len(m.studentlist),1):   
        try:
            #Search if student's mark exists and if it does then x is the index of mark list to point at
            x= m.studentlist[i].get_courseid().index(course_id)
            print(m.studentlist[i].get_id()," ",m.studentlist[i].get_name()," ",m.courselist[course_id].get_name(),"mark: ",m.studentlist[i].get_mark()[x])
        except:
            print(m.studentlist[i].get_id()," ",m.studentlist[i].get_name()," ",m.courselist[course_id].get_name(),"mark: N/A")

#Function to calculate and display students'GPA
def show_GPA():
    import main as m
    #put studentlist list into numpy array
    npstudentlist = np.array(m.studentlist)
    data = []
    #Convert courselist dict to data list
    for element in (m.courselist):
        data.append(m.courselist[element])
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
    m.quickSort(npstudentlist,0,len(npstudentlist)-1) #Sort student list
    #display student list with GPA
    for Student in npstudentlist:
        print(f"{Student.get_id()} {Student.get_name()} DoB: {Student.get_DoB()} GPA: {Student.get_GPA()}")
