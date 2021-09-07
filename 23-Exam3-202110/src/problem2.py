"""
Exam 3, Problem 2

Authors: David Mutchler, Sana Ebrahimi, Mohammad Noureddine, their colleagues,
         and Jordan Asman
"""  # DONE: 1. Put your name in the line above

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2a()
    run_test_problem2b()


def run_test_problem2a():
    """ Test the   problem2a  function"""
    print()
    print("--------------------------------------------------")
    print("Testing the   problem2a   function:")
    print("--------------------------------------------------")

    format_string = "    problem2a( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    seq_of_seq_of_words = [['hello', 'world'],
                           ['hi', 'hello'],
                           [],
                           ['hello', 'hola']]
    word_to_look_for = 'hello'
    expected = 3
    expected_sequence = [['Found IT!', 'world'],
                         ['hi', 'Found IT!'],
                         [],
                         ['Found IT!', 'hola']]
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    # Test 2
    seq_of_seq_of_words = [[]]
    word_to_look_for = 'a'
    expected = 0
    expected_sequence = [[]]
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    # Test 3
    seq_of_seq_of_words = [['abc', 'happy'],
                           ['world', 'peace', 'yes'],
                           ['no', 'war']]
    word_to_look_for = 'sad'
    expected = 0
    expected_sequence = [['abc', 'happy'],
                         ['world', 'peace', 'yes'],
                         ['no', 'war']]
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    # Test 4
    seq_of_seq_of_words = [['abc', 'happy'],
                           ['world', 'peace', 'yes'],
                           ['no', 'war']]
    word_to_look_for = 'no'
    expected = 1
    expected_sequence = [['abc', 'happy'],
                         ['world', 'peace', 'yes'],
                         ['Found IT!', 'war']]
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    # Test 5
    seq_of_seq_of_words = [[], [], [], ['Found IT!'], ['csse120', 'exam3'],
                           ['thursday', 'october', '29th'], []]
    word_to_look_for = 'Found IT!'
    expected = 1
    expected_sequence = [[], [], [], ['Found IT!'], ['csse120', 'exam3'],
                           ['thursday', 'october', '29th'], []]
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    # Test 6
    seq_of_seq_of_words = []
    word_to_look_for = 'ab'
    expected = 0
    expected_sequence = []
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    # Test 7
    seq_of_seq_of_words = [['ab']]
    word_to_look_for = 'ab'
    expected = 1
    expected_sequence = [['Found IT!']]
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    # Test 8
    seq_of_seq_of_words = [['ab']]
    word_to_look_for = 'abc'
    expected = 0
    expected_sequence = [['ab']]
    run_and_print_test([seq_of_seq_of_words, word_to_look_for], expected,
                       test_results, format_string, problem2a)
    check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results)

    print_summary_of_test_results(test_results)


def problem2a(seq_seq, word):
    """
    What comes in:
      -- A sequence of sequences of words
      -- A word we are looking for

    What goes out:
      -- The number of times the given word to look for appears in the entire
          sequence of sequences.

    Side effects:
      -- MUTATES the given sequence of sequences by replacing every
          occurrence of the word we are looking for with "Found IT!"

    Examples:

      seq_seq = [['hello', 'world'], ['hi', 'hello'], [], ['hello', 'hola']]
      count = problem2a(seq_seq, 'hello')  # count becomes 3
      # after the call to problem2a, seq_seq becomes
      # [['Found IT!', 'world'], ['hi', 'Found IT!'], [], ['Found IT!', 'hola']]

      seq_seq = [[]]
      count = problem2a(seq_seq, 'a') # count becomes 0
      # after the call, seq_seq is unchanged

      seq_seq = [['abc', 'happy'], ['world', 'peace', 'yes'], ['no', 'war']]
      count = problem2a(seq_seq, 'sad') # count becomes 0
      # after the call, seq_seq is unchanged


                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type seq_seq: list[list[str]]
      :type word: str
      :rtype: int
    """
    count = 0
    for k in range(len(seq_seq)):
        for j in range(len(seq_seq[k])):
            if seq_seq[k][j] == word:
                seq_seq[k][j] = "Found IT!"
                count = count + 1
    return count
    # -----------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # -----------------------------------------------------------------


