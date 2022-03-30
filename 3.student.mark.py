
import pandas as pd
import math
import numpy as np
import curses 

from curses import wrapper
from datetime import datetime
class student :  
   
    def __init__(self,i,n,D):
          
        self._id=self.__validate_id(i)
        self._name=self.__validate_name(n)
        self._DoB=self.__validate_Dob(D)
    """
    def set_id(self, i):
         self._id=self.__validate_id(i)
    def set_name(self,n):
        self._name=self.__validate_name(n)
    def set_Dob(self,D):
        self._D=self.__validate_Dob(D)             
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._DoB
    """ 
    '''
    validation method section
    '''    
    def __validate_id(self,i):
        if( i != None ):
            return i
        else:
            raise ValueError(f"invalid id :{i}")
    def __validate_name(self,n):
        if(n !=None ):
            return n
        else:
            raise ValueError("invalid name")
    def __validate_Dob(self,d):
        format = "%d-%m-%Y"
        res = True
        try:
            res = bool(datetime.strptime(d, format))
        except ValueError:
             res = False
             raise ValueError("invalid date")  
        if(res==True):
            return d   
            
    '''
    getter setted method section using property funtion and decorator function
    funtion
    '''           
    @property
    def id(self): 
        return self._id
    @id.setter
    def id(self,i):
        self.__validate_id(i)  
        self._id=i 
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,n):
        self.__validate_name(n)
        self._name=n 
    @property
    def DoB(self):  
        return self._DoB        
    @DoB.setter
    def DoB(self,d):  
        self.__validate_Dob(d)           
        self._DoB=d
       
class course :
    def __init__(self,i,n,c):     
        self._course_id=i
        self._course_name=n 
        self._course_credit=c 
    '''
    validation method section
    '''     
    def __validate_id(self,i):
        if( i != None and i.isnumeric() ):
            return i
        else:
            raise ValueError(f"invalid course id :{i}")
    def __validate_name(self,n):
        if(n !=None ):
            return n
        else:
            raise ValueError("invalid course name")
    def __validate_credit(self,c):
        if( c != None and c.isnumeric() ):
            return c
        else:
            raise ValueError(f"invalid course credit :{c}")        
    '''
    getter setted method section using property funtion and decorator function
    funtion
    '''      
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def course_name(self):
        return self._course_name 
    
    @property
    def course_credit(self):
        return self._course_credit
    @course_id.setter
    def course_id(self, i):
        self.__validate_id(i)
        self._course_id=i   
    
    @course_name.setter
    def course_name(self,n):
        self.__validate_name(n)
        self._course_name=n 
    
    @course_credit.setter
    def course_credit(self,c):
        self.__validate_credit(c)
        self._course_credit=c       
