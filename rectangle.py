from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class rectangle:
    def __init__(self, w,h,x,y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(self.x, self.y, 0)
        glBegin(GL_POLYGON)
        glVertex(self.w/2, self.h/2)
        glVertex(self.w/2 , - self.h/2)
        glVertex(- self.w/2 , -self.h/2)
        glVertex(-self.w/2 , self.h/2)
        glEnd()