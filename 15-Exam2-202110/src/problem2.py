"""
Exam 2, Problem 2

Authors: David Mutchler, Sana Ebrahimi, Mohammad Noureddine, their colleagues,
         and Jordan Asman
"""  # DONE: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    run_test_get_color()
    run_test_advance_color()
    run_test_advance_color_many_times()
    run_test_cars_waiting()
    run_test_cars_going_through()
    run_test_car_arrives_at_light()
    run_test_hazardous_intersection()
    run_test_clone_light()


###############################################################################
#  READ THIS:
#  We have worked hard to provide test cases that will expose most errors that
#  students might made, but it is very difficult to cover ALL possible errors!
#  We remind you:  Your code gets credit only if it CORRECT;
#    passing tests does not GUARANTEE correctness.
#
#  and READ THIS TOO:
#         ** ASK YOUR INSTRUCTOR FOR HELP ON ANY METHOD BELOW **
#         ** WHOSE SPECIFICATION AND/OR EXAMPLES YOU DO NOT UNDERSTAND. **
###############################################################################

###############################################################################
# DONE: 2.  READ the   TrafficLight   class defined below.
###############################################################################
class TrafficLight:
    """
    Represents a traffic light whose color is either
      "green", "yellow" or "red".
    """

    def __init__(self, color):
        """
        What comes in:
            - self
            - the color that the traffic light will start with.
        What goes out: nothing.
        Side effects:
            Stores the given color in an instance variable and sets whatever
            instance variables are needed by methods later in this problem.
        """
        self.color = color
        self.cars_wait = 0
        self.cars_passed = 0
        # ---------------------------------------------------------------------
        # DONE: 3.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement this method.
        # ---------------------------------------------------------------------

    def get_color(self):
        """
        What comes in:
            - self
        What goes out: Returns the current color of the traffic light.
        Side effects: None.
        Examples:
           light1 = TrafficLight("red")
           light2 = TrafficLight("green")
           color1 = light1.get_color()  # Sets  color1  to "red"
           color2 = light2.get_color()  # Sets  color2  to "green"

           light2.advance_color()  # Changes its color from "green" to "yellow"
                                   # See the next method.
           a = light1.get_color()  # Sets  a  to "red" (light is still "red")
           b = light2.get_color()  # Sets  b  to "yellow" (its CURRENT color)
        Type hints:
          :rtype: str
        """
        return self.color
        # ---------------------------------------------------------------------
        # DONE: 4.
        #   a. READ the above specification, including the Example.
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_get_color in main()
        #       This will test both your __init__ and get_color methods.
        # ---------------------------------------------------------------------

    def advance_color(self):
        """
        What comes in:
            - self
        Side effects:
          -- If this TrafficLight's current color is green,
               then this method changes it to yellow.
          -- If this TrafficLight's current color is yellow,
               then this method changes it to red.
          -- If this TrafficLight's current color is red,
               then this method changes it to green.
        What goes out:
          Returns the color of this TrafficLight AFTER advancing its color,
          per the Side effects above.  (See examples too.)
        Examples:
           light1 = TrafficLight("red")    # The color of  light1  is "red"
           light2 = TrafficLight("green")  # The color of  light2  is "green"

           a = light2.advance_color()  # The color of  light2  is now "yellow"
                                          # a is also "yellow".
           b = light1.advance_color()  # The color of  light1  is now "green"
                                         # b is also "green".
           c = light1.advance_color()  # The color of  light1  is now "yellow"
                                         # c is also "yellow".
           d = light1.advance_color()  # The color of  light1  is now "red"
                                         # d is also "red".
           e = light1.advance_color()  # The color of  light1  is now "green"
                                         # e is also "green".
           f = light2.advance_color()  # The color of  light2  is now "red"
                                         # f is also "red".
        Type hints:
          :rtype: str
        """
        if self.color == 'green':
            self.color = 'yellow'
            return self.color
        elif self.color == 'yellow':
            self.color = 'red'
            return self.color
        else:
            self.color = 'green'
            return self.color
        # ---------------------------------------------------------------------
        # DONE: 5.
        #   a. READ the above specification, including the Example.
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_advance_color in main()
        # ---------------------------------------------------------------------

    # Be sure to read the IMPORTANT note in the following specification!
    def advance_color_many_times(self, n):
        """
        What comes in:
            - self
            - A non negative integer n
        What goes out: Nothing (i.e., None)
        Side effects:
          Calls   advance_color   n times.
          NO CREDIT unless your code ACTUALLY CALLS  advance_color
        """
        for _ in range(n):
            self.advance_color()
        # ---------------------------------------------------------------------
        # DONE: 6.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_advance_color_many_times() in
        #       main()
        #  IMPORTANT:
        #    No credit unless your code ACTUALLY CALLS   advance_color
        # ---------------------------------------------------------------------

    def car_waits_at_light(self):
        """
        What comes in:
            - self
        What goes out: Nothing (i.e. None)
        Side effects:
          Mutates this TrafficLight to increase by 1 the number of cars
          waiting at this TrafficLight.
        """
        self.cars_wait = self.cars_wait + 1
        # ---------------------------------------------------------------------
        # DONE: 7.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement this method.  The NEXT method will test it.
        # ---------------------------------------------------------------------

    def get_number_of_cars_waiting(self):
        """
        What comes in:
            - self
        What goes out:
            - Returns the number of cars CURRENTLY waiting at this TrafficLight.
        Examples:
            light = TrafficLight('green')
            s = light.get_number_of_cars_waiting() # sets s to 0

            light.car_waits_at_light() # mutates light to increase the number
                                       # of cars waiting
            r = light.get_number_of_cars_waiting() # sets r to 1

            p = light.get_number_of_cars_waiting() # sets p to 1
            light.car_waits_at_light() # mutates light to increase the number
                                       # of cars waiting
            t = light.get_number_of_cars_waiting() # sets t to 2

        Side effects: None.
        Type hints:
          :rtype: int
        """
        return self.cars_wait
        # ---------------------------------------------------------------------
        # DONE: 8.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_cars_waiting in main()
        # ---------------------------------------------------------------------

    def cars_go_through_light(self):
        """
        What comes in:
          - self
        What goes out: Nothing (i.e. None)
        Side effects:
          Mutates this TrafficLight to make all the cars currently waiting
          at this TrafficLight to move through this TrafficLight. Those cars
          will NO LONGER be counted as waiting, instead they will be counted
          as gone through.
        """
        self.cars_passed = self.cars_passed + self.get_number_of_cars_waiting()
        self.cars_wait = 0
        # ---------------------------------------------------------------------
        # DONE: 9.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement this method.  Other methods will test it.
        # ---------------------------------------------------------------------

    def get_number_of_cars_through_light(self):
        """
        What comes in:
          - self
        What goes out:
           - Returns the number of cars that have gone through this TrafficLight
               since this TrafficLight was first constructed.
        Side effects: None.
        Examples:
            light = TrafficLight('green')
            light.car_waits_at_light()
            light.car_waits_at_light()
            light.car_waits_at_light()

            r = light.get_number_of_cars_waiting() # sets r to 3
            light.cars_go_through_light() # makes all cars go through

            s = light.get_number_of_cars_waiting() # sets s to 0
            t = light.get_number_of_cars_through_light() # sets t to 3

            light.car_waits_at_light()
            light.cars_go_through_light()
            x = light.get_number_of_cars_waiting() # sets x to 0
            y = light.get_number_of_cars_through_light() # sets y to 4

        Type hints:
          :rtype: int
        """
        return self.cars_passed
        # ---------------------------------------------------------------------
        # DONE: 10.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_cars_going_through() in main()
        # ---------------------------------------------------------------------

    def car_arrives_at_light(self):
        """
        What comes in:
            - self
        What goes out: Nothing (i.e. None)
        Side effects:
          Mutates this TrafficLight to simulate a car arriving at the
          TrafficLight and behaving like this:
            -- The arriving car will wait at this TrafficLight ONLY if
                 the color of this TrafficLight is currently "red".
            -- Otherwise (that is, if this TrafficLight is "yellow" or "green"),
                 the car goes through this TrafficLight WITHOUT waiting.

        Example:
            light = TrafficLight('red')
            r = light.get_number_of_cars_waiting() # sets r to 0

            light.car_arrives_at_light() # mutates light according to the above
                                         # side effects
            s = light.get_number_of_cars_waiting() # sets s to 1

            light.cars_go_through_light()
            t = light.get_number_of_cars_waiting() # sets t to 0
            p = light.get_number_of_cars_through_light() # sets p to 1

            light.advance_color()
            color = light.get_color()    # sets color to green
            light.car_arrives_at_light() # mutates light according to the above
                                         # side effects
            x = light.get_number_of_cars_waiting() # sets x to 0
            y = light.get_number_of_cars_through_light() # sets y to 2

        """
        if self.color == 'red':
            self.cars_wait += 1
        else:
            self.cars_passed += 1
        # ---------------------------------------------------------------------
        # DONE: 11.
        #   a. READ the above specification, pay special attention to the
        #      examples.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_car_arrives_at_light() in main()
        # ---------------------------------------------------------------------

    def is_hazardous_intersection(self, other_light):
        """
        What comes in:
          - self
          - The other TrafficLight at the intersection (named other_light)
        What goes out:
            - True if the intersection is hazardous,
            - False otherwise.
        where a TrafficLight is hazardous if:
          -- this TrafficLight is "red" AND there are cars waiting at it, AND
          -- the other_light is also "red" and there are cars waiting at it, too
        Side effects: None
        Examples:
            light = TrafficLight('green')
            other_light = TrafficLight('red')

            h = light.is_hazardous_intersection(other_light) # sets h to False

            light.advance_color_many_times(2)
            color = light.get_color() # sets color to red
            h2 = light.is_hazardous_intersection(other_light) # sets h2 to False

            light.car_waits_at_light()
            other_light.car_waits_at_light()
            h3 = light.is_hazardous_intersection(other_light) # sets h3 to True
            h4 = other_light.is_hazardous_intersection(light) # sets h4 to True

            other_light.advance_color()
            h5 = light.is_hazardous_intersection(other_light) # set h5 to False
        Type hints:
          :type other_light: TrafficLight
          :rtype: bool
        """
        if self.color == 'red' and self.cars_wait > 0 and other_light.color == 'red' and other_light.cars_wait > 0:
            return True
        return False
        # ---------------------------------------------------------------------
        # DONE: 12.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_hazardous_intersection() in
        #       main()
        # ---------------------------------------------------------------------

    def clone(self):
        """
        What comes in:
          - self
        What goes out:
          - A new TrafficLight with the same color, number of cars waiting,
              and number of cars that have gone through this TrafficLight.
        Side effects: None.
        Type hints:
          :rtype: TrafficLight
        """
        color = self.get_color()
        new_light = TrafficLight(color)
        new_light.cars_wait = self.get_number_of_cars_waiting()
        new_light.cars_passed = self.get_number_of_cars_through_light()
        return new_light
        # ---------------------------------------------------------------------
        # DONE: 13.
        #   a. READ the above specification.
        #        ** ASK QUESTIONS AS NEEDED. **
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #       Uncomment the call to run_test_clone_light() in main()
        # ---------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def run_test_get_color():
    print()
    print('-----------------------------------------------------------')
    print('Testing the  get_color  method of the TrafficLight class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1
    tf = TrafficLight('green')
    color = tf.get_color()
    passed = passed and assert_eq_variable_type('tf', tf, TrafficLight)
    passed = passed and assert_eq_variable_type('color', color, str)
    passed = passed and assert_eq_variable_value('color', color, 'green')

    # Test 2
    tf = TrafficLight('red')
    color = tf.get_color()
    passed = passed and assert_eq_variable_type('tf', tf, TrafficLight)
    passed = passed and assert_eq_variable_type('color', color, str)
    passed = passed and assert_eq_variable_value('color', color, 'red')

    # Test 3
    tf = TrafficLight('yellow')
    color = tf.get_color()
    passed = passed and assert_eq_variable_type('tf', tf, TrafficLight)
    passed = passed and assert_eq_variable_type('color', color, str)
    passed = passed and assert_eq_variable_value('color', color, 'yellow')

    # Test 4
    tf2 = TrafficLight(tf.get_color())
    tf2_color = tf2.get_color()
    passed = passed and assert_eq_variable_type('tf2', tf2, TrafficLight)
    passed = passed and assert_eq_variable_type('tf2_color', tf2_color, str)
    passed = passed and assert_eq_variable_value('tf2_color', tf2_color,
                                                 tf.get_color())

    if passed:
        print("Good Job, all tests of run_test_get_color PASSED!", color='blue')
    else:
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def run_test_advance_color():
    """ Test the advance color method """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  advance_color  method of the TrafficLight class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1
    tf = TrafficLight('green')
    starting_color = tf.get_color()
    passed = passed and assert_eq_variable_value('starting_color',
                                                 starting_color, 'green')
    # green -> yellow
    y = tf.advance_color()
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 'yellow')
    passed = passed and assert_eq_variable_type('y', y, str)
    # yellow -> red
    r = tf.advance_color()
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 'red')
    passed = passed and assert_eq_variable_type('r', r, str)
    # red -> green
    g = tf.advance_color()
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 starting_color)
    passed = passed and assert_eq_variable_type('g', g, str)

    # Test 2
    tf = TrafficLight('red')
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 'red')
    passed = passed and assert_eq_variable_value('tf.color', tf.advance_color(),
                                                 'green')
    passed = passed and assert_eq_variable_value('tf.color', tf.advance_color(),
                                                 'yellow')
    passed = passed and assert_eq_variable_value('tf.color', tf.advance_color(),
                                                 'red')

    # Test 3
    tf = TrafficLight('green')
    advance_list = [tf.advance_color() for _ in range(3)]
    passed = passed and assert_eq_variable_value('color_list', advance_list,
                                                 ['yellow', 'red', 'green'])

    if passed:
        print("Good Job, all tests of run_test_advance_color PASSED!",
              color='blue')
    else:
        print()
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def run_test_advance_color_many_times():
    """ Test the advance color many times method """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  advance_color_many_times  method of the TrafficLight '
          'class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1
    tf = TrafficLight('green')
    color = tf.advance_color()
    passed = passed and assert_eq_variable_value('tf.color', color, 'yellow')
    tf.advance_color_many_times(1)
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 'red')
    color = tf.get_color()
    tf.advance_color_many_times(0)
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 color)

    # Test 2
    tf = TrafficLight('red')
    tf.advance_color_many_times(2)
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 'yellow')

    # Test 3
    for color in ['green', 'red', 'yellow']:
        tf = TrafficLight(color)
        tf.advance_color_many_times(3)
        passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                     color)

    # Test 4
    tf = TrafficLight('green')
    tf2 = TrafficLight('green')
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 tf2.get_color())
    tf.advance_color()
    tf2.advance_color_many_times(1)
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 tf2.get_color())
    for k in range(20):
        tf2.advance_color_many_times(k)
        for _ in range(k):
            tf.advance_color()
        passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                     tf2.get_color())

    if passed:
        print("Good Job, all tests of run_test_advance_color_many_times "
              "PASSED!", color='blue')
    else:
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def run_test_cars_waiting():
    """ Test the cars waiting methods of the class """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  cars_waiting  methods of the TrafficLight class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1
    tf = TrafficLight('green')
    # By now, the traffic light must have at least two instance variables
    passed = passed and assert_eq_variable_value('tf.number_of_cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    tf.car_waits_at_light()
    passed = passed and assert_eq_variable_value('tf.number_of_cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 1)

    # Test 2
    tf = TrafficLight('red')
    for k in range(1000):
        tf.car_waits_at_light()
        if not assert_eq_variable_value('tf.number_of_cars_waiting',
                                        tf.get_number_of_cars_waiting(), k + 1):
            passed = False
            break

    if passed:
        print("Good Job, all tests of run_test_cars_waiting PASSED!",
              color='blue')
    else:
        print()
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def run_test_cars_going_through():
    """ Test the cars going through mechanism """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  cars_going_through  methods of the TrafficLight class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1: simple case
    tf = TrafficLight('green')
    tf.car_waits_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 1)
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 1)

    # Test 2: checking other colors
    tf = TrafficLight('yellow')
    tf.car_waits_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 1)
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 1)

    # Test 3: checking other colors
    tf = TrafficLight('red')
    tf.car_waits_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 1)
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 1)

    # Test 4: naive case
    tf = TrafficLight('green')
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 0)

    # Test 5: combining things
    tf = TrafficLight('yellow')
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    for _ in range(100):
        tf.car_waits_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 100)
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 100)
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 100)
    tf.car_waits_at_light()
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 101)

    if passed:
        print("Good Job, all tests of run_test_cars_going_through PASSED!",
              color='blue')
    else:
        print()
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def run_test_car_arrives_at_light():
    """ Test a car's arrival at the light """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  car_arrives_at_light  method of the TrafficLight '
          'class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1: Car arrives with a green light
    tf = TrafficLight('green')
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 1)

    # Test 2: advance the light
    tf.advance_color()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 2)

    # Test 3: advance the light again
    tf.advance_color()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 1)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 2)

    # Test 4: combining cars waiting with car arrivals
    tf = TrafficLight('red')
    tf.car_waits_at_light()
    tf.car_waits_at_light()
    tf.car_waits_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 3)
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 4)
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 5)

    # Test 5: light is changing
    tf.advance_color()
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 5)
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 1)
    tf.cars_go_through_light()
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 6)
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 7)
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)

    # Test 6: cars arrive and light changes again
    tf.advance_color()
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 8)
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)

    tf.advance_color()
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 8)
    passed = passed and assert_eq_variable_value('cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 1)

    if passed:
        print("Good Job, all tests of run_test_car_arrives_at_light PASSED!",
              color='blue')
    else:
        print()
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def run_test_clone_light():
    """ Test the cloning function """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  clone  method of the TrafficLight class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1: Basic cloning
    tf = TrafficLight('green')
    tf.car_waits_at_light()
    tf.cars_go_through_light()
    tf.car_waits_at_light()

    clone = tf.clone()
    passed = passed and assert_eq_variable_type('clone', clone, TrafficLight)
    passed = passed and assert_eq_variable_value('clone.color',
                                                 clone.get_color(),
                                                 tf.get_color())
    passed = passed and assert_eq_variable_value('clone.cars_waiting',
                                                 clone.get_number_of_cars_waiting(),
                                                 tf.get_number_of_cars_waiting())
    passed = passed and assert_eq_variable_value('clone.cars_through',
                                                 clone.get_number_of_cars_through_light(),
                                                 tf.get_number_of_cars_through_light())

    # Test 2: Make sure they are not references to each other
    tf = TrafficLight('red')
    tf.car_arrives_at_light()
    clone = tf.clone()

    tf.advance_color()
    tf.cars_go_through_light()
    tf.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('tf.color', tf.get_color(),
                                                 'green')
    passed = passed and assert_eq_variable_value('clone.color',
                                                 clone.get_color(), 'red')

    passed = passed and assert_eq_variable_value('tf.cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('tf.cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 2)

    passed = passed and assert_eq_variable_value('clone.cars_waiting',
                                                 clone.get_number_of_cars_waiting(),
                                                 1)
    passed = passed and assert_eq_variable_value('clone.cars_through',
                                                 clone.get_number_of_cars_through_light(),
                                                 0)

    # Test 3: More manipulation to make sure no mutation is happening
    for _ in range(100):
        clone.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('tf.cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('tf.cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 2)

    passed = passed and assert_eq_variable_value('clone.cars_waiting',
                                                 clone.get_number_of_cars_waiting(),
                                                 101)
    passed = passed and assert_eq_variable_value('clone.cars_through',
                                                 clone.get_number_of_cars_through_light(),
                                                 0)
    clone.cars_go_through_light()
    clone.advance_color_many_times(2)
    clone.car_arrives_at_light()
    passed = passed and assert_eq_variable_value('tf.cars_waiting',
                                                 tf.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('tf.cars_through',
                                                 tf.get_number_of_cars_through_light(),
                                                 2)

    passed = passed and assert_eq_variable_value('clone.cars_waiting',
                                                 clone.get_number_of_cars_waiting(),
                                                 0)
    passed = passed and assert_eq_variable_value('clone.cars_through',
                                                 clone.get_number_of_cars_through_light(),
                                                 102)

    if passed:
        print("Good Job, all tests of run_test_clone PASSED!",
              color='blue')
    else:
        print()
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def run_test_hazardous_intersection():
    """ Test the hazardous intersection method """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  is_hazardous_intersection  method of the TrafficLight '
          'class.')
    print('-----------------------------------------------------------')

    passed = True
    # Test 1
    light = TrafficLight('green')
    other_light = TrafficLight('green')
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 light.is_hazardous_intersection(
                                                     other_light),
                                                 False)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 other_light.is_hazardous_intersection(
                                                     light),
                                                 False)

    # Test 2
    light.advance_color_many_times(2)
    other_light.advance_color_many_times(2)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 light.is_hazardous_intersection(
                                                     other_light),
                                                 False)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 other_light.is_hazardous_intersection(
                                                     light),
                                                 False)

    # Test 3
    light.car_arrives_at_light()
    other_light.car_waits_at_light()
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 light.is_hazardous_intersection(
                                                     other_light),
                                                 True)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 other_light.is_hazardous_intersection(
                                                     light),
                                                 True)

    # Test 4
    light.cars_go_through_light()
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 light.is_hazardous_intersection(
                                                     other_light),
                                                 False)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 other_light.is_hazardous_intersection(
                                                     light),
                                                 False)

    # Test 5
    light.car_waits_at_light()
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 light.is_hazardous_intersection(
                                                     other_light),
                                                 True)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 other_light.is_hazardous_intersection(
                                                     light),
                                                 True)
    # Test 6
    other_light.advance_color()
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 light.is_hazardous_intersection(
                                                     other_light),
                                                 False)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 other_light.is_hazardous_intersection(
                                                     light),
                                                 False)

    # Test 7
    other_light.advance_color_many_times(2)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 light.is_hazardous_intersection(
                                                     other_light),
                                                 True)
    passed = passed and assert_eq_variable_value('is_hazardous',
                                                 other_light.is_hazardous_intersection(
                                                     light),
                                                 True)

    if passed:
        print("Good Job, all tests of run_test_is_hazardous_intersection "
              "PASSED!", color='blue')
    else:
        print()
        print("At least one of the test cases FAILED. Read the specification\n"
              "  and update your code.", color='red')


def assert_eq_variable_type(name, var, expected_type):
    """
    Soft assert that a variable is of a given type

    :param name: the name of the variable
    :param var: the variable to check
    :param expected_type: the type that the variable must be of
    """
    if not isinstance(var, expected_type):
        explanation = """The object {} should be of type {} but it is not.
    Perhaps your code is returning something different?""".format(
            name,
            expected_type
        )
        print()
        print_failure_message()
        print_failure_message(explanation)
        return False
    return True


def assert_eq_variable_value(name, var, value):
    if type(var) is not type(value):
        explanation = """The objects {} and {} you are trying to compare
    have different types. Check that your code is returning a value of the 
    correct type""".format(name, str(value))
        print()
        print_failure_message()
        print_failure_message(explanation)
        return False

    if var != value:
        explanation = """The variable {0} should have value {1} but they are
    different. Make sure your implementation logic is correct.
        Expected: {1}
        Actual: {2}""".format(name, str(value), var)
        print()
        print_failure_message()
        print_failure_message(explanation)
        return False

    return True


def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=0.5):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message, flush=True, color="red")
    time.sleep(flush_time)


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
