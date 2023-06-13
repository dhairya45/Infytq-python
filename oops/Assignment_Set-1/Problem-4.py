"""
A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if

Age and marks are valid and
Marks is 65 or more
Write a python program to represent the students seeking admission in the university.

"""


class Student:
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
        
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
    
        
