"""
Exam 1, problem 3.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Jordan Asman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  problem3  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # ONE test on ONE window.
    title = "Test 1 of Problem 3"
    window = rg.RoseWindow(350, 250, title)

    # Test 1:
    rectangle = rg.Rectangle(rg.Point(175, 50), rg.Point(325, 80))
    rectangle.fill_color = "yellow"
    rectangle.outline_thickness = 5
    circle = rg.Circle(rg.Point(100, 150), 50)
    problem3(rectangle, circle, "blue", window)
    window.close_on_mouse_click()

    # TWO MORE tests on ANOTHER window
    title = "Tests 2 & 3 of Problem 3e"
    window = rg.RoseWindow(700, 350, title)

    # Test 2:
    rectangle = rg.Rectangle(rg.Point(150, 250), rg.Point(50, 200))
    rectangle.outline_thickness = 20
    circle = rg.Circle(rg.Point(75, 50), 25)
    circle.fill_color = "yellow"
    problem3(rectangle, circle, "forest green", window)
    window.continue_on_mouse_click()

    # Test 3:
    rectangle = rg.Rectangle(rg.Point(275, 250), rg.Point(425, 100))
    rectangle.fill_color = "pink"
    circle = rg.Circle(rg.Point(575, 250), 100)
    problem3(rectangle, circle, "black", window)
    window.close_on_mouse_click()

    # TWO MORE tests on ANOTHER window
    title = "Tests 4 & 5 of Problem 3"
    window = rg.RoseWindow(500, 200, title)

    # Test 4:
    rectangle = rg.Rectangle(rg.Point(70, 80), rg.Point(40, 30))
    rectangle.fill_color = "yellow"
    rectangle.outline_thickness = 15
    circle = rg.Circle(rg.Point(200, 35), 25)
    circle.fill_color = "black"
    problem3(rectangle, circle, "magenta", window)
    window.continue_on_mouse_click()

    # Test 5:
    rectangle = rg.Rectangle(rg.Point(430, 60), rg.Point(430, 140))
    rectangle.fill_color = "blue"
    rectangle.outline_thickness = 6
    circle = rg.Circle(rg.Point(350, 100), 40)
    problem3(rectangle, circle, "light blue", window)
    window.close_on_mouse_click()


def problem3(rectangle, circle, color, window):
    """
    See   problem3_pictures.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Rectangle.
      -- An rg.Circle
      -- A string that represents a color in RoseGraphics
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws, on the given rg.RoseWindow:
        a. The given rg.Rectangle.
        b. The given rg.Circle, but changing:
             -- its outline color to the given color, and
             -- its outline thickness to the given rg.Rectangle's
                    outline thickness.
        c. An rg.Square that:
             -- is a square (so its width and height are equal)
             -- is centered at the center of the given rg.Rectangle
             -- has width (and height) equal to the DIAMETER of the
                   given  *** rg.Circle ***   (see the picture for details)
            -- has outline color "red"
            -- has outline thickness 3
            -- is on top of the given rectangle if they overlap (to do this,
                 attach the new square AFTER attaching the given rectangle)

           Note: for full credit you must construct an rg.Square
           and not an rg.Rectangle that happens to form a square.
                .
      Must render but   ** NOT close **   the window.

    Type hints:
      :type rectangle: rg.Rectangle
      :type circle:    rg.Circle
      :type color:     str
      :type window:    rg.RoseWindow
    """
    rectangle.attach_to(window)
    circle.outline_color = color
    circle.outline_thickness = rectangle.outline_thickness
    circle.attach_to(window)
    square = rg.Square(rectangle.get_center(), circle.radius * 2)
    square.outline_color = 'red'
    square.outline_thickness = 3
    square.attach_to(window)
    window.render()
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
