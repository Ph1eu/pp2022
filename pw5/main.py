import input, output


def main():
    input.input_student()
    input.input_course()
    for i in range(len(input.input_course_list)) :
        input.input_mark()
    output.display_student_list()
    output.display_w_mark()
    output.display_course_list()
    
main()    