import unittest
from classes.pizza import Pizza

class TestPizzaClass(unittest.TestCase):
    """Test the pizza class"""
    
    def setUp(self):
        """Create an instance of the Pizza Class for testing all class functions"""
        self.my_pizza = Pizza("Sally's Pizza")
        
    def test_add_topping_success(self):
        """Test Adding a valid topping to the pizza"""
        self.my_pizza.addTopping("mushrooms")
        self.assertIn("mushrooms",self.my_pizza.toppings)
        
    def test_add_topping_failure(self):
        """Test adding a topping that is invalid to the pizza"""
        self.my_pizza.addTopping("bbq chicken")
        self.assertNotIn("bbq chicken",self.my_pizza.toppings)
        
    def test_remove_topping_success(self):
        """Test adding a valid topping to the pizza and removing it to ensure it is effectively removed."""
        self.my_pizza.addTopping("ham")
        self.assertIn("ham",self.my_pizza.toppings)
        self.my_pizza.removeTopping("mushrooms")
        self.assertIn("mushrooms",self.my_pizza.toppings)
        
        
        
        
