"""
This module demonstrates lets you practice INPUT from the CONSOLE.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, Mark Hays, their colleagues, and
         Jordan Asman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ TESTs the functions in this module (by calling them). """
    double_a_float()
    print_an_integer_many_times()
    print_an_integer_many_times_on_one_row()
    input_it_all()


def double_a_float():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a floating point number.
       b. Prints the input number, but doubled (i.e., multiplied by 2).
    No input validation is required.  ** Nothing else should be printed. **

    Example:
    Here is a sample run, where the user input is to the right of the colon:
         Enter a number: -3.14
         -6.28
    """
    num = float(input('Enter a floating point number: '))
    print(num + num)
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def print_an_integer_many_times():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a positive integer.
       b. Prints the input integer, but doubled (i.e., multiplied by 2),
          the input number of times.  (See the example.)
    No input validation is required.  ** Nothing else should be printed. **

    Example:
    Here are two sample runs, where user input is to the right of the colon:
         Enter an integer: 3
         6
         6
         6

         Enter an integer: 5
         10
         10
         10
         10
         10
    """
    num = int(input('Please enter a positive integer: '))
    for _ in range(num):
        print(num * 2)
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def print_an_integer_many_times_on_one_row():
    """
    Same as the previous problem, but print the numbers
    on a single line with no spaces in between them.

    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         666

         Enter an integer: 5
         1010101010
    """
    num = input('Please enter a positive integer: ')
    count = int(num)
    number = 2 * int(num)
    doubled = str(number)
    print(count * doubled)
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   The testing code is already written for you (above).
    #  __
    #  HINT: One way to print on a SINGLE line is to build up a string
    #        and then print that (single) string.
    # -------------------------------------------------------------------------


def input_it_all():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
      Prompts the user for and inputs:
        -- A positive floating point number
        -- A positive integer
        -- A string
      in that order (via three separate INPUT statements).
      Then prints, in this order, all on separate lines:
        a. The square root of the floating point number,
           repeated the input integer number of times.
        b. The string, repeated the input integer number of times.
      No input validation is required.  ** Nothing else should be printed. **

    Example:
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    number = float(input('Please enter a floating point number: '))
    integer = int(input('Please enter a positive integer: '))
    string = input('Please enter a string: ')
    for _ in range(integer):
        print(number ** (1/2))
    for _ in range(integer):
        print(string)

    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   The testing code is already written for you (above).
    #  __
    #  HINT: If you add an  import math   statement, put it at the BEGINNING
    #        of this module, NOT ** INSIDE ** the definition of this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
