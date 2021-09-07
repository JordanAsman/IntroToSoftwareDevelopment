"""
Exam 2, Problem 1

Authors: David Mutchler, Sana Ebrahimi, Mohammad Noureddine, their colleagues,
         and Jordan Asman
"""  # DONE: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    print()
    print("--------------------------------------------------")
    print("Un-comment the tests one by one")
    print("as you work the problems.")
    print("--------------------------------------------------")
    run_test_problem1a()
    run_test_problem1b()


###############################################################################
# DONE: 2. Right-click on the  src  folder and
#              Mark Directory as ... Sources Root,
#          if you have not already done so.
###############################################################################

def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1a   function:")
    print("--------------------------------------------------")

    format_string = "    problem1a( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = 10
    argument = [90, 10, 45]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Test 2
    expected = 18
    argument = [4, 1, 6, 18, 10, 12, 21]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Test 3
    expected = 33
    argument = [33]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Test 4
    expected = 99
    argument = [4, 1, 6, 0, 100, 99, 12, 21, 2, 33, 23]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Test 5
    expected = 100
    argument = [4, 1, 6, 0, 99, 100, 12, 21, 2, 33, 23]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Test 6
    expected = -99
    argument = [4, 1, 6, 0, -10, -99, 12, 21, 2, 33, 23]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Test 7
    expected = -10
    argument = [4, 1, 6, 0, -99, -10, 12, 21, 2, 33, 23]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Test 8
    expected = 510
    argument = [10 * x for x in range(103)]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1a)

    # Summary:
    print_summary_of_test_results(test_results)


def problem1a(numbers):
    """
    What comes in: A sequence of numbers,
      where the length of the sequence is guaranteed to be odd.
    What goes out:
      -- The number at the middle of the sequence.
    Side effects:   None.
    Examples:
      -- problem1a( [90, 10, 45] )                 returns  10
      -- problem1a( [4, 1, 6, 18, 10, 12, 21] )    returns  18
      -- problem1a( [33] )					       returns  33
                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    Type hints:
      :type numbers: list[int]
      :rtype: int
    """
    center = int((len(numbers) / 2))
    return numbers[center]
    ###########################################################################
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################


def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1b   function:")
    print("--------------------------------------------------")

    format_string = "    problem1b( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = 7.4
    argument = [1, 7, 6, 5, 10, 3, 9]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 2
    expected = 5.0
    argument = [2, 1, 4, 4, 7]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 3
    expected = 8.0
    argument = [9, 4, 7, 6, 2]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 4
    expected = 2.0
    argument = [1, 2, 1]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 5
    expected = 6.0
    argument = [1, 2, 10]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 6
    expected = 2.0
    argument = [1, 2, 2]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 7
    expected = 2.0
    argument = [2, 2, 1]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)
    # Test 8
    expected = 6.0
    argument = [10, 2, 1]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 9
    expected = 7.0
    argument = [10, 2, 9]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 10
    expected = 2.0
    argument = [2, 2, 2]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 11
    expected = 8.0
    argument = [1, 2, 8, 7, 7]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 12
    expected = 8.5
    argument = [9, 2, 8, 7, 7]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)
    # Test 13
    expected = 8.5
    argument = [2, 9, 8, 7, 7]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)
    # Test 14
    expected = 8.0
    argument = [8, 8, 8, 7, 7]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)
    # Test 15
    expected = 9.0
    argument = [1, 2, 8, 2, 10]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)
    # Test 16
    expected = 9.0
    argument = [1, 2, 8, 10, 2]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 17
    expected = 7.0
    argument = [4, 10, 4, 10, 2]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)
    # Test 18
    expected = 6.4
    argument = [4, 10, 4, 10, 4]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)
    # Test 19
    expected = 7.2
    argument = [6, 10, 4, 6, 10]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 20
    expected = 18.0
    argument = [4, 1, 6, 18, 10, 12, 17]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 21
    expected = 33.0
    argument = [33]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 22
    expected = 101.0
    argument = [4, 1, 6, 0, 100, 99, 12, 21, 104, 33, 23]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 23
    expected = 126.25
    argument = [155, 150, 6, 0, 99, 100, 12, 100, 2, 33, 23]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 24
    expected = -3.9
    argument = [4, 1, 6, 0, -10, -99, 11, 20, -2, 30, -300]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 25
    expected = -3.9
    argument = [-300, 1, 6, 0, -10, -99, 11, 20, -2, 30, 4]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 26
    expected = -5.5
    argument = [-300, -1, -100, -100, -99, -10, -12, -20, -200, -38, -300]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 27
    expected = sum(range(51, 103)) / 52
    argument = [x for x in range(103)]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 28
    expected = 4 * sum(range(114, 129)) / 15
    argument = [4 * x for x in range(100, 129)]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 29
    expected = 1000.0
    argument = [4 * x for x in range(100, 129)]
    argument[14] = 1000
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 30
    expected = 1500.0
    argument = [4 * x for x in range(100, 129)]
    argument[14] = 1000
    argument[0] = 2000
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Test 30
    expected = 1500.0
    argument = [4 * x for x in range(100, 129)]
    argument[14] = 1000
    argument[28] = 2000
    run_and_print_test([argument], expected, test_results, format_string,
                       problem1b)

    # Summary:
    print_summary_of_test_results(test_results)


