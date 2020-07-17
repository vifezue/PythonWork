import unittest
from classes.InventoryItem import InventoryItem

class TestInventoryClass(unittest.TestCase):
    """Test constructor for Inventory Item"""
    def setUp(self):
        self.inventoryItem = InventoryItem("9595","Candybar",10)
        
    def test_buyItem(self):
        """Test function for buy item with parameter"""
        self.inventoryItem.buyItem(6)
        self.assertTrue(4,self.inventoryItem.currentQuantity)
        
    def test_buyItem_default(self):
        """Test function for buy item with default value"""
        self.inventoryItem.buyItem()
        self.assertTrue(9,self.inventoryItem.currentQuantity)
        
    def test_buyItem_default_fail(self):
        """False condition to test """
        self.inventoryItem.buyItem()
        self.assertFalse(10,self.inventoryItem.currentQuantity)