from classes.clsPerson import Person
from classes.clsStudent import Student
from classes.clsInstructor import Instructor
from classes.clsValidator import *
from functions.getStudentInfo import get_StudentInfo
from functions.getInstructorInfo import get_InstructorInfo
from functions.displayInformation import display_information
from functions.addIndividual import enter_decision



print("::::::Welcome to our College Information Database:::::::")
collegeRecord = []
notfinished = True
while notfinished: 
        individual = Validator.enter_person_type()
        individual = str(individual).strip()
        if individual == "S":
           myStudent = get_StudentInfo()
           collegeRecord.append(myStudent)
        else:
            myInstructor = get_InstructorInfo()
            collegeRecord.append(myInstructor)
        response = enter_decision()
        if response == "N":
            display_information(collegeRecord)
            print("Goodbye!")
            break
        else:
            continue


        
