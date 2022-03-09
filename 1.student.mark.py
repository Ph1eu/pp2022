import pandas as pd
student={
    "id": None,
    "name":None,
    "DoB":None,
    "mark":{}
}
course={"course_id":None,
        "name":None}
student_list = []
course_list = []
def add_stu():
    num = int(input("input number of students:"))
    while(num != 0):
        student["id"] = input("input student id:")
        if(student["id"] in student_list or student["id"].isnumeric() == False or student["id"]==None):
            print("student id already exists or wrong type!please re-enter")
            continue
        
        student["name"] = input("input student name:")
        
        student["DoB"] = input("input student DoB(dd/mm/yy):")
        dob=student["DoB"].split("/")
        if( 0<int(dob[0]) <32 and 0<int(dob[1]) <13 and 0<int(dob[2]) <2022):
                if(int(dob[1])==2 and int(dob[0])>29):
                    print("invalid date!please re-enter")
                    continue
                if(int(dob[1])==2 and int(dob[2])%4==0 and int(dob[0])>29):
                    print("invalid date!please re-enter")
                    continue

        student_list.append(student.copy())
        num -= 1
def add_course():
    num = int(input("input number of courses:"))
    while(num != 0):
        course["course_id"] = input("input course id:")
        if(course["course_id"] in course_list or course["course_id"]==None or course["course_id"].isnumeric() == False):
            print("course id already exists or wrong type!please re-enter")
            continue
        course["name"] = input("input course name:")
        course_list.append(course.copy()) 
        num -= 1       
        
def add_mark(course):
    for i in range(len(student_list)):
        mark = input(f"input mark for student id {i+1} for course {course} :")
        student_list[i]["mark"][course]=mark


# print student list with pandas
def print_stu_list():
    df=pd.DataFrame(data=student_list,columns=["id","name","DoB"])
    print(df.to_string(index=False))
    print("\n")  
#print course list with pandas
def print_course_list():
    df=pd.DataFrame(data=course_list,columns=["course_id","name"])
    print(df.to_string(index=False))
    print("\n")  

#print student list with for loop
def print_stu_list_for():    
    for i in range(len(student_list)):
        print("student id:",student_list[i]["id"])
        print("student name:",student_list[i]["name"])
        print("student DoB:",student_list[i]["DoB"])
        print("\n")     
#print course list with for loop
def print_course_list_for():   
    for i in range(len(course_list)):
        print("course id:",course_list[i]["course_id"])
        print("course name:",course_list[i]["name"])
        print("\n")     
#print student mark with a given course
def print_stu_mark(course):
    for i in range(len(student_list)):
        print("student id:",student_list[i]["id"])
        print("student name:",student_list[i]["name"])
        print("course_name:",course)
        print("student mark:",student_list[i]["mark"][course])
        print("\n")        
        
add_stu()
add_course()
add_mark("math")        
print_stu_list()
print_course_list()
print_stu_list_for()
print_course_list_for()
print_stu_mark("math")