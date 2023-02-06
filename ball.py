from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint
from math import pi, cos, sin
class ball:
    def __init__(self,r,x,y):
        self.r =r
        self.x = x
        self.y = y
        self.prevx = x
        self.prevy = y
        self.speedx = 1.2 if randint(0,1) else -1.2
        self.speedy = 1.2 
    
    def draw(self, steps = 100):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glBegin(GL_POLYGON)    
        dtheta = 2*pi / steps 
        theta = 0 
        while theta <= 2*pi : 
            x = int (self.x + self.r * cos(theta))
            y = int (self.y + self.r * sin(theta)) 
            theta += dtheta 
            glVertex2i(x,y)
        glEnd()

