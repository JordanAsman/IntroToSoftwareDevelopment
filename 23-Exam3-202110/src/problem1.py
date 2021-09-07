"""
Exam 3, Problem 1

Authors: David Mutchler, Sana Ebrahimi, Mohammad Noureddine, their colleagues,
         and Jordan Asman
"""  # DONE: 1. Put your name in the line above

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()


def run_test_problem1a():
    """ Test the problem1a function """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1a   function:")
    print("--------------------------------------------------")

    format_string = "    problem1a( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = 17
    argument1 = [10, 3, 4, 3, 3]
    argument2 = 4
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1a)

    # Test 2
    expected = 23
    argument1 = [10, 3, 4, 3, 3]
    argument2 = 5
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1a)

    # Test 3
    expected = 10
    argument1 = [10, 3, 4, 3, 3]
    argument2 = 10
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1a)

    # Test 4
    expected = 10
    argument1 = [1, 2, 3, 4, 4, 5, 4]
    argument2 = 4
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1a)

    # Test 5
    expected = 0
    argument1 = [0, 1000000]
    argument2 = 0
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1a)

    # Test 6
    expected = 0
    argument1 = []
    argument2 = -100
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1a)

    # Test 7
    expected = 0
    argument1 = []
    argument2 = 75
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1a)

    print_summary_of_test_results(test_results)


def problem1a(seq, num):
    """
    What comes in:
      -- A sequence of numbers.
      -- A number "num".
    What goes out:
      -- Returns the sum of the numbers in the sequence
           until the first time we encounter "num".
           The integer "num" must be included in the sum that is returned.
      -- If the sequence does not contain "num", then this function
           returns the sum of ALL the numbers in the sequence.
    Side effects:  None.

    Examples:
      -- Suppose that
            seq_seq = [10, 3, 4, 3, 3]
         Then if num = 4,
            problem1(seq_seq, num) returns 10 + 3 + 4, which 17,
         and  if num = 5,
            problem1(seq_seq, num) returns
               10 + 3 + 4 + 3 + 3, which is 23,
         and  if num = 10,
            problem1(seq_seq, num) returns 10

      -- More examples:
         - problem1([1, 2, 3, 4, 4, 5, 4], 4)
            returns 1 + 2 + 3 + 4 = 10

         - problem1([0, 1000000], 0)
            returns 0

        - problem1([], -100)
            returns 0

        - problem1([], 75)  returns 0

                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    Type hints:
      :type seq: list[float]
      :type num: float
      :rtype: int
    """
    sum = 0
    k = 0
    while k < len(seq):
        if seq[k] != num:
            sum = sum + seq[k]
            k = k + 1
        else:
            sum = sum + num
            break
    return sum
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------


def run_test_problem1b():
    """ Test the   problem1b   function"""
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1b   function:")
    print("--------------------------------------------------")

    format_string = "    problem1b( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = -74
    argument1 = [[1, 3, 4], [-9, 8, 0], [9, 10, -100], [3, 2, 1]]
    argument2 = -100
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 2
    expected = 10
    argument1 = [[1, 2, 3, 4, 4, 5, 4], [1, 2, 3]]
    argument2 = 4
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 3
    expected = 0
    argument1 = [[], [0], [1, 100000]]
    argument2 = 0
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 4
    expected = 100001
    argument1 = [[], [0], [1, 100000]]
    argument2 = -100
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 5
    expected = 0
    argument1 = [[]]
    argument2 = -1
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 6
    expected = -1181510
    argument1 = [[-243319, -938191]]
    argument2 = 290650
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 7
    expected = 195086
    argument1 = [[195086]]
    argument2 = 195086
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 8
    expected = 1508492
    argument1 = [[-189501, 729213, -81513, 768591], [281702, -10140, 810930]]
    argument2 = 281702
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 9
    expected = -333947
    argument1 = [[-333947, -768641], [591219],
                 [-66226, 725342, 359795, -444982]]
    argument2 = -333947
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    # Test 10
    expected = 1031754
    argument1 = [[206424, 825330, 426726], [-125415]]
    argument2 = 825330
    run_and_print_test([argument1, argument2], expected, test_results,
                       format_string, problem1b)

    print_summary_of_test_results(test_results)


def problem1b(seq_seq, num):
    """
    What comes in:
      -- A sequence of sequences of numbers.
      -- A number "num".
    What goes out:
      -- Returns the sum of the numbers in the subsequences
           until the first time we encounter "num".
           The integer "num" must be included in the sum that is returned.
      -- If no subsequences contain "num", then this function
           returns the sum of ALL the numbers in the subsequences.
    Side effects:  None.

    Examples:
      -- Suppose that
            seq_seq = [(10, 3, 4, 3, 3),
                       (-9, 0),
                       (10, 5, 20),
                       (6, 2, 2, 2, 1)]
         Then if num = 4,
            problem1(seq_seq, num) returns 10 + 3 + 4, which 17,
         and  if num = 5,
            problem1(seq_seq, num) returns
               10 + 3 + 4 + 3 + 3 + (-9) + 0 + 10 + 5, which is 29,
         and  if num = 2,
            problem1(seq_seq, num) returns
               10 + 3 + 4 + 3 + 3 + (-9) + 0 + 10 + 5 + 20 + 6 + 2, which is 57,
         and  if num = 7 (which is not in any of the subsequences),
            problem1(seq_seq, num) returns
               10 + 3 + 4 + 3 + 3 + (-9) + 0 + 10 + 5 + 20 + 6 + 2 + 2 + 2 + 1,
               which is 62.
               
      -- More examples:
         - problem1([(1, 2, 3, 4, 4, 5, 4),
                     (1, 2, 3)],
                    4)
            returns 1 + 2 + 3 + 4 = 10

         - problem1([(),
                    (0, 5),
                    (1, 100000)],
                   0)
            returns 0

        - problem1([(),
                    (0, 5),
                    (1, 100000)],
                   -100)
            returns 0 + 5 + 1 + 100000, which is 100006

        - problem1([], 75)  returns 0
        - problem([(), (), (), ()], 88)  returns 0

                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    Type hints:
      :type seq_seq: list[list[float]]
      :type num: float
      :rtype: int
    """
    sum = 0
    broken = False
    for k in range(len(seq_seq)):
        if broken:
            break
        for j in range(len(seq_seq[k])):
            if seq_seq[k][j] == num:
                sum = sum + num
                broken = True
                break
            else:
                sum = sum + seq_seq[k][j]
    return sum
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
