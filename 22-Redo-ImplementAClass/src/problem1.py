"""
Exam 2, problem 2.
Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import typing
import testing_helper


###############################################################################
# The  main  function and the TODOs for you are after this:
###############################################################################
def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    # run_test_init()
    # run_test_fill()
    # run_test_pour()
    # run_test_pour_two()
    # run_test_double_sized_pot()
    # run_test_get_amount_filled()


###############################################################################
# The   CoffeePot   class (and its methods) begins here.
###############################################################################
class CoffeePot(object):
    """ Represents a pot that contains coffee. """

    def __init__(self, volume, coffee):
        """
        What comes in:
          -- self
          -- the volume of this CoffeePot (in ounces)
          -- the initial amount of coffee (in ounces) in this CoffeePot
               (You may assume that the given initial amount of coffee
                is less than or equal to the given volume.)
        What goes out: Nothing (i.e., None).
        Side effects:
           Sets instance variables:
              self.volume
              self.coffee
           to the given volume and amount of coffee, respectively.
        Examples:  See tests.
        """
        # ---------------------------------------------------------------------
        # TODO: 2.
        #   a. READ the above specification.
        #      READ the test case supplied in the testing section below.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        A FEW tests are already written (below), but they may not
        #        be adequate to expose all bugs.  Add more tests as desired.
        # ---------------------------------------------------------------------

    def fill(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        Side effects:
           Adds enough coffee to this CoffeePot to fill it up.
           For example, if this CoffeePot has volume 12 ounces
           and currently holds 4 ounces of coffee,
           then calling this method would change this CoffeePot's coffee to 12.
        """
        # ---------------------------------------------------------------------
        # TODO: 3.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------

    def pour(self, ounces):
        """
        What comes in:
          -- self
          -- a positive integer
        What goes out: Nothing (i.e., None).
        Side effects: Pours the given number of ounces of coffee
          from this CoffeePot, unless the given number of ounces
          would empty this CoffeePot, in which case the number of ounces of
          coffee in this CoffeePot is set to 0.
          For example, if this CoffeePot has volume 12 ounces
          and currently holds 7 ounces of coffee,
          then:
            -- calling this method with argument 4
                 would change this CoffeePot's coffee to 7 - 4 (which is 3),
            -- calling this method with argument 10
                 would change this CoffeePot's coffee to 0.
        """
        # ---------------------------------------------------------------------
        # TODO: 4.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------

    def pour_two(self, m, n, other_coffee_pot):
        """
         What comes in:
           -- self,
           -- two positive numbers, and
           -- another CoffeePot
         What goes out: Nothing (i.e., None).
         Side effects:
            Pours   m   ounces of coffee from this CoffeePot
            and   n  ounces of coffee from the given other_coffee_pot.
            ** MUST BE IMPLEMENTED by CALLING the  POUR  method appropriately.
         Type hints:
           :type m: int
           :type n: int
           :type other_coffee_pot: CoffeePot
        """
        # ---------------------------------------------------------------------
        # TODO: 5.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------

    def double_sized_pot(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Return a new CoffeePot that contains no coffee but whose volume
               is twice the volume of this CoffeePot.
        Side effects: None.
        """
        # ---------------------------------------------------------------------
        # TODO: 6.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------

    def get_amount_filled(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns the total amount of coffee
               that was put into this CoffeePot by calling its  fill  method.
               ** See the testing code for examples. **
        Side effects: None.
        """
        # ---------------------------------------------------------------------
        # TODO: 7.  Same instructions as per the previous, but for this method.
        # ---------------------------------------------------------------------


###############################################################################
# The TEST functions for the  CoffeePot  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the CoffeePot class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the CoffeePot class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    pot1 = CoffeePot(12, 7)
    run_test_instance_variables(pot1, 12, 7)

    # Test 2
    print('\nTest 2:')
    pot2 = CoffeePot(10, 0)
    run_test_instance_variables(pot2, 10, 0)

    # Test 3
    print('\nTest 3:')
    pot1 = CoffeePot(8, 8)
    run_test_instance_variables(pot1, 8, 8)


def run_test_fill():
    """ Tests the   fill   method of the CoffeePot class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   fill   method of the CoffeePot class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    pot1 = CoffeePot(12, 7)
    pot1.fill()
    run_test_instance_variables(pot1, 12, 12)

    # Test 2
    print('\nTest 2:')
    pot1 = CoffeePot(10, 0)
    pot1.fill()
    run_test_instance_variables(pot1, 10, 10)

    # Test 3
    print('\nTest 3:')
    pot3 = CoffeePot(8, 8)
    run_test_instance_variables(pot3, 8, 8)


def run_test_pour():
    """ Tests the   pour   method of the CoffeePot class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   pour   method of the CoffeePot class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    pot1 = CoffeePot(12, 7)
    pot1.pour(4)
    run_test_instance_variables(pot1, 12, 3)

    # Test 2
    print('\nTest 2:')
    pot2 = CoffeePot(12, 7)
    pot2.pour(10)
    run_test_instance_variables(pot2, 12, 0)

    # Test 3
    print('\nTest 3:')
    pot3 = CoffeePot(8, 8)
    pot3.pour(8)
    run_test_instance_variables(pot3, 8, 0)

    # Test 4
    print('\nTest 4:')
    pot3 = CoffeePot(6, 2)
    pot3.pour(0)
    run_test_instance_variables(pot3, 6, 2)


def run_test_pour_two():
    """ Tests the   pour_two   method of the CoffeePot class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   pour_two   method of the CoffeePot class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    pot1 = CoffeePot(12, 7)
    pot2 = CoffeePot(10, 6)
    pot1.pour_two(4, 1, pot2)
    run_test_instance_variables(pot1, 12, 3)
    run_test_instance_variables(pot2, 10, 5)

    # Test 2
    print('\nTest 2:')
    pot1 = CoffeePot(12, 11)
    pot2 = CoffeePot(10, 6)
    pot1.pour_two(8, 5, pot2)
    run_test_instance_variables(pot1, 12, 3)
    run_test_instance_variables(pot2, 10, 1)

    # Test 3
    print('\nTest 3:')
    pot1 = CoffeePot(12, 11)
    pot2 = CoffeePot(10, 5)
    pot1.pour_two(5, 8, pot2)
    run_test_instance_variables(pot1, 12, 6)
    run_test_instance_variables(pot2, 10, 0)

    # Test 4
    print('\nTest 4:')
    pot1 = CoffeePot(12, 10)
    pot2 = CoffeePot(10, 5)
    pot1.pour_two(20, 11, pot2)
    run_test_instance_variables(pot1, 12, 0)
    run_test_instance_variables(pot2, 10, 0)

    # Test 5
    print('\nTest 5:')
    pot1 = CoffeePot(12, 7)
    pot2 = CoffeePot(10, 6)
    pot2.pour_two(1, 4, pot1)
    run_test_instance_variables(pot1, 12, 3)
    run_test_instance_variables(pot2, 10, 5)


def run_test_double_sized_pot():
    """ Tests the   double_sized_pot   method of the CoffeePot class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   double_sized_pot   method of the CoffeePot class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    pot1 = CoffeePot(12, 7)
    pot2 = pot1.double_sized_pot()
    run_test_instance_variables(pot1, 12, 7)
    run_test_instance_variables(pot2, 24, 0)


def run_test_get_amount_filled():
    """ Tests the   get_amount_filled   method of the CoffeePot class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_amount_filled   method of the CoffeePot class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    pot1 = CoffeePot(12, 7)  # No coffee added yet
    run_test_instance_variables(pot1, 12, 7)
    print()
    expected = 0
    actual = pot1.get_amount_filled()
    print('Expected from get_amount_filled:', expected)
    print('                         Actual:', actual)
    print_result_of_test(expected, actual)

    # Test 1 continued
    print('\nTest 1a (continuation of Test 1):')
    pot1.fill()    # 5 ounces added
    run_test_instance_variables(pot1, 12, 12)
    print()
    expected = 5
    actual = pot1.get_amount_filled()
    print('Expected from get_amount_filled:', expected)
    print('                         Actual:', actual)
    print_result_of_test(expected, actual)

    # Test 1 continued
    print('\nTest 1b (continuation of Test 1):')
    pot1.pour(12)  # Pot is now empty
    pot1.fill()    # 12 ounces added, so now 5 + 12 ounces added
    run_test_instance_variables(pot1, 12, 12)
    print()
    expected = 5 + 12
    actual = pot1.get_amount_filled()
    print('Expected from get_amount_filled:', expected)
    print('                         Actual:', actual)
    print_result_of_test(expected, actual)

    # Test 1 continued
    print('\nTest 1c (continuation of Test 1):')
    pot1.pour(5)  # Pot now has 7 ounces; still 5 + 12 ounces added
    run_test_instance_variables(pot1, 12, 7)
    print()
    expected = 5 + 12
    actual = pot1.get_amount_filled()
    print('Expected from get_amount_filled:', expected)
    print('                         Actual:', actual)
    print_result_of_test(expected, actual)

    # Test 1 continued
    print('\nTest 1d (continuation of Test 1):')
    pot1.pour(6)  # Pot now has 1 ounce; still 5 + 12 ounces added
    run_test_instance_variables(pot1, 12, 1)
    print()
    expected = 5 + 12
    actual = pot1.get_amount_filled()
    print('Expected from get_amount_filled:', expected)
    print('                         Actual:', actual)
    print_result_of_test(expected, actual)

    # Test 1 continued
    print('\nTest 1e (continuation of Test 1):')
    pot1.fill()   # 11 ounces added, so now 5 + 12 + 11 ounces added
    run_test_instance_variables(pot1, 12, 12)
    print()
    expected = 5 + 12 + 11
    actual = pot1.get_amount_filled()
    print('Expected from get_amount_filled:', expected)
    print('                         Actual:', actual)
    print_result_of_test(expected, actual)

    # Test 1 continued
    print('\nTest 1f (continuation of Test 1):')
    pot1.pour(8)  # Pot now has 4 ounces; still 5 + 12 + 11 ounces added
    run_test_instance_variables(pot1, 12, 4)
    print()
    expected = 5 + 12 + 11
    actual = pot1.get_amount_filled()
    print('Expected from get_amount_filled:', expected)
    print('                         Actual:', actual)
    print_result_of_test(expected, actual)


###############################################################################
# The following are HELPER functions that display error messages in RED
# and help make it easier for us to write tests.
# Do NOT change any of the following.
###############################################################################
def run_test_instance_variables(pot, expected_volume, expected_coffee):
    """
    Tests whether the instance variables for the given Triangle
    are per the given expected values.
      -- Prints relevant messages.
      -- Returns True if all is OK, else returns False.
    """
    # noinspection PyBroadException
    try:
        return (run_test_type_of_object(pot) and
                run_test_types_of_instance_variables(pot) and
                run_test_values_of_instance_variables(
                    pot,
                    expected_volume,
                    expected_coffee))
    except Exception:
        something_unexpected_happened_in_our_testing_code()
        return False


def run_test_values_of_instance_variables(pot,
                                          expected_volume,
                                          expected_coffee):
    # Print the EXPECTED and ACTUAL values of the instance variables
    format_string = '  {:9} {:>4} {:>9}'
    print('  Testing instance variables:')
    print('            volume    coffee')
    print('            ------    ------')
    print(format_string.format('Expected:',
                               str(expected_volume),
                               str(expected_coffee)))
    print(format_string.format('Actual:', str(pot.volume), str(pot.coffee)))

    # Print a message indicating whether or not
    # the EXPECTED values are equal to the ACTUAL values.
    expected = (expected_volume, expected_coffee)
    actual = (pot.volume, pot.coffee)
    return print_result_of_test(expected, actual)


def something_unexpected_happened_in_our_testing_code():
    print_failure_message()
    explanation = (
            '  Something unexpected has happened in the testing \n' +
            '  code that we supplied.  You should probably\n' +
            '  SEEK HELP FROM YOUR INSTRUCTOR NOW.')
    print_failure_message(explanation)


def run_test_type_of_object(pot):
    """ Returns True if the argument is in fact a Triangle object """
    if isinstance(pot, CoffeePot):
        return True
    else:
        explanation = ('  The following object to test:\n' +
                       '     ' + str(pot) + '\n' +
                       '  should be a CoffeePot object,\n' +
                       '  but it is not.  Perhaps your code\n' +
                       '  returned something of the wrong type?')
        print_failure_message()
        print_failure_message(explanation)
        return False


def run_test_types_of_instance_variables(pot):
    """
    Returns True if the argument has the right instance variables
    and they are all numbers.
    """
    # If NONE of the expected instance variables exist,
    # then perhaps the only "problem" is that the  __init__  method
    # has not yet been implemented.
    attributes = dir(pot)
    if 'volume' not in attributes or 'coffee' not in attributes:
        explanation = (
                '  This object:\n' +
                '     ' + str(pot) + '\n' +
                '  should have these instance variables:\n' +
                '     self.volume\n' +
                '     self.coffee\n' +
                '  but it has lacks at least one of them.\n' +
                '  Perhaps you simply have not yet\n' +
                '  implemented the   __init__   method?\n' +
                '  (If so, implement it now.)\n' +
                '  Or perhaps you misspelled an instance variable?')
        print_failure_message()
        print_failure_message(explanation)
        return False

    return True


def is_list_of_strings(strings):
    return ((strings == [])
            or (isinstance(strings[0], str)
                and is_list_of_strings(strings[1:])))


def print_result_of_test(expected, actual):
    if are_equal(expected, actual):
        print("  PASSED the above test -- good!", color="blue")
        return True

    print_failure_message()

    # if isinstance(expected, list) or isinstance(expected, tuple):
    #     explanation = (
    #             '  For at least one of the above, its Expected value\n' +
    #             '  does not equal its Actual value.'
    #             'Note: the printed\n' +
    #             '  values are the actual values ROUNDED to 1 decimal place.')
    #     print_failure_message(explanation)

    return False


def are_equal(a, b):
    # We will treat two numbers as being "equal" if they are
    # the same when each is rounded to 12 decimal places.
    if isinstance(a, float) and isinstance(b, float):
        return round(a, 12) == round(b, 12)

    # For lists and tuples, their items have to be equal for the
    # lists/tuples to be equal.
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    # For all else, they must be equal in the "usual" way:
    return a == b


def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=0.5):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message, flush=True, color="red")
    time.sleep(flush_time)


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
