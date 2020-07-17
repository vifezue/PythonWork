def display_information(list):
    """Display the Object (Student,Instructor) information
    
    Arguments:
        list {object} -- Passes in the object type
    """
    for object in list:
        if isinstance(object,Student):
            print("Student Name: "+ object.name)
            print("Student Major: "+ object.major)
            print("Student Email: "+ object.emailaddress)
            print("Student ID: "+ object.student_id)
        else:
            print("Instructor Name:" + object.name)
            print("Instructor Email:" + object.emailaddress)
            print("Instructor ID:" + object.instructor_id)
            print("Instructor ID:" + object.last_institution)
            print("Instructor ID:" + object.highest_degree_earned)