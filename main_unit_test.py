# Unit Tests for Mathematical Functions and String Utils

import unittest
from myMATH.comp import mult, divide
from myMATH.sim import add, minus
from string_utils import reverse_string



# Define a test class for the functions in the 'comp' module
class unittest_comp(unittest.TestCase):
# Test the 'mult' function    
    def testmult(self):
        self.assertEqual(mult(4,5), 20)
# Test the 'divide' function
    def testdivide(self):    
        self.assertEqual(divide(6,3), 2)

# Define a test class for the functions in the 'sim' module
class unittest_sim(unittest.TestCase):        
# Test the 'add' function
    def testadd(self):
        self.assertEqual(add(4,5), 9)    
# Test the 'minus' function
    def testminus(self):
        self.assertEqual(minus(6,2), 4)

class unittest_string_utils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('Python'), 'nohtyP')
        self.assertEqual(reverse_string('12345'), '54321')
        
        
# Run all the tests defined in the test classes
if __name__ == '__main__':
    unittest.main()        
