"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Morgan Brown.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

magenta_turtle = rg.SimpleTurtle('circle')
magenta_turtle.pen = rg.Pen('magenta', 2)
magenta_turtle.speed = 10
window.tracer(2)

size = 150

for k in range(20):

    magenta_turtle.draw_circle(size)

    magenta_turtle.pen_up()
    magenta_turtle.right(45)
    magenta_turtle.forward(10)
    magenta_turtle.right(25)

    magenta_turtle.pen_down()
    size = size

another_turtle = rg.SimpleTurtle('square')
another_turtle.pen = rg.Pen('midnight blue', 1)

for k in range(500):
    another_turtle.left(60)
    another_turtle.forward(k)

window.close_on_mouse_click()
