import pandas as pd
import numpy as np

from domains.student_class import student 
from domains.course_class import course

class stu_list:
    mark_dict = {}    
    
    def __init__(self,s : list[student] ,c : list[course]):
        self.student_list=s
        self.course_list=c
        
        
    #get id student_list

    
    '''
    method to display information about list using pandas 
    '''                 
    def display(self):
        self.student_list.sort()
        data_stu={'id':[ student.get_id() for student in self.student_list ],
                  'name':[student.get_name() for student in self.student_list],
                  'DoB':[student.get_dob for student in self.student_list]}
        df=pd.DataFrame(data=data_stu,columns=["id","name","DoB"])  
        print(df.to_string(index=False))
    #sort student id in ascending order 
    def sort_id(self):
        #seperate number in student id and sort in ascending order
        self.student_list.sort()
        pass
    
 
    # Driver code
  
    #sortStringArray(s, a, n)    
        
    def avg_gpa(self):
        mark_matrix=[]
        credit_matrix=[]
        self.student_list.sort()
        for student in self.student_list: #get mark matrix
            mark_matrix.append([self.mark_dict[sub][student.get_id()-1]for sub in self.mark_dict]) #get mark of student from mark_dict
        
        for course in self.course_list: #get credit matrix
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
        
        data_stu={'id':[ student.get_id() for student in self.student_list ],
                  'name':[student.get_name() for student in self.student_list],
                  'DoB':[student.get_dob() for student in self.student_list],
                  'Average':self.avg_gpa()}
        df_stu=pd.DataFrame(data=data_stu,columns=["id","name","DoB","Average"])
        df_mark=pd.DataFrame(data=self.mark_dict)
        df_full=pd.concat([df_stu,df_mark],axis=1)  #axis=1 means join by columns  
        print(df_full.to_string(index=False))    