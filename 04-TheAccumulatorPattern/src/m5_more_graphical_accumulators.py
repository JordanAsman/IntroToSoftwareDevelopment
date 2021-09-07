"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python. 
  
Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Jordan.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg

# -----------------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# -----------------------------------------------------------------------------

##############################################################################
# DONE: 2. Read the following, then change its _TODO_ to DONE.
#   Throughout these exercises, you must use  RANGE  statements.
#   At this point of the course, you are restricted to the SINGLE-ARGUMENT
#   form of RANGE statements, like this:
#         range(blah):
#   There is a MULTIPLE-ARGUMENT form of RANGE statements (e.g. range(a, b))
#   but you are NOT permitted to use the MULTIPLE-ARGUMENT form yet, for
#   pedagogical reasons.  Change the above _TODO_ to DONE after reading this.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_draw_squares_from_circle()
    run_test_draw_circles_from_rectangle()
    run_test_draw_lines_from_rectangles()


def run_test_draw_squares_from_circle():
    """ Tests the   draw_squares_from_circle  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  draw_squares_from_circle  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TWO tests on ONE window.
    # -------------------------------------------------------------------------
    title = "Tests 1 and 2 of DRAW_SQUARES_FROM_CIRCLE: "
    title = title + " 7 little squares from green circle, 4 big squares"
    window1 = rg.RoseWindow(650, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = "green"
    draw_squares_from_circle(7, circle, window1)

    # Test 2:
    circle = rg.Circle(rg.Point(350, 70), 50)
    draw_squares_from_circle(4, circle, window1)
    window1.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # A third test on ANOTHER window.
    # -------------------------------------------------------------------------
    title = "Test 3 of DRAW_SQUARES_FROM_CIRCLE: "
    title += " 20 teeny squares from blue circle!"
    window2 = rg.RoseWindow(525, 300, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 50), 10)
    circle.fill_color = "blue"
    draw_squares_from_circle(20, circle, window2)

    window2.close_on_mouse_click()


def draw_squares_from_circle(n, circle, window):
    """
    What comes in:  Three arguments:
      -- A positive integer n.
      -- An rg.Circle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   3_draw_squares_from_circle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Circle on the given rg.RoseWindow.
      Then draws  n  rg.Squares on the given rg.RoseWindow, such that:
        -- The first rg.Square circumscribes the given rg.Circle.
        -- Each subsequent rg.Square has its upper-left quarter
             on top of the lower-right quarter of the previous rg.Square,
             so that the squares form an overlapping sequence
             that goes down and to the right.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n:      int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    circle.attach_to(window)
    cntr_x = circle.center.x
    cntr_y = circle.center.y
    rad = circle.radius
    length = 2 * rad
    corner_x = cntr_x - rad
    corner_y = cntr_y - rad
    for k in range(n + 1):
        sq = rg.Square(rg.Point(cntr_x, cntr_y), length)
        sq.attach_to(window)
        corner_x = corner_x + rad
        corner_y = corner_y + rad
        cntr_x = corner_x + rad
        cntr_y = corner_y + rad
    window.render()
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #  _
    #  CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #      as in   draw_row_of_circles   in m1e,
    #      instead of directly using the loop variable.
    #  ########################################################################
    #  HINT: To figure out the code that computes the necessary
    #        positions of each square,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    #  ########################################################################
    # -------------------------------------------------------------------------


