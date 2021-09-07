"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Jordan Asman.
"""
###############################################################################
# DONE: 1.
#   On Line 6 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#  _
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2  rg.SimpleTurtle  objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#  _
#   In this CHALLENGE problem, be creative!
#   Strive for way-cool pictures!  Abstract pictures rule!
#  _
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#  _
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
' import rose graphics '
import rosegraphics as rg
' create window '
window = rg.TurtleWindow()
window.delay(20)
window.tracer(5)
' create turtles '
mickey = rg.SimpleTurtle("turtle")
minnie = rg.SimpleTurtle("turtle")
goofy = rg.SimpleTurtle("turtle")
donald = rg.SimpleTurtle("turtle")
daisy = rg.SimpleTurtle("turtle")
pete = rg.SimpleTurtle("turtle")
pluto = rg.SimpleTurtle("turtle")
' defines pens '
mickey.pen = rg.Pen("red", 5)
minnie.pen = rg.Pen("orange", 2)
goofy.pen = rg.Pen("blue", 10)
donald.pen = rg.Pen("black", 5)
daisy.pen = rg.Pen("magenta", 5)
pete.pen = rg.Pen("yellow", 5)
pluto.pen = rg.Pen("green", 1)
' initial positions '
mickey.pen_up()
mickey.go_to(rg.Point(0, -150))
mickey.pen_down()
minnie.pen_up()
donald.pen_up()
donald.go_to(rg.Point(0, -150))
donald.pen_down()
daisy.pen_up()
daisy.go_to(rg.Point(0, -150))
daisy.pen_down()
pete.pen_up()
pete.go_to(rg.Point(0, -150))
pete.pen_down()
minnie.pen_up()
minnie.go_to(rg.Point(-250, -250))
minnie.pen_down()
goofy.pen_up()
goofy.go_to(rg.Point(-250, -50))
goofy.pen_down()
' loop for moving '
for i in range(4):
    ' moves mickey '
    mickey.draw_regular_polygon(6, 100)
    mickey.pen_up()
    mickey.left(45)
    mickey.backward(10)
    mickey.right(45)
    mickey.pen_down()
for j in range(6):
    ' moves minnie '
    minnie.draw_circle(50)
    minnie.pen_up()
    minnie.right(45)
    minnie.backward(20)
    minnie.left(45)
    minnie.pen_down()
for k in range(3):
    ' moves goofy '
    goofy.draw_regular_polygon(8, 50)
    goofy.pen_up()
    goofy.right(30)
    goofy.backward(50)
    goofy.left(30)
    goofy.pen_down()
for l in range(4):
    ' moves donald '
    donald.draw_regular_polygon(6, 100)
    donald.pen_up()
    donald.left(135)
    donald.forward(10)
    donald.right(135)
    donald.pen_down()
for m in range(4):
    ' moves daisy '
    daisy.draw_regular_polygon(6, 100)
    daisy.pen_up()
    daisy.left(135)
    daisy.backward(10)
    daisy.right(135)
    daisy.pen_down()
for n in range(4):
    ' moves pete '
    pete.draw_regular_polygon(6, 100)
    pete.pen_up()
    pete.left(45)
    pete.forward(10)
    pete.right(45)
    pete.pen_down()
window.tracer(30)
for o in range(30):
    ' head '
    pluto.pen_up()
    pluto.go_to(rg.Point(0 + 2 * o, -300 + 2 * o))
    pluto.pen_down()
    pluto.draw_circle(200)
    pluto.pen_up()
    ' ear '
    pluto.go_to(rg.Point(-150 + 2 * o, 60 + 2 * o))
    pluto.pen_down()
    pluto.draw_circle(100)
    pluto.pen_up()
    ' ear '
    pluto.go_to(rg.Point(150 + 2 * o, 60 + 2 * o))
    pluto.pen_down()
    pluto.draw_circle(100)
    pluto.pen_up()
' close window '
window.close_on_mouse_click()