class stu_list:
    mark_dict = {}    
    
    def __init__(self,s : list[student] ,c : list[course]):
        self.__student_list=s
        self.__course_list=c
    '''
    method to input information about student to the list
    '''
    def input(self):
        n = int(input("input number of students:"))
        while (n != 0):         
            id =int(input("input id for student:"))
            name = input("input name for student:")
            dob = input("input dob for student")
            for students in self.__student_list:
                if(students.id == id):
                    print("student id already exists!please re-enter")
                    continue         
                
            self.__student_list.append(student(id,name,dob))    
            n -= 1
    '''
    method to display information about list using pandas 
    '''                 
    def display(self):
        data_stu={'id':[ student.id for student in self.__student_list ],
                  'name':[student.name for student in self.__student_list],
                  'DoB':[student.DoB for student in self.__student_list]}
        df=pd.DataFrame(data=data_stu,columns=["id","name","DoB"])  
        print(df.to_string(index=False))
    '''
    method to input mark about student  
    '''
    def input_mark(self):
        
        while True:
            sub = str(input("enter subject: "))
            valid = False
            for course in self.__course_list :
                if sub in course.course_name :
                    valid= True
            if valid == True:
                break
            else:
                print("subject has not been added yet")            
        mark_list=[]
        for students in self.__student_list:
            m = float(input(f"input {sub} mark for student {students.name} with id {students.id} : "))
            m = math.floor(m*10)/10 #round down to 1 decimal place
            mark_list.append(m)       
        self.mark_dict[sub]=[]
        self.mark_dict.update({sub:mark_list})
    def avg_gpa(self):
        mark_matrix=[]
        credit_matrix=[]
        
        for student in self.__student_list: #get mark matrix
            mark_matrix.append([self.mark_dict[sub][student.id -1]for sub in self.mark_dict]) #get mark of student from mark_dict
        
        for course in self.__course_list: #get credit matrix
            credit_matrix.append([course.course_credit]) #get credit of course from course_list
        
        #using numpy to perform matrix multiplication to calculate weighted sum and average gpa
        mark_matrix = np.matrix(mark_matrix)
        credit_matrix = np.matrix(credit_matrix)  
        weight_sum_mat= np.matmul(mark_matrix,credit_matrix)
        #transforming matrix to list
        average = np.true_divide(weight_sum_mat,np.sum(credit_matrix))
        average = np.round(average,decimals=1)
        average.T
        average = np.array(average).flatten()
        '''
       ## for debugging
        print("mark")
        print(mark_matrix)
        print("credit")
        print(credit_matrix)
        print("ava")
        
        print(average)
        '''    
        return average
    '''
    method to display information about student with their mark 
    '''    
    def display_w_mark(self):
        
        data_stu={'id':[ student.id for student in self.__student_list ],
                  'name':[student.name for student in self.__student_list],
                  'DoB':[student.DoB for student in self.__student_list],
                  'Average':self.avg_gpa()}
        df_stu=pd.DataFrame(data=data_stu,columns=["id","name","DoB","Average"])
        df_mark=pd.DataFrame(data=self.mark_dict)
        df_full=pd.concat([df_stu,df_mark],axis=1)  #axis=1 means join by columns  
        print(df_full.to_string(index=False))        
class course_list:
    def __init__(self,c : list[course]):
        self.course_list=c
    '''
    method to input information about course to the list
    '''    
    def input(self):
        n = int(input("input number of courses:"))
        while (n != 0):         
            id =int(input("input id for course:"))
            name = input("input name for course:")
            cre= int(input("input credit for course"))
            for courses in self.course_list:
                if(courses.course_id == id and courses.course_name == name):
                    print("course already exists!please re-enter")
                    continue         
                
            self.course_list.append(course(id,name,cre))    
            n -= 1
    '''
    method to input information about the course using pandas
    '''        
    def display(self):
        data_course={'id':[ courses.course_id for courses in self.course_list ],
                  'name':[courses.course_name for courses in self.course_list],
                  'credit':[courses.course_credit for courses in self.course_list]}
        df=pd.DataFrame(data=data_course,columns=["id","name","credit"])  
        print(df.to_string(index=False))                                                
if __name__=="__main__": 
    
    #sample data       
    course_list_test=course_list([course(1,'math',3),course(2,'physics',3),course(3,'chemistry',3)])
    student_list_test=stu_list([student(1,'hieu',"16-04-2002"),student(2,'hai',"11-07-2002"),student(3,'son',"1-04-2002")],course_list_test.course_list)
    
    #displat student list 
    student_list_test.display()
    #input mark for each course
    for course in course_list_test.course_list: 
        student_list_test.input_mark()
    #display mark and calculate gpa 
    student_list_test.display_w_mark()
    student_list_test.avg_gpa()
   
   
'''
   for list in [student_list_test , course_list_test]:
       list.input()
       list.display()
   student_list_test.input_mark()
   student_list_test.display_w_mark()
   student_list_test.avg_gpa
'''
'''
Sample output (no curses because i dont think it is necessary) :
 id name        DoB
  1 hieu 16-04-2002
  2  hai 11-07-2002
  3  son  1-04-2002
enter subject: math
input math mark for student hieu with id 1 : 8
input math mark for student hai with id 2 : 9
input math mark for student son with id 3 : 10
enter subject: physics
input physics mark for student hieu with id 1 : 5
input physics mark for student hai with id 2 : 6
input physics mark for student son with id 3 : 7
enter subject: chemistry
input chemistry mark for student hieu with id 1 : 5.99
input chemistry mark for student hai with id 2 : 6.88
input chemistry mark for student son with id 3 : 4.55
 id name        DoB  Average  math  physics  chemistry
  1 hieu 16-04-2002      6.3   8.0      5.0        5.9
  2  hai 11-07-2002      7.3   9.0      6.0        6.8
  3  son  1-04-2002      7.2  10.0      7.0        4.5
'''    
    
  
  