def get_StudentInfo():
    """Collects the user input with validation and builds the Student Object
    
    Returns:
        Student -- returns the Student Class after validation
    """
    name = Validator.enter_valid_name()
    email = Validator.enter_valid_email()
    student_id = Validator.enter_valid_student_id()
    major = Validator.enter_student_major()

    myStudent = Student(name,email,student_id,major)
    return myStudent 