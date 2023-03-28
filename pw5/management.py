import os
import zlib

studentlist=[]
courselist={}

#Restore marks in database
def restore_marks():
    if not os.path.exists("marks.txt"):
        f = open("marks.txt", 'x')
    f = open("marks.txt", 'r')
    for line in f:
        index =0
        c = 0
        element=0
        while (True):
            try:
                if line[element]==',':
                    c=c+1
                    if c==1:
                        i = line[index:element]
                        index = element+1
                    if c==2:
                        courseid = line[index:element]
                        index = element+1
            except:
                mark = line[index:element-1]
                mark = float(mark)
                break
            element=element+1
        for j in range(0,len(studentlist),1):
            if studentlist[j].get_id()==i:
                break
        studentlist[j].set_mark(mark)
        studentlist[j].set_courseid(courseid)
    f.close()
#staticmethod
def compressing_files(filename_in, filename_out):
    with open(filename_in, "rb") as fin, open(filename_out, "wb") as fout:
        data = fin.read()
        compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        fout.write(compressed_data)

#staticmethod
def decompressing_files(filename_in, filename_out):
    with open(filename_in, "rb") as fin, open(filename_out, "wb") as fout:
        data = fin.read()
        decompressed_data = zlib.decompress(data)
        fout.write(decompressed_data)

#check if .dat files exist
def check_files():
    if os.path.isfile('./students.dat'):
        decompressing_files("students.dat", "students.txt")
    if os.path.isfile('./courses.dat'):
        decompressing_files("courses.dat", "courses.txt")
    if os.path.isfile('./marks.dat'):
        decompressing_files("marks.dat", "marks.txt")

#compress txt files to .dat
def compress():
    if os.path.exists("students.txt"):
        compressing_files("students.txt", "students.dat")
    if os.path.exists("courses.txt"):
        compressing_files("courses.txt", "courses.dat")
    if os.path.exists("marks.txt"):
        compressing_files("marks.txt", "marks.dat")

#Menu
def Menu():
    import input as ip
    import output as op
    while True:
        compress()
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