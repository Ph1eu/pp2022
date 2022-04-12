
import pandas as pd
import input 
import os
cwd = os.getcwd()
print(cwd)

def display_student_list():
        data_stu={'id':[ student.get_id() for student in input.output_student_list.student_list ],
                  'name':[student.get_name() for student in input.output_student_list.student_list],
                  'DoB':[student.get_dob() for student in input.output_student_list.student_list]}
        df=pd.DataFrame(data=data_stu,columns=["id","name","DoB"])  
        print(df.to_string(index=False))
        df.to_csv(cwd+'\students.txt', header=["ID","Name","DoB"], index=None, sep=' ', mode='a')
def display_w_mark():
        
        data_stu={'id':[ student.get_id() for student in input.output_student_list.student_list ],
                  'name':[student.get_name() for student in input.output_student_list.student_list],
                  'DoB':[student.get_dob() for student in input.output_student_list.student_list],
                  'Average':input.output_student_list.avg_gpa()}
        df_stu=pd.DataFrame(data=data_stu,columns=["id","name","DoB","Average"])
        df_mark=pd.DataFrame(data=input.output_student_list.mark_dict)
        df_full=pd.concat([df_stu,df_mark],axis=1)  #axis=1 means join by columns  
        print(df_full.to_string(index=False))
        df_full.to_csv(cwd+'\marks.txt', header=["ID","Name","DoB","Average"]+list(input.output_student_list.mark_dict.keys()), index=None, sep=' ', mode='a')
def display_course_list():
        data_course={'id':[ courses.course_id for courses in input.output_course_list.course_list ],
                  'name':[courses.course_name for courses in input.output_course_list.course_list],
                  'credit':[courses.course_credit for courses in input.output_course_list.course_list]}
        df=pd.DataFrame(data=data_course,columns=["id","name","credit"])  
        print(df.to_string(index=False))        
        df.to_csv(cwd+'\courses.txt', header=["Id","Name","Credit"], index=None, sep=' ', mode='a')   
              