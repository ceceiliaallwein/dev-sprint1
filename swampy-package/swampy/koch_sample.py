
from TurtleWorld import *  
import math 
world = TurtleWorld()
bob = Turtle()
bob.delay = .01


def draw(t, length, n):
    """
    Draws a tree with the given trunk length and levels of recursion.

    Turtle ends up back where he started.

    Arguments:
        t: Turtle
        length: trunk length
        n: int levels of recursion
    """
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


#lt(bob)
#bk(bob, 70)
#draw(bob, 10, 7)

#wait_for_user()


# NOTES ON L-SYSTEMS 

# Koch curves 
# variables: F
# constants: + - 
# start: F
# Wikipedia rules: (F -> F-F+F+F-F) 
# RampUp rules: (F -> F-F++F-F)

# F = draw forward
# + = right turn 60 degrees
# - = left turn 60 degrees 


def koch(t, x):
    """Draws a Koch curve with a given length x.

    Turtle does not end up back where he started. 

    Arguments:
        t: Turtle
        x: side length
    """
#    n = 7
    if x < 3: 
        fd(t, x)
#   elif n == 0: 
#       return
    else:  
        angle = 60
        koch(t, x/3) 
        lt(t, angle)
        koch(t, x/3)
        rt(t, angle*2) 
        koch(t, x/3)
        lt(t, angle)
        koch(t, x/3)


def snowflake (t, x):
    '''
    Draws a snowflake with given side length x.

    Angles sum to 360 to ensure that ends meet.

    Iteration is set at 3, because each iteration 
    forms a side of the triangle, i.e. snowflake.

    The snowflake can have n number of sides, 
  
    ''' 
    for i in range (3): 
        koch(t, x)
        rt(t, 120)

def doily (t, x, n):
    '''
    Draws a snowflake with given side length x.

    Angles sum to 360.

    Iteration has been generalized to relate 
    the angle to the number of iterations.  
    ''' 
    angle = 360/n
    if n <= 2: 
        return
    else:
        for i in range (n): 
            koch(t, x)
            rt(t, angle)


#koch(bob, 200)

#snowflake(bob, 200)

doily(bob, 200, 5)

wait_for_user()


###################################

# QUESTIONS
# The Koch curve doesn't appear (visually) to need an axiom (F) to set 
# the starting position like the tree algorithm; however, the L-system 
# does define a starting axiom. What's this relationship? My first
# instinct was to think about F as the first level of recursion, but it's
# not. It's just a line segment. Thoughts? 