"""
Continuing with the previous scenario, a student eligible for admission has to choose a course and pay the fees for it. If they have scored more than 85 marks in qualifying exam, they get 25% discount on fees.

Valid course ids and fees are given below:

course id      fees

1001         25575.0

1002        15500.0

Extend the program written in the previous assignment to include the above requirement.

Instance variables and methods to be included in Student class are given below.
"""

dict={1001:	25575.0, 1002:15500.0}

class Student:
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
        self.__course_id=None
        self.__fees=None
    
    def get_course_id(self):
        return self.__course_id
                
    def get_fees(self):
        return self.__fees
                
    def choose_course(self,course_id):
        if course_id in dict.keys():
            self.__course_id=course_id
            self.__fees=dict[course_id]
            
            if self.__marks>85:
                self.__fees=0.75*self.__fees
                return True
            else:
                return True
        else:
            return False
                
        
    def validate_marks(self):
        if self.__marks in range(0,101):
            return True
        else:
            return False
            
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    
    def check_qualification(self):
        if self.validate_marks()==True and self.validate_age()==True:
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False
            
            
    def set_student_id(self,student_id):
        self.__student_id=student_id
        
    def set_marks(self,marks):
        self.__marks=marks
    
    def set_age(self,age):
        self.__age=age
        
    
        
    def get_student_id(self):
        return self.__student_id
        
    def get_marks(self):
        return self.__marks
        
    def get_age(self):
        return self.__age
    


maddy=Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(89)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
    
        
