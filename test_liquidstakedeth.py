# test_liquidstakedeth.py
"""
Tests for LiquidStakedEth module.
"""

import unittest
from liquidstakedeth import LiquidStakedEth

class TestLiquidStakedEth(unittest.TestCase):
    """Test cases for LiquidStakedEth class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LiquidStakedEth()
        self.assertIsInstance(instance, LiquidStakedEth)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LiquidStakedEth()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
