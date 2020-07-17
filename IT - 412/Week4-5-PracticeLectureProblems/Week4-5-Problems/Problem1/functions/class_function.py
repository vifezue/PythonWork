def createRecord(courseName, strSemester):
    
    dict = {'course':courseName, 'semester': strSemester}
    print(dict)
    return dict

def validate_str(passedStr):
    """Validates the Course Name string"""   
    passedStr = passedStr.strip()
    
    if passedStr:
        if passedStr.isspace:
            return True
        else:
            return False
    else:
        return False
    
def validate_semester(passedStr):   
    """Validates the semester string"""
    if passedStr:
        if str(passedStr).isnumeric():
            return True
        else:
            return False
    else:
        return False

def getCourseName():
    """Gets the course name"""
    ret_course_name = input("Please enter your course name: ")
    course_name_ok = False
    while not course_name_ok:
        course_name_ok = validate_str(ret_course_name)
        if not course_name_ok:
                ret_course_name = input("Course name was not valid. Please try again: ")
                course_name_ok = validate_str(ret_course_name)
    return ret_course_name

def getSemesterName():
    """Gets the semester name"""
    ret_semester_name = input("Please enter your semester name: ")
    semester_ok = False
    while not semester_ok:
        semester_ok = validate_semester(ret_semester_name)
        if not semester_ok:
                ret_semester_name = input("Semester name was not valid. Please try again: ")
                semester_ok = validate_semester(ret_semester_name)
    return ret_semester_name
