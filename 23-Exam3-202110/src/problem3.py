"""
Exam 3, Problem 3

Authors: David Mutchler, Sana Ebrahimi, Mohammad Noureddine, their colleagues,
         and Jordan Asman
"""  # DONE: 1. Put your name in the line above

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Test the   problem3   function"""
    print()
    print("--------------------------------------------------")
    print("Testing the   problem3   function:")
    print("--------------------------------------------------")

    print()
    print('Test 1 of christmas_tree: r=3')
    christmas_tree(3)

    print()
    print('Test 2 of christmas_tree: r=4')
    christmas_tree(4)

    print()
    print('Test 3 of christmas_tree: r=5')
    christmas_tree(5)

    print()
    print('Test 3 of christmas_tree: r=6')
    christmas_tree(6)

    print()
    print('Test 4 of christmas_tree: r=8')
    christmas_tree(8)

    print()
    print('Test 4 of christmas_tree: r=9')
    christmas_tree(9)


def christmas_tree(r):
    """
    What comes in:
      -- An integer r that is > 2 and that is <= 9

    What goes out:
      -- Nothing

    Side effects:
      -- Prints the shape of a christmas tree surrounded by numbers in the
          patterns shown in the examples below.

          All shown examples are aligned to the left side of your console. In
          other words, you don't need to worry about leading spaces except in
          the last row.

          For the last row, we always print three '*' shifted appropriately.

    Examples:
      -- christmas_tree(9):
      123456789*987654321
      12345678***87654321
      1234567*****7654321
      123456*******654321
      12345*********54321
      1234***********4321
      123*************321
      12***************21
      1*****************1
              ***


      -- christmas_tree(3):
         123*321
         12***21
         1*****1
           ***


      -- christmas_tree(4):
         1234*4321
         123***321
         12*****21
         1*******1
            ***


      -- christmas_tree(8):
         12345678*87654321
         1234567***7654321
         123456*****654321
         12345*******54321
         1234*********4321
         123***********321
         12*************21
         1***************1
                ***


                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

        ** IMPORTANT: You are NOT allowed to use string multiplication or **
        **             string manipulation functions.                     **

        Hint: You might find it useful to count the number of stars you have to
        print and use a separate counter for those.
    """
    for k in range(r):
        for j in range(r-k):
            print(j+1, end='')
        for m in range((k+1)*2-1):
            print('*', end='')
        for n in range(r-k, 0, -1):
            print(n, end='')
        print()
    for l in range(r-1):
        print(' ', end='')
    for o in range(r-1, r+2):
        print('*', end='')
    # -----------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # -----------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("ERROR - While running this test,")
        print("your code raised the following exception:")
        print()
        time.sleep(1)
        raise
