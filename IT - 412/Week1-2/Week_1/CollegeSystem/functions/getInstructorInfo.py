def get_InstructorInfo():

    """Builds Collects the user input with validation and builds the Instructor Object
    
    Returns:
        Instructor -- Builds the instructor information
    """
    name = Validator.enter_valid_name()
    email = Validator.enter_valid_email()
    instructor_id = Validator.enter_valid_instructor_id()
    last_institution = Validator.enter_last_institution()
    highest_degree_earned = Validator.enter_highest_degree_earned()

    myInstructor = Instructor(name,email,instructor_id,last_institution,highest_degree_earned)
    return myInstructor