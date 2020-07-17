from classes.clsPerson import Person

class Student(Person):
    """[Student Class Constructor]
    
    Arguments:
        Person {object} -- [Passes in the Person base class]
    """
    def __init__(self, name, emailaddress,student_id, major = "General Education"):
        super(Student,self).__init__(name,emailaddress)
        Student.student_id = student_id
        Student.major = major