def run_test_draw_circles_from_rectangle():
    """ Tests the   draw_circles_from_rectangle  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  draw_circles_from_rectangle  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TWO tests on ONE window.
    # -------------------------------------------------------------------------
    title = "Tests 1 and 2 of DRAW_CIRCLES_FROM_RECTANGLE: "
    title = title + " 4 large circles and 5 small circles from a rectangle & 8 large circles and 3 small circles from a rectangle"
    window1 = rg.RoseWindow(720, 500, title)

    # Test 1:
    rectangle = rg.Rectangle(rg.Point(400, 250), rg.Point(440, 325))
    rectangle.fill_color = "green"
    rectangle.outline_color = "black"
    rectangle.outline_thickness = 5
    draw_circles_from_rectangle(4, 5, rectangle, window1)

    # Test 2:
    rectangle = rg.Rectangle(rg.Point(600, 400), rg.Point(500, 450))
    rectangle.fill_color = "blue"
    rectangle.outline_color = "red"
    rectangle. outline_thickness = 3
    draw_circles_from_rectangle(8, 3, rectangle, window1)
    window1.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # A third test on ANOTHER window.
    # -------------------------------------------------------------------------
    title = "Test 3 of DRAW_CIRCLES_FROM_RECTANGLE: "
    title += " 6 large circles and 10 small circles from a rectangle!"
    window2 = rg.RoseWindow(620, 380, title)

    # Test 3:
    rectangle = rg.Rectangle(rg.Point(375, 330), rg.Point(350, 280))
    rectangle.fill_color = "yellow"
    rectangle.outline_color = "brown"
    rectangle.outline_thickness = 5
    draw_circles_from_rectangle(6, 10, rectangle, window2)

    window2.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the  draw_circles_from_rectangle  function
    #   defined below.  Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #  ########################################################################
    #  HINT: Consider using the same test cases as suggested by the
    #    pictures in  4_draw_circles_from_rectangle.pdf   in this project.
    #    Follow the same form as the example in a previous problem.
    #  ########################################################################
    # -------------------------------------------------------------------------


def draw_circles_from_rectangle(m, n, rectangle, window):
    """
    What comes in:  Four arguments:
      -- Positive integers m and n.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   4_draw_circles_from_rectangle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Rectangle on the given rg.RoseWindow.
      Then draws  m  rg.Circles on the given rg.RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the height
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately to the left of the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately to the left
             of the previous rg.Circle, so that the circles form a row
             that goes to the left.
        -- Each rg. Circle has the same fill_color as the given
             rg.Rectangle (and has no outline_color).
      Then draws  n  rg.Circles on the given RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the width
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately above the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately above the previous
             rg.Circle, so that the circles form a column that goes up.
        -- Each rg.Circle has the same outline_color as the given
             rg.Rectangle (and has no fill_color).
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type m:         int
      :type n:         int
      :type rectangle: rg.Rectangle
      :type window:    rg.RoseWindow
    """
    rectangle.attach_to(window)
    rad1 = rectangle.get_width() / 2
    rad2 = rectangle.get_height() / 2
    cntr_x = rectangle.get_center().x
    cntr_y = rectangle.get_center().y
    cntr_x1 = rectangle.get_center().x - rad2
    cntr_y1 = rectangle.get_center().y - rad2
    cntr_x2 = rectangle.get_center().x - rad1
    cntr_y2 = rectangle.get_center().y - rad1
    for _ in range(n):
        center = rg.Point(cntr_x, cntr_y1 - rad1)
        circle = rg.Circle(center, rad1)
        circle.outline_thickness = 1
        cntr_y1 = cntr_y1 - 2 * rad1
        circle.attach_to(window)
    for _ in range(m):
        center = rg.Point(cntr_x2 - rad2, cntr_y)
        circle = rg.Circle(center, rad2)
        circle.outline_thickness = 1
        circle.fill_color = rectangle.fill_color
        cntr_x2 = cntr_x2 - 2 * rad2
        circle.attach_to(window)
    window.render()
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #  _
    #  CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #      as in   draw_row_of_circles   in m1e,
    #      instead of directly using the loop variable.
    #  ########################################################################
    #  HINT: To figure out the code that computes the necessary
    #        positions of each circle,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    #  ########################################################################
    # -------------------------------------------------------------------------


def run_test_draw_lines_from_rectangles():
    """ Tests the   draw_lines_from_rectangles  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  draw_lines_from_rectangles  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # TWO tests on ONE window.
    title = "Tests 1 & 2 of DRAW_LINES_FROM_RECTANGLES:"
    title += "  5 lines, 8 lines!"
    window1 = rg.RoseWindow(900, 400, title)

    rectangle1 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
    rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
    rectangle1.outline_color = "red"
    rectangle2.outline_color = "blue"
    draw_lines_from_rectangles(rectangle1, rectangle2, 5, window1)

    rectangle1 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
    rectangle2 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
    rectangle2.outline_color = "green"
    draw_lines_from_rectangles(rectangle1, rectangle2, 8, window1)

    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = "Test 3 of DRAW_LINES_FROM_RECTANGLES:  11 lines!"
    window2 = rg.RoseWindow(700, 700, title)

    rectangle1 = rg.Rectangle(rg.Point(550, 200), rg.Point(650, 100))
    rectangle2 = rg.Rectangle(rg.Point(600, 50), rg.Point(650, 75))
    rectangle1.outline_color = "brown"
    rectangle2.outline_color = "cyan"
    rectangle2.outline_thickness = 10
    draw_lines_from_rectangles(rectangle1, rectangle2, 11, window2)

    window2.close_on_mouse_click()


