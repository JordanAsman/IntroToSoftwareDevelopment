"""
An exercise that summarizes what you have learned in this Session.

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
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:
#  _
#    - Constructs a SimpleTurtle with a  "blue"  Pen.
#    - Makes the SimpleTurtle go straight UP 200 pixels.
#    - Makes the SimpleTurtle lift its pen UP
#         (so that the next movements do NOT leave a "trail")
#         HINT: Use the "dot trick" to figure out how to do this.
#    - Makes the SimpleTurtle go to the Point at (100, -40).
#    - Makes the SimpleTurtle put its pen DOWN
#         (so that the next movements will return to leaving a "trail").
#    - Makes the SimpleTurtle's pen have color "green" and thickness 10.
#    - Makes the SimpleTurtle go 150 pixels straight DOWN.
#  _
#   Don't forget to:
#     - import rosegraphics and
#     - construct a TurtleWindow
#            [remember the required PARENTHESES for constructing an object!]
#         at the BEGINNING of your code, and to
#     - ask your  TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.  (Again, parentheses needed!)
#   See the beginning and end of  m5e_loopy_turtles  for an example.
#  _
#   As always, test by running the module.
#   As always, COMMIT-and-PUSH when you are done with this module.
###############################################################################
' import rosegraphics '
import rosegraphics as rg
' create window '
window = rg.TurtleWindow()
window.delay(50)
' create turtle and move '
bill = rg.SimpleTurtle("turtle")
bill.pen = rg.Pen("blue", 2)
bill.left(90)
bill.forward(200)
bill.pen_up()
bill.go_to(rg.Point(100, -40))
bill.pen_down()
bill.pen = rg.Pen("green", 10)
bill.left(180)
bill.forward(150)
window.close_on_mouse_click()