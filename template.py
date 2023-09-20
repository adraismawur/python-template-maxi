"""Main module of your code

Author(s): Arjan Draisma

This code is covered under the GNU General Public License v3.0.
Please refer to the LICENSE located in the root of this repository.
"""

# imports are always at the top of your file
# they are sorted first by standard library
import sys

# then by third party
# e.g. import numpy as np

# then by your own code
from template.module_example import say_hello
from another_file import another_function


if __name__ == "__main__":
    file_name = sys.argv[0]

    say_hello(file_name)

    another_function()
