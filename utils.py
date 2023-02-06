# ball and rectangle collision function
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from rectangle import *
from ball import *

def dcrc(b: ball, r: rectangle):
    dx = abs(b.x - r.x)
    dy = abs(b.y- r.y)
    if (dx > (r.w/2 + b.r)) or (dy > (r.h/2 + b.r)):
        return False 
    # rectangle is not touched at the corners
    elif ((dx-r.w/2)**2 + (dy - r.h/2) **2 > b.r**2) and (b.x > r.x + r.w/2 or b.x < r.x - r.w/2) and (b.y > r.y + r.h/2 or b.y < r.y - r.h/2):
        return False

    elif b.y > r.y and dy <= b.r + r.h/2 and b.prevy - r.y > (r.h/2 + b.r):
        return "top"
    elif b.y < r.y and dy <= b.r + r.h/2 and r.y - b.prevy > (r.h/2 + b.r): 
        return "bottom" 

    elif b.x > r.x and dx <= b.r + r.w/2 and b.prevx - r.x > (r.w/2 + b.r):
        return "right"
    elif b.x < r.x and dx <= b.r + r.w/2 and r.x - b.prevx > (r.w/2 + b.r):
        return 'left'
    return "corner"

#ball wall collision function
def bcc(ball): 
    if ball.x + ball.r > 1000: 
        ball.x =  1000 - ball.r
        return "right"
    elif ball.x - ball.r < 0:
        ball.x = ball.r
        return "left"
    elif ball.y -ball.r < 0:
        ball.y = ball.r
        return "bottom"
    elif ball.y + ball.r > 1000:
        ball.y = 1000 - ball.r
        return "bottom"


# text function
def text(x, y,color, text):
    glColor(*color)
    glRasterPos2d(x, y)
    glutBitmapString(GLUT_BITMAP_HELVETICA_18, str(text).encode("ascii"))
    glColor(1,0,0)
