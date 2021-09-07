"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Jordan Asman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    two_circles()
    lines()
    circle_and_rectangle()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()
    circ1 = rg.Circle(rg.Point(200, 200), 50)
    circ2 = rg.Circle(rg.Point(100, 100), 30)
    circ2.fill_color = "aquamarine"
    circ1.attach_to(window)
    circ2.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #     -- ANY two rg.Circle objects that meet the criteria are fine.
    #     -- File  COLORS.txt  lists all legal color-names.
    #   Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines, for the thicker Line):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()
    line1 = rg.Line(rg.Point(10, 10), rg.Point(100, 100))
    line2 = rg.Line(rg.Point(150, 50), rg.Point(300, 400))
    line2.thickness = 5
    line1.attach_to(window)
    line2.attach_to(window)

    mid = line2.get_midpoint()
    midx = line2.get_midpoint().x
    midy = line2.get_midpoint().y

    print(mid)
    print(midx)
    print(midy)

    window.render()
    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #    -- ANY lines that meet the criteria are fine.
    #  Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the name of the relevant method
    #    and instance variables.
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle (using its INSTANCE VARIABLES):
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.  (Hint: For this, you'll need to use
         a METHOD that begins with "get".)
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()
    circ = rg.Circle(rg.Point(50, 50), 50)
    rect = rg.Rectangle(rg.Point(100, 100), rg.Point(200, 200))
    circ.fill_color = "blue"
    circ.attach_to(window)
    rect.attach_to(window)

    print("Circle Information")
    print(circ.outline_thickness)
    print(circ.fill_color)
    print(circ.center)
    print(circ.center.x)
    print(circ.center.y)

    print("Rectangle Information")
    print(rect.outline_thickness)
    print(rect.fill_color)
    print(rect.get_center())
    print(rect.get_center().x)
    print(rect.get_center().y)

    window.render()
    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function, per its green doc-string above.
    #    -- ANY objects that meet the criteria are fine.
    #  Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
