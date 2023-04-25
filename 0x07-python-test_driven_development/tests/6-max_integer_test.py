#!/usr/bin/python3
""" A concise Unittest for a function that finds the maximum
integer in a list.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


Class TestMaxInt(unittest.TestCase):
    """ The class that houses all the test cases """
    def test_emptyList(self):
        self.assertEqual(max_integer([]), None)

    def test_Iflist(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_positiveInt(self):
        self.assertEqual(max_integer([2, 5, 9, 92]), 92)

    def test_negativeInt(self):
        self.assertEqual(max_integer([-2, -49, -34, -3]), -2)

    def test_oneElement(self):
        self.assertEqual(max_integer([9, 92]), 92)

    def test_twoElement(self):
        self.assertEqual(max_integer([2]), 2)

    def test_mixed(self):
        with self.assertRaises(TypeError):
            max_integer[3, (5, 5)]

    def test_emptyList(self):
        self.assertEqual(max_integer[], None)
