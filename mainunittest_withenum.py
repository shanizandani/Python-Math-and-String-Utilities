import unittest
from app import perform_operation
from myMATH.comp import mult, divide
from myMATH.sim import add, minus
from string_utils import reverse_string
from enum_1 import Operation


# Define a test class for the functions in the 'comp' module
class unittest_comp(unittest.TestCase):
    # Test the 'mult' function    
    def test_mult(self):
        self.assertEqual(mult(4, 5), 20)
    # Test the 'divide' function
    def test_divide(self):    
        self.assertEqual(divide(6, 3), 2)

# Define a test class for the functions in the 'sim' module
class unittest_sim(unittest.TestCase):        
    # Test the 'add' function
    def test_add(self):
        self.assertEqual(add(4, 5), 9)    
    # Test the 'minus' function
    def test_minus(self):
        self.assertEqual(minus(6, 2), 4)


# Define a test class for the functions in the 'string_utils' module
class unittest_string_utils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('Python'), 'nohtyP')
        self.assertEqual(reverse_string('12345'), '54321')

# enum
# Define a test class for the perform_operation function
class unittest_perform_operation(unittest.TestCase):
    # Test the 'perform_operation' function
    def test_perform_operation(self):
        self.assertEqual(perform_operation(2, 3, Operation.ADD), 5)
        self.assertEqual(perform_operation(5, 1, Operation.MULT), 5)
        self.assertEqual(perform_operation(5, 1, Operation.DIVIDE), 5.0)
        self.assertEqual(perform_operation(5, 1, Operation.MINUS), 4)
       


        
        
# Run all the tests defined in the test classes
if __name__ == '__main__':
    unittest.main() 
