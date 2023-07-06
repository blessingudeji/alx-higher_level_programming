#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_one(self):
        """Tests for an empty list []"""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_two(self):
        """Tests for no arguments passed"""
        self.assertIsNone(max_integer())

    def test_three(self):
        """Tests for a single number in the list"""
        one_num = [5]
        self.assertEqual(max_integer(one_num), 5)

    def test_three(self):
        """Tests for all positive num  with max at end"""
        positive_e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(positive_e), 50)

    def test_four(self):
        """Tests for all positive num with max in middle"""
        positive_m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(positive_m), 360)

    def test_five(self):
        """Tests for all positive num with max at beginning"""
        positive_b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(positive_b), 200)

    def test_six(self):
        """Tests for list with one negative number"""
        negative_o = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(negative_o), 200)

    def test_seven(self):
        """Tests for list with all negative numbers"""
        negative_a = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(negative_a), -1)

    def test_eight(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_nine(self):
        """Tests for a string in list"""
        string = [1, 2, "Hi", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
