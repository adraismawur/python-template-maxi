"""Contains an example function for the template package

This file, and the folder it is in are totally optional. You can delete them if you
think you will not be writing a lot of code, and you can just make a few files in the
root directory instead.
"""

# it is important to have a descriptive docstring as shown above for each module
# this makes it easy for someone to decide whether they want to be looking at this file


def say_hello(who_calls_hello):
    """Print a hello message to the console

    Args:
        who_calls_hello (str): The name of the caller.

    Returns:
        None
    """
    # it is also important to describe your function!
    # here it is obvious what the function does, but remember to describe the arguments
    # and the return value

    print(who_calls_hello + " says: Hello, World!")