# Be sure to read the IMPORTANT note in the following specification!
def problem1b(numbers):
    """
    What comes in: A a sequence of numbers,
       where the length of the sequence is guaranteed to be odd.
    What goes out:
       The average of the numbers in the sequence that are
       bigger than or equal to the number at the middle of the sequence.
    Side effects: None

    Examples:
      - problem1b( [1, 7, 6, 5, 10, 3, 9] )    returns  7.4
           - since the number at the middle of the sequence is 5,
           - and the numbers in the list bigger than or equal to 5 are
                7, 6, 5, 10 and 9,
           - and those 5 numbers add up to 7 + 6 + 5 + 10 + 9, which is 37,
           - and the average of 5 numbers that sum to 37 is 37 / 5,
           - which is 7.4.
      -- problem1b( [2, 1, 4, 4, 7] )          returns  5.0
           - since the number at the middle of the sequence is 4,
           - and the numbers in the list bigger than or equal to 4 are
                4, 4 and 7,
           - and the sum of those 3 numbers is 15,
           - so the average of them is 15/3, which is 5.0.
      -- problem1b( [9, 4, 7, 6, 2] )          returns  8.0
           - since the number at the middle of the sequence is 7,
           - and the numbers in the list bigger than or equal to 7 are 9 and 7,
           - and the sum of those 2 numbers is 16,
           - so the average of them is 16/2, which is 8.0.

    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.

                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    Type hints:
      :type numbers: list[int]
      :rtype: float
    """
    middle = problem1a(numbers)
    sum = 0.0
    count = 0.0
    for k in range(len(numbers)):
        if numbers[k] >= middle:
            sum += numbers[k]
            count +=1
    if count > 0:
        return sum/count
    else:
        return 0.0
    ###########################################################################
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
    #   REMINDER:
    #    **  You simply MUST do a concrete example by hand to figure out
    #    **  the steps needed to solve this (or any!) problem.
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

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


def run_and_print_test(args, expected, test_results, format_string, function):
    print_expected_result_of_test(args, expected, test_results,
                                  format_string)
    actual = function(*args)
    print_actual_result_of_test(expected, actual, test_results)


if __name__ == '__main__':
    # To allow color-coding the output to the console:
    USE_COLORING = True  # Change to False to revert to OLD style coloring

    testing_helper.USE_COLORING = USE_COLORING
    if USE_COLORING:
        # noinspection PyShadowingBuiltins
        print = testing_helper.print_colored
    else:
        # noinspection PyShadowingBuiltins
        print = testing_helper.print_uncolored

    # --------------------------------------------------------------------------
    # Calls  main  to start the ball rolling.
    # The   try .. except   prevents error messages on the console from being
    # intermingled with ordinary output to the console.
    # --------------------------------------------------------------------------
    try:
        main()
    except Exception:
        print("ERROR - While running this test,", color="red")
        print("your code raised the following exception:", color="red")
        print()
        time.sleep(1)
        raise
