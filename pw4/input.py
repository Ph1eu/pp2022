import math

import re 
import datetime
from domains.student_class import student 
from domains.course_class import course

from domains.course_list_class import  course_list
from domains.stu_list_class import stu_list

input_student_list =[]
input_course_list =[]

output_student_list = stu_list(input_student_list,input_course_list)
output_course_list = course_list(input_course_list)




def _validate_stu_id(i):
        return( len(re.findall("B[IA]\\d*-\\d{3}",i))>0)
         
          
def _validate_name(n):
    for s in n:
        if(not s.isalpha()) and (not s.isspace()):
            return False
        else:
            return True 
def _validate_Dob(d):
        format = "%d-%m-%Y"
        res = True
        try:
            res = bool(datetime.datetime.strptime(d, format))
        except Exception:
             res = False
             raise Exception("invalid date")  
        
        return res 
def _repOK_stu(id,name,dob):
    if (_validate_stu_id(id) and _validate_name(name) and _validate_Dob(dob)):
        return True
    else:
        return False
    
def input_student():
        n = int(input("input number of students:"))
        while (n != 0):         
            id =input("input id for student:")
            name = input("input name for student:")
            dob = input("input dob for student")
            for students in input_student_list:
                if (len(input_student_list)== 0):
                    break
                if(students.get_id() == id ):
                    print("student id already exists!please re-enter")
                    continue         
            if(not _repOK_stu(id,name,dob)):
               print("invalid input student infor!please re-enter")
               continue     
            input_student_list.append(student(id,name,dob))    
            n -= 1
 
def input_course():
        n = int(input("input number of courses:"))
        while (n != 0):         
            id =int(input("input id for course:"))
            name = input("input name for course:")
            cre= int(input("input credit for course"))
            for courses in input_course_list:
                if(courses.course_id == id and courses.course_name == name):
                    print("course already exists!please re-enter")
                    continue         
                
            input_course_list.append(course(id,name,cre))    
            n -= 1          
def input_mark():
        
        while True:
            sub = str(input("enter subject: "))
            valid = False
            for course in input_course_list :
                if sub == course.course_name :
                    valid= True
            if valid == True:
                break
            else:
                print("subject has not been added yet")            
        mark_list=[]
        for Student in input_student_list:
            m = float(input(f"input {sub} mark for student {Student.get_name()} with id {Student.get_id() } : "))
            m = math.floor(m*10)/10 #round down to 1 decimal place
            mark_list.append(m)       
        output_student_list.mark_dict[sub]=[]
        output_student_list.mark_dict.update({sub:mark_list})             
            