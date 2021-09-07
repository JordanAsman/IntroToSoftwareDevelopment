"""
Exam 1, problem 1.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Jordan Asman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time

import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()


###############################################################################
# DONE: 2. Right-click on the  src  folder and
#              Mark Directory as ... Sources Root,
#          if you have not already done so.
###############################################################################

###############################################################################
# DONE: 3.  READ the green doc-strings for the:
#     - greatest_common_divisor
#   function defined below.  You do NOT need to understand its implementation,
#   just its specifications (per the doc-strings).  You should  ** CALL **
#   that function as needed in implementing other function(s) in this module.
#   After you have READ this, change its _TODO_ to DONE.
###############################################################################


def greatest_common_divisor(a, b):
    """
    What comes in: Two positive integers a and b.
    What goes out:
      -- Returns the greatest common divisor of a and b, that is,
         the largest positive integer that divides evenly into both a and b.
    Side effects:  None.
    Examples:
      greatest_common_divisor(12, 8) is 4 because 4 divides evenly into 12
         and into 8, and no integer larger than 4 divides evenly into both.
         
      greatest_common_divisor(12, 35) is 1 because 1, 2, 3 and 4 are the only
         integers that divide evenly into 12, and the only one of those
         that divides evenly into 35 is 1.
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problem(s) below.
    # -------------------------------------------------------------------------


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1a   function:")
    print("--------------------------------------------------")

    format_string = "    problem1a( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = False
    print_expected_result_of_test([12, 8], expected, test_results,
                                  format_string)
    actual = problem1a(12, 8)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    if actual == "False":
        print("Your function returned the STRING 'False',")
        print("which is WRONG.  It should have returned")
        print("the built-in constant False.")

    # Test 2:
    expected = True
    print_expected_result_of_test([12, 35], expected, test_results,
                                  format_string)
    actual = problem1a(12, 35)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    if actual == "True":
        print("Your function returned the STRING 'True',")
        print("which is WRONG.  It should have returned")
        print("the built-in constant True.")

    # Test 3:
    expected = True
    print_expected_result_of_test([7, 13], expected, test_results,
                                  format_string)
    actual = problem1a(7, 13)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = False
    print_expected_result_of_test([8, 12], expected, test_results,
                                  format_string)
    actual = problem1a(8, 12)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = True
    print_expected_result_of_test([21, 155], expected, test_results,
                                  format_string)
    actual = problem1a(21, 155)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = True
    print_expected_result_of_test([1001, 3000], expected, test_results,
                                  format_string)
    actual = problem1a(1001, 3000)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = True
    print_expected_result_of_test([17, 97], expected, test_results,
                                  format_string)
    actual = problem1a(17, 97)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = True
    print_expected_result_of_test([97, 17], expected, test_results,
                                  format_string)
    actual = problem1a(97, 17)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = False
    print_expected_result_of_test([1000000, 357294], expected, test_results,
                                  format_string)
    actual = problem1a(1000000, 357294)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem1a(a, b):
    """
    What comes in: Two positive integers a and b.
    What goes out:
      -- Returns True if the greatest common divisor of a and b is 1.
    Side effects:   None.
    Examples:
      greatest_common_divisor(12, 8)  is 4, so problem1a(12, 8)  returns False.
      greatest_common_divisor(12, 35) is 1, so problem1a(12, 35) returns True.

                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    """
    if greatest_common_divisor(a, b) == 1:
        return True
    else:
        return False
    ###########################################################################
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
    ###########################################################################


