def student_grade(name, code_grade, presentation_grade, final_exam_grade):
    final_grade = int(code_grade)*0.4+int(presentation_grade)*0.3+int(final_exam_grade)*0.3
    result = 'the final grade of  '+name+ ' is '+ str(final_grade)
    return result
print(student_grade('Lao_Shuxuan','98','99','97'))