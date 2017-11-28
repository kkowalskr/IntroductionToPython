"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  Kenny Kowalski  with your own name.
########################################################################

########################################################################
# DON: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
##########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

mr_red = rg.SimpleTurtle('turtle')
mr_red.pen = rg.Pen('red','3')
mr_red.speed = 150

mr_blue = rg.SimpleTurtle('turtle')
mr_blue.pen = rg.Pen('blue','10')
mr_blue.speed = 150

mr_red.pen_up()
mr_red.right(135)
mr_red.forward(200)
mr_red.left(135)
mr_red.pen_down()

size = 300

for k in range(24):

    mr_blue.draw_circle(100)
    mr_blue.pen_up()
    mr_blue.right(15)
    mr_blue.pen_down()

    mr_red.draw_square(size)
    mr_red.pen_up()
    mr_red.right(135)
    mr_red.forward(20)
    mr_red.left(135)
    mr_red.pen_down()

    size = size + 30


window.close_on_mouse_click()