def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1b   function:")
    print("--------------------------------------------------")

    format_string = "    problem1b( {}, {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 3
    print_expected_result_of_test([6, 30, 40],
                                  expected, test_results, format_string)
    actual = problem1b(6, 30, 40)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 4
    print_expected_result_of_test([36, 20, 32],
                                  expected, test_results, format_string)
    actual = problem1b(36, 20, 32)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 5
    print_expected_result_of_test([36, 19, 32],
                                  expected, test_results, format_string)
    actual = problem1b(36, 19, 32)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 4
    print_expected_result_of_test([36, 20, 33],
                                  expected, test_results, format_string)
    actual = problem1b(36, 20, 33)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 4
    print_expected_result_of_test([36, 20, 34],
                                  expected, test_results, format_string)
    actual = problem1b(36, 20, 34)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 5
    print_expected_result_of_test([36, 20, 35],
                                  expected, test_results, format_string)
    actual = problem1b(36, 20, 35)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 744
    print_expected_result_of_test([1016, 500, 2000],
                                  expected, test_results, format_string)
    actual = problem1b(1016, 500, 2000)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 745
    print_expected_result_of_test([1016, 500, 2001],
                                  expected, test_results, format_string)
    actual = problem1b(1016, 500, 2001)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 746
    print_expected_result_of_test([1016, 499, 2002],
                                  expected, test_results, format_string)
    actual = problem1b(1016, 499, 2002)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print()
    print("The next set of tests will take")
    print("up to 10 or so seconds.  Be patient.")
    # More tests: the greatest common divisor of 2 and X is 1
    #   if and only if X is odd.  That forms the basis for the following tests:
    passed_first_set_of_extra_tests = True
    for t in range(1, 3333):
        expected = (t + 1) // 2
        actual = problem1b(2, 1, t)  # Run the code to test
        if expected != actual:
            print_expected_result_of_test([2, 1, t], expected,
                                          test_results, format_string)
            print_actual_result_of_test(expected, actual, test_results)
            passed_first_set_of_extra_tests = False
            break

    if passed_first_set_of_extra_tests:
        message = "  PASSED the FIRST set of extra tests -- good!"
        testing_helper.print_colored(message, color="blue")

    print()
    print("The next set of tests will again take")
    print("up to 10 or so seconds.  Be patient.")
    # Still more tests: a calculation similar to the previous loop
    #   forms the basis for the following tests:
    passed_second_set_of_extra_tests = True
    r = 2 * 2 * 5 * 11
    for t in range(1, 5001):
        expected = (t
                    - (t // 2)  # subtract out multiples of 2
                    - (t // 5)  # subtract out multiples of 5
                    - (t // 11)  # subtract out multiples of 11
                    + (t // 10)  # multiples of 10 were double-counted
                    + (t // 22)  # multiples of 22 were double-counted
                    + (t // 55)  # multiples of 55 were double-counted
                    - (t // 110))  # multiples of 110 were triple-counted
        actual = problem1b(r, 1, t)  # Run the code to test
        if expected != actual:
            print_expected_result_of_test([r, 1, t], expected,
                                          test_results, format_string)
            print_actual_result_of_test(expected, actual, test_results)
            passed_second_set_of_extra_tests = False
            break

    if passed_second_set_of_extra_tests:
        message = "  PASSED the SECOND set of extra tests -- good!"
        testing_helper.print_colored(message, color="blue")

    print_summary_of_test_results(test_results)


def problem1b(r, s, t):
    """
    What comes in:  Non-negative integers r, s, and t, with s <= t.
    What goes out:
      -- Returns the number of integers between s and t, inclusive,
           for which the greatest common divisor of the integer and r is 1.
           (See examples.)
    Examples:
      -- If r = 6, s = 30, and t = 40, this function returns 3 because:
           -- The greatest common divisor of 6 and 30   is 6.     NO.
           -- The greatest common divisor of 6 and 31   is 1.    YES, is 1.
           -- The greatest common divisor of 6 and 32   is 2.     NO.
           -- The greatest common divisor of 6 and 33   is 3.     NO.
           -- The greatest common divisor of 6 and 34   is 2.     NO.
           -- The greatest common divisor of 6 and 35   is 1.    YES, is 1.
           -- The greatest common divisor of 6 and 36   is 6.     NO.
           -- The greatest common divisor of 6 and 37   is 1.    YES, is 1.
           -- The greatest common divisor of 6 and 38   is 2.     NO.
           -- The greatest common divisor of 6 and 39   is 3.     NO.
           -- The greatest common divisor of 6 and 40   is 2.     NO.
          and there are 3 YES's in the above, that is,
            - for 31, 35, and 37,  their greatest_common_divisor with 6 is 1,
            - and for all other integers between 30 and 40, their
              greatest common divisor with 6 is NOT 1.

      -- If r = 36, s = 20, and t = 32, this function returns 4 because:
           -- The greatest common divisor of 23 and 36 is 1.
           -- The greatest common divisor of 25 and 36 is 1.
           -- The greatest common divisor of 29 and 36 is 1.
           -- The greatest common divisor of 31 and 36 is 1.
           -- and for all other integers between 20 and 32,
                its greatest common divisor with 36 is NOT 1.

      *** Ask for help if you do not understand the above examples. ***
     """
    count = 0
    for k in range((t + 1) - s):
        if problem1a(r, k + s):
            count = count + 1
    return count
    ###########################################################################
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
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
try:
    main()
except Exception:
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
