class Student:
    def __init__(self, first_name, last_name, undergraduate_programme):
        self.first_name = first_name
        self.last_name =last_name
        self.undergraduate_programme = undergraduate_programme
    def student_information(self):
        return print('The student is ' +self.first_name+' '+self.last_name+' who comes from '+self.undergraduate_programme)

student = Student('Shuxuan', 'Lao', 'BMS')
student.student_information()