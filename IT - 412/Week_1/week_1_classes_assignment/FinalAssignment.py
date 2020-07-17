from clsPerson import Person
from clsStudent import Student
from clsInstructor import Instructor
from clsValidator import *

def get_StudentInfo():
    #Collects the user input with validation and builds the Student Object
    name = Validator.enter_valid_name()
    email = Validator.enter_valid_email()
    student_id = Validator.enter_valid_student_id()
    major = Validator.enter_student_major()

    myStudent = Student(name,email,student_id,major)
    return myStudent
    

def get_InstructorInfo():
    #Builds Collects the user input with validation and builds the Instructor Object
    name = Validator.enter_valid_name()
    email = Validator.enter_valid_email()
    instructor_id = Validator.enter_valid_instructor_id()
    last_institution = Validator.enter_last_institution()
    highest_degree_earned = Validator.enter_highest_degree_earned()

    myInstructor = Instructor(name,email,instructor_id,last_institution,highest_degree_earned)
    return myInstructor

def display_information(list):
    #checks for the object type then prints the attributes
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
def enter_decision():
    #gets person type with user input
    enter_decision = True
    while True:
        response = input("Do you wish to add another individual (Y or N)?")
        if response.upper() == "N" or response.upper() == "Y":
            break
        else:
            print("That was not a valid entry. Please re-enter and try again.")
            continue
    return response.upper()

print("::::::Welcome to our College Information Database:::::::")
collegeRecord = []
notfinished = True
while notfinished: 
    #Main Method
        individual = Validator.enter_person_type()
        individual = str(individual).strip()
        if individual == "S":
           myStudent = get_StudentInfo()
           collegeRecord.append(myStudent)
        else:
            myInstructor = get_InstructorInfo()
            collegeRecord.append(myInstructor)
        response = enter_decision()
        #Asks the user to add another user if possible by user input
        if response == "N":
            display_information(collegeRecord)
            print("Goodbye!")
            break
        else:
            continue


        
