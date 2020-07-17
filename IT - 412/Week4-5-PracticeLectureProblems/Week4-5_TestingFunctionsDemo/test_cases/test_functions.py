import unittest
from functions.function_library import *

class NamePartTestCase(unittest.TestCase):
    """Test for functions in the function_library.py file"""

    def test_name_part(self):
        """Here is a test I think should work"""
        self.assertTrue(validate_name_part("Tom"))
            
    