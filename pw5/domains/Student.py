#Create a class Student that contains student's information
class Student():
    def __init__(self,id,name,DoB):
        self.__id = id
        self.__name  = name
        self.__DoB  = DoB
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