from clsPerson import Person

class Student(Person):
     """Student class inherited from Person
     
     Arguments:
         Person {base class} -- Person class passed in with properties
     """
    def __init__(self, name, emailaddress,student_id, major = "General Education"):
        super(Student,self).__init__(name,emailaddress)
        Student.student_id = student_id
        Student.major = major
