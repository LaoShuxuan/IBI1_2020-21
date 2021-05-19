#define a function that can calcualte the total marks of students
def student_grade(name, code_grade, presentation_grade, final_exam_grade):
    final_grade = int(code_grade)*0.4+int(presentation_grade)*0.3+int(final_exam_grade)*0.3
    #show the result
    result = 'the final grade of  '+name+ ' is '+ str(final_grade)
    return result
# give a example
print(student_grade('Lao_Shuxuan','98','99','97'))
