'''Mathematical Operations with Custom Packages and Enums'''
import string_utils
from enum_1 import Operation
import myMATH.comp as comp
import myMATH.sim as sim

# Define a function to perform mathematical operations based on input operation
def perform_operation(n1, n2, operation):
    if operation == Operation.ADD: # If operation is addition
        return sim.add(n1, n2) # Call the add function from sim package
    elif operation == Operation.MINUS: # If operation is subtraction
        return sim.minus(n1, n2) # Call the minus function from sim package
    elif operation == Operation.MULT: # If operation is multiplication
        return comp.mult(n1, n2) # Call the mult function from comp package
    elif operation == Operation.DIVIDE: # If operation is division
        return comp.divide(n1, n2) # Call the divide function from comp package
    else:
        raise ValueError("Invalid operation") # If an invalid operation is provided, raise an error

# Call the perform_operation function with different inputs and print the output
if __name__ == '__main__':
    print(perform_operation(2, 3, Operation.ADD)) # Output: 5
    print(perform_operation(5, 1, Operation.MULT)) # Output: 5
    print(perform_operation(5, 1, Operation.DIVIDE)) # Output: 5.0
    print(perform_operation(5, 1, Operation.MINUS)) # Output: 4
    # We also call the divide, add, minus, and reverse_string functions 
    # from their respective modules and output their results as well.
    print(comp.divide(3, 4)) 
    print(sim.add(3, 4))
    print(sim.minus(4, 3))
    print(string_utils.reverse_string("shani")) # Output: inahs




