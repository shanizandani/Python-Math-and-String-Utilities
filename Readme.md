
# Python Math and String Utilities
This repository contains Python modules for mathematical and string operations.

## Modules

### myMATH.comp

This module provides basic mathematical operations:
- `mult(x, y)` multiplies two numbers `x` and `y`.
- `divide(x, y)` divides `x` by `y`.

### myMATH.sim

This module provides simple mathematical operations:
- `add(x, y)` adds two numbers `x` and `y`.
- `minus(x, y)` subtracts `y` from `x`.

### string_utils

This module provides utilities for string operations:
- `reverse_string(s)` reverses the input string `s`.

## Enum

### enum_1

This module provides an enum for the basic mathematical operations:
- `Operation` defines four basic mathematical operations: ADDI, MINUS, MULT, DIVIDE.

## Usage

The functions can be used by importing them in your Python code.

Example:

from myMATH.comp import mult, divide
from myMATH.sim import add, minus
from string_utils import reverse_string
from enum_1 import Operation

result = mult(2, 3)
print(result) # Output: 6

result = add(2, 3)
print(result) # Output: 5

result = reverse_string("hello")
print(result) # Output: olleh

result = perform_operation(2, 3, Operation.ADDI)
print(result) # Output: 5

## Testing

The `unittest` module is used to run the tests. To run the tests, run the following command in your terminal:

python -m unittest main_unit_test.py


## Installation

To download and use this project, you can either clone the repository or download it as a ZIP file.
Cloning the repository

  1.  Open your terminal or command prompt.
  2.  Change the current working directory to the location where you want the cloned directory to be made.
  3.  Type git clone https://github.com/<your-username>/<your-repository-name>.git and press enter.
  Type git clone https://github.com/shanizandani/Python-Math-and-String-Utilities.git and press enter.

  4.  Change the current working directory to the cloned directory.
  5.  Type python main.py to run the program.

Downloading as a ZIP file

   6. Go to the repository on GitHub.
   7. Click on the "Code" button and select "Download ZIP".
   8. Extract the ZIP file to the location where you want the project to be saved.
   9. Open your terminal or command prompt.
  10.  Change the current working directory to the project directory.
   11. Type python main.py to run the program.

 ## Python version
 This project was written in Python 3.11 or a later version.

## License

This project is licensed under the MIT License. See the LICENSE file for more information
You can find the full text of the MIT License at the official website of the Open Source Initiative (OSI) at https://opensource.org/licenses/MIT.