"""
Exam 3, Problem 4

Authors: David Mutchler, Sana Ebrahimi, Mohammad Noureddine, their colleagues,
         and Jordan Asman
"""  # DONE: 1. Put your name in the line above

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4a()
    run_test_problem4b()


def run_test_problem4a():
    """ Test the   problem4a   function"""
    print()
    print("--------------------------------------------------")
    print("Testing the   problem4a   function:")
    print("--------------------------------------------------")

    format_string = "    problem4a( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = 1234
    list_of_digits = [1, 2, 3, 4]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 2
    expected = 1056
    list_of_digits = [1, 0, 5, 6]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 3
    expected = 756
    list_of_digits = [0, 0, 7, 5, 6]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 4
    expected = 9
    list_of_digits = [9]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 5
    expected = 11
    list_of_digits = [1, 1]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 6
    expected = 0
    list_of_digits = [0, 0, 0, 0, 0, 0, 0, 0]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 7
    expected = 1000000
    list_of_digits = [1, 0, 0, 0, 0, 0, 0]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 8
    expected = 998877665544332211
    list_of_digits = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 9
    expected = 1
    list_of_digits = [0, 0, 1]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    # Test 10
    expected = 10
    list_of_digits = [0, 1, 0]
    run_and_print_test([list_of_digits], expected, test_results,
                       format_string, problem4a)

    print_summary_of_test_results(test_results)


def problem4a(list_of_digits):
    """
    What comes in:
      -- A non empty list of integers that are digits (recall a digit is an
          integer >= 0 and < 10)

    What goes out:
      -- The integer represented by the individual digits in the list.

    Side effects:   None.

    Examples:
      -- problem4a([1, 2, 3, 4])
        returns 1234 = 1 * 1000 + 2 * 100 + 3 * 10 + 4
         or alternatively 1234 = 1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10^0

      -- problem4a([1, 0, 5, 6, 7, 0])
        return 105670 = 1 * 100000 + 0 * 10000 + 5 * 1000 + 6 * 100 + 7 * 10 + 0

      -- problem4a([0, 1, 0, 1])
        returns 101 = 0 * 1000 + 1 * 100 + 0 * 10 + 1

      -- problem4a([1])
        return 1

      -- problem4a([1, 0])
        returns 10 = 1 * 10 + 0

                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type list_of_digits: list[int]
      :rtype: int
    """
    number = 0
    length = len(list_of_digits)
    for k in range(length):
        power = (length - 1) - k
        number = number + list_of_digits[k] * (10 ** power)
    return number
    # -----------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # -----------------------------------------------------------------


def run_test_problem4b():
    """ Test the   problem4b   function"""
    print()
    print("--------------------------------------------------")
    print("Testing the   problem4b   function:")
    print("--------------------------------------------------")

    format_string = "    problem4b( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = [0, 3]
    left = [1]
    right = [2]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 2
    expected = [0, 2, 4, 6, 8]
    left = [1, 2, 3, 4]
    right = [1, 2, 3, 4]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 3
    expected = [1, 0]
    left = [9]
    right = [1]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 4
    expected = [1, 0, 0, 1]
    left = [1, 0, 0]
    right = [9, 0, 1]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 5
    expected = [1, 0, 0, 0]
    left = [5, 1, 4]
    right = [4, 8, 6]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 6
    expected = [1, 2, 1, 5]
    left = [6, 0, 5]
    right = [6, 1, 0]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 7
    expected = [0, 2, 2]
    left = [1, 9]
    right = [0, 3]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 8
    expected = [1, 8, 1, 2, 3, 6]
    left = [8, 4, 1, 0, 6]
    right = [9, 7, 1, 3, 0]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 9
    expected = [0, 1]
    left = [1]
    right = [0]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    # Test 10
    expected = [0, 5, 1]
    left = [2, 6]
    right = [2, 5]
    run_and_print_test([left, right], expected, test_results, format_string,
                       problem4b)

    print_summary_of_test_results(test_results)


def problem4b(left, right):
    """
    What comes in:
     -- Two non empty lists of DIGITS that HAVE THE SAME LENGTH, i.e.,
         len(left) == len(right) is TRUE

    What comes out:
     -- A list of digits of length len(left) + 1 (which is also len(right) + 1)
      that contains the digit by digit representation of the sum of the two
      numbers represented by left and right.

    Side effects: None

    Examples:
      -- problem4b([1], [2])
        returns [0, 3] because 3 = 1 + 2

      -- problem4b([1, 2, 3, 4], [1, 2, 3, 4])
        returns [0, 2, 4, 6, 8] because 2468 = 1234 + 1234

      -- problem4b([9], [1])
        returns [1, 0] because 10 = 9 + 1

      -- problem4b([1, 0, 0], [9, 0, 1])
        returns [1, 0, 0, 1] because 1001 = 100 + 901

      -- problem4b([5, 1, 4], [4, 8, 6])
        returns [1, 0, 0, 0] because 1000 = 514 + 486

      -- problem4b([6, 0, 5], [6, 1, 0])
        returns [1, 2, 1, 5] because 1215 = 605 + 610

                ** ASK YOUR INSTRUCTOR FOR HELP **
         ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    # ------------------------------------------------------------------------#
    # Hint: When adding two digits, if the answer is > 10 then we store a 0   #
    #  digit and maintain a carry for the next summation.                     #
    #                                                                         #
    #  Example: when summing the digits 9 and 5, the result is 15 > 10,       #
    #  so our digit becomes 0 and we maintain a carry of 5 for the next       #
    #  addition.                                                              #
    # ------------------------------------------------------------------------#

    Type hints:
      :type left: list[int]
      :type right: list[int]
      :rtype: list[int]
    """
    list = []
    for j in range(len(left) + 1):
        list.append(0)
    sum = 0
    carried = 0
    for k in range(len(left) - 1, -1, -1):
        sum = left[k] + right[k] + carried
        if sum // 10 > 0:
            carried = sum // 10
            list[k+1] = sum % 10
        else:
            list[k+1] = sum
            carried = 0
    if carried > 0:
        list[0] = carried
    return list
    # -----------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # -----------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def run_and_print_test(args, expected, test_results, format_string, function):
    print_expected_result_of_test(args, expected, test_results,
                                  format_string)
    actual = function(*args)
    print_actual_result_of_test(expected, actual, test_results)


def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("ERROR - While running this test,", color="red")
        print("your code raised the following exception:", color="red")
        print()
        time.sleep(1)
        raise
