import unittest
from functions.class_function import *

class ClassFunctionTestCase(unittest.TestCase):
    
    def test_class_function(self):
        """Testing creating a course"""
        test_course = "IT 412"
        semester = 2050        
        self.assertTrue(validate_str(test_course),validate_semester(semester))
        
    def test_invalid_class_function(self):
        """Testing passing invalid parameters"""
        test_course = "IT412"
        semester = 2050        
        self.assertTrue(validate_str(test_course),validate_semester(semester))
        
    def test_invalid_class_function_second(self):
        """Testing passing invalid parameters"""
        test_course = "IT 412"
        semester = "2050"        
        self.assertTrue(validate_str(test_course),validate_semester(semester))
        

        
    