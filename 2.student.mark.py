from datetime import datetime
import pandas as pd

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
    def __init__(self,i,n):     
        self._course_id=i
        self._course_name=n  
    def __validate_id(self,i):
        if( i != None ):
            return i
        else:
            raise ValueError(f"invalid course id :{i}")
    def __validate_name(self,n):
        if(n !=None ):
            return n
        else:
            raise ValueError("invalid course name")    
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def course_name(self):
        return self._course_name 
    @course_id.setter
    def course_id(self, i):
        self.__validate_id(i)
        self._course_id=i   
    @course_name.setter
    def course_name(self,n):
        self.__validate_name(n)
        self._course_name=n   
class stu_list:
    mark_dict = {}    
    
    def __init__(self,s : list[student] ,c : list[course]):
        self.__student_list=s
        self.__course_list=c
        
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
                     
    def display(self):
        data_stu={'id':[ student.id for student in self.__student_list ],
                  'name':[student.name for student in self.__student_list],
                  'DoB':[student.DoB for student in self.__student_list]}
        df=pd.DataFrame(data=data_stu,columns=["id","name","DoB"])  
        print(df.to_string(index=False))
    def input_mark(self):
        
        while True:
            sub = str(input("enter subject"))
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
            m = float(input(f"input {sub} mark for student {students.name} with id {students.id} "))
            mark_list.append(m)       
        self.mark_dict[sub]=[]
        self.mark_dict.update({sub:mark_list})
    def display_w_mark(self):
        
        data_stu={'id':[ student.id for student in self.__student_list ],
                  'name':[student.name for student in self.__student_list],
                  'DoB':[student.DoB for student in self.__student_list],}
        df_stu=pd.DataFrame(data=data_stu,columns=["id","name","DoB"])
        df_mark=pd.DataFrame(data=self.mark_dict)
        df_full=pd.concat([df_stu,df_mark],axis=1)  #axis=1 means join by columns  
        print(df_full.to_string(index=False))        
class course_list:
    def __init__(self,c : list[course]):
        self.course_list=c
    def input(self):
        n = int(input("input number of courses:"))
        while (n != 0):         
            id =int(input("input id for course:"))
            name = input("input name for course:")
            
            for courses in self.course_list:
                if(courses.course_id == id and courses.course_name == name):
                    print("course already exists!please re-enter")
                    continue         
                
            self.course_list.append(course(id,name))    
            n -= 1
    def display(self):
        data_course={'id':[ courses.course_id for courses in self.course_list ],
                  'name':[courses.course_name for courses in self.course_list]}
        df=pd.DataFrame(data=data_course,columns=["id","name",])  
        print(df.to_string(index=False))                                                
if __name__=="__main__":        
   course_list_test=course_list([])
   student_list_test=stu_list([],course_list_test.course_list)

   for list in [student_list_test , course_list_test]:
       list.input()
       list.display()
   student_list_test.input_mark()
   student_list_test.display_w_mark()
      
   #student_list_test.add_stu()
   #student_list_test.display_student_list()
   
   pass
    
    
  
  