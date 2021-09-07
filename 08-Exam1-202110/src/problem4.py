"""
Exam 1, problem 4.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Jordan Asman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


def run_test_problem4():
    """ Tests the   problem4  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem4  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem4'
    window = rg.RoseWindow(300, 300, title)

    problem4(5, 50, 10, 250, 60, "blue", "green", "red", window)
    window.close_on_mouse_click()

    # TWO tests on ANOTHER window.
    title = 'Tests 2 and 3 of problem4'
    window = rg.RoseWindow(350, 400, title)

    problem4(3, 60, 20, 150, 120, "yellow", "black", "blue", window)
    window.continue_on_mouse_click()

    problem4(3, 260, 70, 310, 170, "magenta", "blue", "black", window)
    window.close_on_mouse_click()

    # TWO MORE tests on yet ANOTHER window.
    title = 'Tests 4 and 5 of problem4'
    window = rg.RoseWindow(300, 500, title)

    problem4(21, 30, 50, 130, 70, "red", "white", "blue", window)
    window.continue_on_mouse_click()

    problem4(8, 200, 10, 250, 60, "magenta", "blue", "black", window)
    window.close_on_mouse_click()


def problem4(number_of_rectangles, x1, y1, x2, y2, color1, color2,
             color3, window):
    """
    See   problem4_pictures.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- A positive integer for the number of rectangles to draw
      -- Four more positive integers x1, y1, x2, y2 that specify
           opposite corners of the first rectangle to draw
      -- Three colors, to be used as described below
      -- A rg.RoseWindow.
    What goes out:  Nothing (i.e., None).

    Side effects:
      1. Draws, on the given RoseWindow, rg.Rectangles such that:
           a.  There are the given  number_of_rectangles  rg.Rectangles.
           b.  The topmost rg.Rectangle has:
                -- upper-left corner is at (x1, y1)
                -- lower-right corner is at (x2, y2)
                -- outline thickness is 5
                -- fill color is the given color1
           c. For subsequent rg.Rectangles:
                -- They have the same size as the first rg.Rectangle.
                -- They are positioned immediately below the preceding
                     rg.Rectangle, as shown in the  problem4_pictures.pdf  file.
                -- Their outline thickness is 5 (like the first rg.Rectangle).
                -- Their fill color alternates:
                     -- The 1st rg.Rectangle uses color1
                     -- The 2nd rg.Rectangle uses color2
                     -- The 3rd rg.Rectangle uses color1
                     -- The 4th rg.Rectangle uses color2
                          etc.

      2. Draws, on the given RoseWindow, rg.Circles such that:
          a.  Each rg.Rectangle has a single rg.Circle associated with it.
                Hence, there are the given  number_of_rectangles  rg.Circles.
          b.  Each rg.Circle is centered at the center of the left side
               of its associated rg.Rectangle.
          c.  The diameter of each rg.Circle
                is the height of its associated rg.Rectangle.
          d.  The fill color of each rg.Circle is the given color3,
                and the outline thickness is 3.
          e.  Each rg.Circle is drawn on TOP of its associated rg.Rectangle.
               -- You can accomplish this by doing the   attach_to
                  for the rg.Circle AFTER doing the   attach_to
                  for its associated rg.Rectangle.

      Must render but   ** NOT close **   the window.

    Type hints:
      :type number_of_rectangles:  int
      :type x1:      int
      :type y1:      int
      :type x2:      int
      :type y2:      int
      :type color1:  str
      :type color2:  str
      :type color3:  str
      :type window:  rg.RoseWindow
    """
    shift = y2 - y1
    for k in range(number_of_rectangles):
        rec = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
        rec.outline_thickness = 5
        if (k + 1) % 2 == 1:
            rec.fill_color = color1
        else:
            rec.fill_color = color2
        rec.attach_to(window)
        cir = rg.Circle(rg.Point(x1, (y1 + y2) / 2), shift / 2)
        cir.fill_color = color3
        cir.outline_thickness = 3
        cir.attach_to(window)
        y1 = y1 + shift
        y2 = y2 + shift
    window.render()
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT: Implement this problem piece by piece, for example like this:
    #     Step 1: Draw the first rg.Rectangle.
    #     Step 2: Draw the remaining rg.Rectangles, but with no fill colors yet.
    #     Step 3: Draw the first rg.Circle.
    #     Step 4: Draw the remaining rg.Circles.
    #     Step 5: Get the fill colors of the rg.Rectangles to alternate
    #               between color1 and color2.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
