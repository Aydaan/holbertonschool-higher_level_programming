#!/usr/bin/python3
"""
Unittest for max_integer function.
"""
import unittest
max_integer = __import__("6-max_integer").max_integer
class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""
    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))
    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([5]), 5)
    def test_positive_integers(self):
        """Test a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_negative_integers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-8, -2, -5]), -2)
    def test_mixed_integers(self):
        """Test a list with positive and negative integers."""
        self.assertEqual(max_integer([-5, 3, 0, 8, -1]), 8)
    def test_float_values(self):
        """Test a list containing floats."""
        self.assertEqual(max_integer([1.5, 2.8, 2.7]), 2.8)
    def test_duplicate_max(self):
        """Test a list with duplicate maximum values."""
        self.assertEqual(max_integer([3, 5, 5, 2]), 5)
    def test_max_at_beginning(self):
        """Test when the maximum is the first element."""
        self.assertEqual(max_integer([9, 4, 3, 2]), 9)
    def test_max_at_end(self):
        """Test when the maximum is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
    def test_sorted_list(self):
        """Test an already sorted list."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
if __name__ == "__main__":
    unittest.main()
