import pandas as pd

from domains.course_class import course
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