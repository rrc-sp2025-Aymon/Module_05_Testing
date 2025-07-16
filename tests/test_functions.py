"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch

from src.functions import greet_name_age, grade_outcome

class TestFunctions(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
       name = "Joe"
       age = 25
       expected = "Hello Joe, you are 25 years old!"
       actual = greet_name_age(name,age)
       self.assertEqual(expected,actual)
    
    def test_grade_outcome_a_plus(self):
        grade = 91
        expected = "A+"
        actual = grade_outcome(grade)
        self.assertEqual(expected,actual)

    def test_grade_outcome_pass(self):
        grade = 76
        expected = "Pass"
        low_edge = 50
        high_edge =90    
        self.assertEqual(expected,grade_outcome(grade))
        self.assertEqual(expected,grade_outcome(low_edge))
        self.assertEqual(expected,grade_outcome(high_edge))

    def test_grade_outcome_fail(self):
        grade = 40
        low_edge = -1
        high_edge = 49
        expected = "Fail"
        self.assertEqual(expected,grade_outcome(grade))
        self.assertEqual(expected,grade_outcome(low_edge))
        self.assertEqual(expected,grade_outcome(high_edge))