def draw_lines_from_rectangles(rectangle1, rectangle2, n, window):
    """
    What comes in:  Four arguments:
      -- Two rg.Rectangles.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   5_draw_lines_from_rectangles.pdf   in this project
      for pictures that may help you better understand
      the following specification:

      First draws the given rg.Rectangles on the given rg.RoseWindow.
      Then draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The 1st rg.Line goes from the center of one of the
             1st rg.Rectangle to the center of the 2nd rg.Rectangle.
        -- The 2nd rg.Line goes from the lower-left corner of the
              1st rg.Rectangle and is parallel to the 1st rg.Line,
              with the same length and direction as the 1st rg.Line.
        -- Subsequent rg.Lines are shifted from the previous rg.Line in
              the same way that the 2nd rg.Line is shifted from the 1st.
        -- Each of the rg.Lines has thickness 5.
        -- The colors of the rg.Lines alternate, as follows:
             - The 1st, 3rd, 5th, ... rg.Line has color R1_color
             - The 2nd, 4th, 6th, ... rg.Line has color R2_color
            where
             - R1_color is the outline color of the 1st rg.Rectangle
             - R2_color is the outline color of the 2nd rg.Rectangle
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rectangle1: rg.Rectangle
      :type rectangle2: rg.Rectangle
      :type n:          int
      :type window:     rg.RoseWindow
      """
    rectangle1.attach_to(window)
    rectangle2.attach_to(window)
    R1_color = rectangle1.outline_color
    R2_color = rectangle2.outline_color
    cntr_x1 = rectangle1.get_center().x
    cntr_y1 = rectangle1.get_center().y
    cntr_x2 = rectangle2.get_center().x
    cntr_y2 = rectangle2.get_center().y
    corner_x1 = rectangle1.get_lower_left_corner().x
    corner_y1 = rectangle1.get_upper_left_corner().y
    shift_x = cntr_x1 - corner_x1
    shift_y = cntr_y1 - corner_y1
    for k in range(n):
        start = rg.Point(cntr_x1, cntr_y1)
        end = rg.Point(cntr_x2, cntr_y2)
        cntr_x1 = cntr_x1 - shift_x
        cntr_y1 = cntr_y1 + shift_y
        cntr_x2 = cntr_x2 - shift_x
        cntr_y2 = cntr_y2 + shift_y
        line = rg.Line(start, end)
        line.thickness = 5
        if (k + 1) % 2 == 0:
            line.color = R2_color
        else:
            line.color = R1_color
        line.attach_to(window)
    window.render()
    # -------------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #          Tests have been written for you (above).
    #  _
    #  CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #      as in   draw_row_of_circles   in m1e,
    #      instead of directly using the loop variable.
    #  ########################################################################
    #  HINT: To figure out the code that computes the necessary
    #        endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    #  ########################################################################
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
