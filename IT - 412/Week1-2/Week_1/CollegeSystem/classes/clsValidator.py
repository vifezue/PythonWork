class Validator:
    """[Validation class using static Methods]
    
    Returns:
        [string] -- [passes a string or an empty string]
    """
    @staticmethod
    def enter_person_type():
        #gets person type by user input
        accept_entry = True
        while True:
            individual = input("Please enter a S for Student and I for Instructor: ")
            if not individual 
            if individual.upper() == "S" or individual.upper() == "I":
                break
            else:
                print("That was not a valid entry. Please re-enter and try again.")
                continue
        return individual

    @staticmethod
    def is_chars_valid(value,list):
        #Method to check if a passed in value is in a list
        for item in value:
            valid_chars = True
            if item in list:
                valid_chars = False
                break
        return valid_chars


    @staticmethod
    def enter_valid_email():
        """Validates email entry"""
        invalid_email_characters = ["!", '"', "#", "$", "%", "^", "&", "*", "(", ")" "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
        accept_email_entry = True
        while True:
            try:
                email = str(input("Please enter an email: "))
                for item in email:
                    if item in invalid_email_characters:
                        accept_email_entry = False
                        break
                if email == "" or email.isalnum == False or accept_email_entry == False:
                    print("Email was not a valid entry. Please re-enter and try again.")
                    continue
            except ValueError:
                print("Email was not a valid entry. Please re-enter and try again.")
                continue
            else:
                break
        return email

    @staticmethod
    def enter_valid_name():
        """Validates Name Entry"""
        invalid_name_characters = ["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")" "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
        accept_name_entry = True
        while True:
            try:
                name = str(input("Please enter the first and last name: "))
                for item in name:
                    if item in invalid_name_characters:                   
                        accept_name_entry = False
                        break
                if name == "" or accept_name_entry == False:
                    print("Name was not a valid entry. Please re-enter and try again.")
                    continue
            except ValueError:
                print("Name was not a valid entry. Please re-enter and try again.")
                continue
            else:
                break
        #formats the Name string
        strName = name.split(" ",2)
        firstName = strName[0]
        lastName = strName[1]
        name = firstName.capitalize() + " "+ lastName.capitalize()
        return name

    @staticmethod
    def enter_valid_student_id():
        """Validates Student ID Entry"""
        accept_id_entry = True
        while True:
            try:
                ID = str(input("Please enter the identification number: "))
                if ID == "" or len(ID) > 7:
                    print("ID was not a valid entry. Please re-enter and try again.")
                    continue
            except ValueError:
                print("ID was not a valid entry. Please re-enter and try again.")
                continue
            else:
                break
        return ID

    @staticmethod
    def enter_valid_instructor_id():
        """Validates Instructor ID entry"""
        accept_id_entry = True
        while True:
            try:
                ID = str(input("Please enter the identification number: "))
                if ID == "" or len(ID) > 5:
                    print("ID was not a valid entry. Please re-enter and try again.")
                    continue
            except ValueError:
                print("ID was not a valid entry. Please re-enter and try again.")
                continue
            else:
                break
        return ID

    @staticmethod
    def enter_student_major():
        """Validates Student Major Entry"""
        accept_major_entry = True
        while True:
            try:
                major = str(input("Please enter the students major: "))
                if major == "":
                    print("Major was not a valid entry. Please re-enter and try again.")
                    continue
            except ValueError:
                print("Major was not a valid entry. Please re-enter and try again.")
                continue
            else:
                break
        return major

    @staticmethod
    def enter_last_institution():
        """Validates Last Institution entry"""
        accept_last_institution = True
        while True:
            try:
                last_institution = str(input("Please enter the last institution: "))
                if last_institution == "":
                    print("Last Institution was not a valid entry. Please re-enter and try again.")
                    continue
            except ValueError:
                print("Last Institution was not a valid entry. Please re-enter and try again.")
                continue
            else:
                break
        return last_institution

    @staticmethod
    def enter_highest_degree_earned():
        """Validates Highest Degree entry"""
        accept_highest_degree_earned = True
        while True:
            try:
                highest_degree_earned = str(input("Please enter the highest degree earned: "))
                if highest_degree_earned == "":
                    print("Highest Degree Earned was not a valid entry. Please re-enter and try again.")
                    continue
            except ValueError:
                print("Highest Degree Earned was not a valid entry. Please re-enter and try again.")
                continue
            else:
                break
        return highest_degree_earned

