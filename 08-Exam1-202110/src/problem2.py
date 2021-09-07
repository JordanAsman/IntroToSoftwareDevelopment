"""
Exam 1, problem 2.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Jordan Asman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time

import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2a()
    run_test_problem2b()


def run_test_problem2a():
    """ Tests the   problem2a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('--------------------------------------------------')

    format_string = '    problem2a( {}, {}, {})'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 16 + 50 + 108 + 196  # which is 370
    print_expected_result_of_test([4, 7, 2],
                                  expected, test_results, format_string)
    actual = problem2a(4, 7, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 813708286658351638412742051606525819035781221475772765980157440302430013063785135968597904162041848766733763776919970
    print_expected_result_of_test([13, 15, 99],
                                  expected, test_results, format_string)

    actual = problem2a(13, 15, 99)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 323413
    print_expected_result_of_test([3, 8, 5],
                                  expected, test_results, format_string)
    actual = problem2a(3, 8, 5)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 2 + 6 + 12  # which is 20
    print_expected_result_of_test([2, 4, 1],
                                  expected, test_results, format_string)
    actual = problem2a(2, 4, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 2 + 6 + 12 + 20  # which is 40
    print_expected_result_of_test([2, 5, 1],
                                  expected, test_results, format_string)
    actual = problem2a(2, 5, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = (1 * 8) + (2 * 9) + (3 * 10) + (4 * 11) + (5 * 12)  # this = 160
    print_expected_result_of_test([8, 12, 1],
                                  expected, test_results, format_string)
    actual = problem2a(8, 12, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 254
    print_expected_result_of_test([2, 4, 3],
                                  expected, test_results, format_string)
    actual = problem2a(2, 4, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 254
    print_expected_result_of_test([2, 4, 3],
                                  expected, test_results, format_string)
    actual = problem2a(2, 4, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 7554
    print_expected_result_of_test([7, 10, 3],
                                  expected, test_results, format_string)
    actual = problem2a(7, 10, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 7554
    print_expected_result_of_test([7, 10, 3],
                                  expected, test_results, format_string)
    actual = problem2a(7, 10, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 333300
    print_expected_result_of_test([2, 100, 1],
                                  expected, test_results, format_string)
    actual = problem2a(2, 100, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 25164150
    print_expected_result_of_test([2, 100, 2],
                                  expected, test_results, format_string)
    actual = problem2a(2, 100, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 6489060
    print_expected_result_of_test([75, 110, 2],
                                  expected, test_results, format_string)
    actual = problem2a(75, 110, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 6806446
    print_expected_result_of_test([74, 110, 2],
                                  expected, test_results, format_string)
    actual = problem2a(74, 110, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 6944937
    print_expected_result_of_test([75, 111, 2],
                                  expected, test_results, format_string)
    actual = problem2a(75, 111, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = 7274644
    print_expected_result_of_test([74, 111, 2],
                                  expected, test_results, format_string)
    actual = problem2a(74, 111, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)

    # Test 17:
    expected = 729474980
    print_expected_result_of_test([74, 111, 3],
                                  expected, test_results, format_string)
    actual = problem2a(74, 111, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = 193354354
    print_expected_result_of_test([74, 76, 4],
                                  expected, test_results, format_string)
    actual = problem2a(74, 76, 4)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19:
    expected = 2646501
    print_expected_result_of_test([3, 200, 1],
                                  expected, test_results, format_string)
    actual = problem2a(3, 200, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 20:
    expected = 40664620
    print_expected_result_of_test([3, 200, 1],
                                  expected, test_results, format_string)
    actual = problem2a(10, 500, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem2a(m, n, r):
    """
    What comes in:  Positive integers m, n, and r, with n >= m.
    What goes out:
      -- Returns the sum:
          (1 * (m ** r))  +  (2 * ((m + 1) ** r))
                          +  (3 * ((m + 2) ** r))
                          +  (4 * ((m + 3) ** r))
                          +  ...
                          +  (X * (n ** r))
         where you must decide what   X   is from the obvious pattern.
         (See the examples below.)
    Side effects:   None.
    Examples:
      -- If m = 4, n = 7, and r = 2, this function returns:
           (1 * (4 ** 2))  +  (2 * (5 ** 2))
                           +  (3 * (6 ** 2))
                           +  (4 * (7** 2))
                 (which is    16 + 50 + 108 + 196,   which is   370)
      -- If m = 13, n = 15, and r = 99, this function returns:
            (1 * (13 ** 99))  +  (2 * (14 ** 99))  +  (3 * (15 ** 99))
                 (which is a very large number)
      -- If m = 3, n = 8, and r = 5, this function returns:
            (1 * (3 ** 5))  +  (2 * (4 ** 5))
                            +  (3 * (5 ** 5))
                            +  (4 * (6 ** 5))
                            +  (5 * (7 ** 5))
                            +  (6 * (8 ** 5))
                 (which is 323413)

      -- ASK FOR HELP if you do not understand the above examples.
    """
    sum = 0
    for k in range(n + 1 - m):
        sum = sum + ((k + 1) * (m + k) ** r)
    return sum
    ###########################################################################
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT: If you cannot determine the right value for X
    #     in the above specification, you may ask us to tell it to you,
    #     in which case your score on this problem is automatically three
    #     less than full credit, even if you solve the rest of the problem.
    #     Your score on this problem will not be less than 0, no matter what.
    ###########################################################################


def run_test_problem2b():
    """ Tests the   problem2b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')

    format_string = '    problem2b( {}, {})'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 100
    print_expected_result_of_test([4, 2],
                                  expected, test_results, format_string)
    actual = problem2b(4, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 179196
    print_expected_result_of_test([3, 10],
                                  expected, test_results, format_string)
    actual = problem2b(3, 10)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 2275
    print_expected_result_of_test([6, 3],
                                  expected, test_results, format_string)
    actual = problem2b(6, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 385
    print_expected_result_of_test([10, 1],
                                  expected, test_results, format_string)
    actual = problem2b(10, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 506
    print_expected_result_of_test([11, 1],
                                  expected, test_results, format_string)
    actual = problem2b(11, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 650
    print_expected_result_of_test([12, 1],
                                  expected, test_results, format_string)
    actual = problem2b(12, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 428738436
    print_expected_result_of_test([203, 2],
                                  expected, test_results, format_string)
    actual = problem2b(203, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 437228100
    print_expected_result_of_test([204, 2],
                                  expected, test_results, format_string)
    actual = problem2b(204, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 445843225
    print_expected_result_of_test([205, 2],
                                  expected, test_results, format_string)
    actual = problem2b(205, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 454585041
    print_expected_result_of_test([206, 2],
                                  expected, test_results, format_string)
    actual = problem2b(206, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 190658856025
    print_expected_result_of_test([934, 2],
                                  expected, test_results, format_string)
    actual = problem2b(934, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 327369
    print_expected_result_of_test([17, 3],
                                  expected, test_results, format_string)
    actual = problem2b(17, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 6657201
    print_expected_result_of_test([18, 4],
                                  expected, test_results, format_string)
    actual = problem2b(18, 4)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 1
    print_expected_result_of_test([1, 123456789],
                                  expected, test_results, format_string)
    actual = problem2b(1, 123456789)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 1 + (2 ** 54)  # which is 18014398509481985
    print_expected_result_of_test([2, 53],
                                  expected, test_results, format_string)
    actual = problem2b(2, 53)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = 1 + (2 ** 58) + (3 ** 58)  # this = 4710128697534475211073315434
    print_expected_result_of_test([3, 57],
                                  expected, test_results, format_string)
    actual = problem2b(3, 57)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17:
    expected = 333383335000
    print_expected_result_of_test([10000, 1],
                                  expected, test_results, format_string)
    actual = problem2b(10000, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = 41667916675000
    print_expected_result_of_test([50000, 1],
                                  expected, test_results, format_string)
    actual = problem2b(50000, 1)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19:
    expected = 2065793401
    print_expected_result_of_test([301, 2],
                                  expected, test_results, format_string)
    actual = problem2b(301, 2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 20:
    expected = 532208970969
    print_expected_result_of_test([305, 3],
                                  expected, test_results, format_string)
    actual = problem2b(305, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 21:
    expected = 540976671465
    print_expected_result_of_test([306, 3],
                                  expected, test_results, format_string)
    actual = problem2b(306, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 22:
    expected = 549859545466
    print_expected_result_of_test([307, 3],
                                  expected, test_results, format_string)
    actual = problem2b(307, 3)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 23:
    expected = 6352220573286585266782656
    print_expected_result_of_test([43, 10],
                                  expected, test_results, format_string)
    actual = problem2b(143, 10)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem2b(a, b):
    """
    What comes in:  Positive integers a and b.
    What goes out:
    -- Returns the sum:
          (1 * (1 ** b)  +  (2 * (2 ** b))
                         +  (3 * (3 ** b))
                         +  (4 * (4 ** b))
                         +  ...
                         +  (a * (a ** b))
    Side effects:   None.
    Examples:
    -- If a = 4 and b = 2, this function returns:
          (1 * (1 ** 2))  +  (2 * (2 ** 2))
                          +  (3 * (3 ** 2))
                          +  (4 * (4 ** 2))
              (which is    1 + 8 + 27 + 64,   which is   100)
    -- If a = 3 and b = 10, this function returns:
           (1 * (1 ** 10))  +  (2 * (2 ** 10))  +  (3 * (3 ** 10))
              (which is 179196)
    -- If a = 6 and b = 3, this function returns:
           (1 * (1 ** 3))  +  (2 * (2 ** 3))
                           +  (3 * (3 ** 3))
                           +  (4 * (4 ** 3))
                           +  (5 * (5 ** 3))
                           +  (6 * (6 ** 3))
              (which is 2275)

    -- ASK FOR HELP if you do not understand the above examples.
    """
    return problem2a(1, a, b)
    ###########################################################################
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   functions that are DEFINED ABOVE.
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix="")


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
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