def run_test_problem2b():
    """ Test the   problem2a  function"""
    print()
    print("--------------------------------------------------")
    print("Testing the   problem2b   function:")
    print("--------------------------------------------------")

    format_string = "    problem2b( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    seq_of_seq_of_int = [[0, 1, 2, -1, 5],
                         [-5, -10, 5, 0, 2],
                         [1, 2, 3],
                         [],
                         [-100]]
    expected = [-5, -10, -100]
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 2
    seq_of_seq_of_int = [[0], [-1, -2, 3], [0], [-10], []]
    expected = [-1, -2, -10]
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 3
    seq_of_seq_of_int = [[-1000], [1, 2, 3], [0, -1, -19], [500, 999]]
    expected = []
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 4
    seq_of_seq_of_int = [[3, 9, 8, 7], [1, 3, 2], [-10], [3], [3, 4], [1, 2]]
    expected = [1, 2, -10, 1, 2]
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 5
    seq_of_seq_of_int = [[1000], [1, 2, 3], [0, -1, -19], [500, 999]]
    expected = [1, 2, 3, 0, -1, -19, 500, 999]
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 6
    seq_of_seq_of_int = [[1, 1], [1, 1, 1, 1], [1, 1, 1]]
    expected = []
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 7
    seq_of_seq_of_int = [[-100000], [], [], [], []]
    expected = []
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 8
    seq_of_seq_of_int = [[-1, -1, 2], [3, 4, 1], [0, 5, 4]]
    expected = []
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    # Test 9
    seq_of_seq_of_int = [[100, 100], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    expected = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    run_and_print_test([seq_of_seq_of_int], expected, test_results,
                       format_string, problem2b)

    print_summary_of_test_results(test_results)


def problem2b(seq_seq_of_int):
    """
    What comes in:
      -- A non-empty sequence of sequences of integers with the first of
          those sequences being guaranteed non empty. i.e.,
          seq_seq_of_int[0] is non-empty.

    What goes out:
      -- A list containing the integers in seq_seq_of_int that are
          strictly SMALLER  than the smallest number in seq_seq_of_int[0].

    Side effects: NONE

    Examples:
      -- problem2b([[0, 1, 2, -1, 5],
                   [-5, -10, 5, 0, 2], [1, 2, 3],
                   [], [-100]])
         returns [-5, -10, -100] since:
            (1) -1 is the smallest number in seq_seq_of_int[0]
            (2) -5, -10, -100 are all smaller than -1

         NOTE: -1 is not included in the returned list.

         NOTE: since all numbers in seq_seq_of_int[0] are greater than
         or equal to -1, no number from seq_seq_of_int[0] will appear in the
         returned list.

      -- problem2b([[0], [-1, -2, 3], [0], [-10], []))
          returns [-1, -2, -10] since:
            (1) 0 is the smallest number in seq_seq_of_int[0]
            (2) -1, -2, -10 are all smaller than 0

      -- problem2b([[-1000], [1, 2, 3], [0, -1, -19], [500, 999]])
          returns [] since:
            (1) 1000 is the smallest number in seq_seq_of_int[0]
            (2) no other number anywhere in seq_seq_of_int is < 1000

      -- problem2b([3, 9, 8, 7], [1, 3, 2], [-10], [3], [3, 4], [1, 2])
          returns [1, 2, -10, 1, 2] since:
            (1) 3 is the smallest number in seq_seq_of_int[0]
            (2) 1, 2, -10, 1, 2 are all < 3:
                (2.1) 1, 2 are < 3 in seq_seq_of_int[1]
                (2.2) -10 is < 3 in seq_seq_of_int[2]
                (2.3) 1, 2 are < 3 in seq_seq_of_int[5]

    Type hints:
    :type seq_seq_of_int: list[list[int]]
    :rtype: list[int]
    """
    smallest = seq_seq_of_int[0][0]
    smaller = []
    for k in range(1, len(seq_seq_of_int[0])-1):
        if seq_seq_of_int[0][k] < smallest:
            smallest = seq_seq_of_int[0][k]
    for j in range(1, len(seq_seq_of_int)):
        for n in range(len(seq_seq_of_int[j])):
            if seq_seq_of_int[j][n] < smallest:
                smaller.append(seq_seq_of_int[j][n])
    return smaller
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


def check_problem3a_sequences(seq_of_seq_of_words, expected_sequence,
                              test_results):
    """
    Check the resulting sequences for problem3a
    """
    print()
    print("  Expected sequence after the call: {}".format(expected_sequence))
    print("  Actual sequence after the call: {}".format(seq_of_seq_of_words))
    if len(seq_of_seq_of_words) != len(expected_sequence):
        test_results[0] -= 1
        test_results[1] += 1
        print("  *** FAILED the above test: The content of seq_seq "
              "are not correct! ***", color='red')
        return

    for k in range(len(seq_of_seq_of_words)):
        for j in range(len(seq_of_seq_of_words[k])):
            try:
                if seq_of_seq_of_words[k][j] != expected_sequence[k][j]:
                    test_results[0] -= 1
                    test_results[1] += 1
                    print(
                        "  *** FAILED the above test: The content of seq_seq "
                        "are not correct! ***", color='red')
                    return
            except:
                test_results[0] -= 1
                test_results[1] += 1
                print("  *** FAILED the above test: The content of seq_seq "
                      "are not correct! ***", color='red')
                return

    print("  PASSED the above test -- good!", color='blue')




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
