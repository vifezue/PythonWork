from clsPerson import Person
"""Instructor class with inheritance from Person
"""
class Instructor(Person):
    #INSTRUCTOR CLASS
    def __init__(self,name,emailaddress,instructor_id, last_institution, highest_degree_earned):
        super(Instructor,self).__init__(name,emailaddress)
        Instructor.instructor_id = instructor_id
        Instructor.last_institution = last_institution
        Instructor.highest_degree_earned = highest_degree_earned



