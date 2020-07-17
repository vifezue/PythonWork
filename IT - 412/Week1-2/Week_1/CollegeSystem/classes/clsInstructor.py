from classes.clsPerson import Person
class Instructor(Person):
    """[Instructor Object from passing in the Person and property base class]
    
    Arguments:
        Person {[object]} -- [passes in the base class Person]
    """
    def __init__(self,name,emailaddress,instructor_id, last_institution, highest_degree_earned):
        super(Instructor,self).__init__(name,emailaddress)
        Instructor.instructor_id = instructor_id
        Instructor.last_institution = last_institution
        Instructor.highest_degree_earned = highest_degree_earned



