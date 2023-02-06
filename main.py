
# Made by:
# Kareem ElZeky 120190032
# Adham Khalid 120190133


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from random import randint 
from utils import *
from ball import *
from rectangle import *

# global variables
paddle = rectangle(160, 30, 500, 50)
recs = []
ball = ball(20,500,300)
score = 0
state = 0


def init_rectangles():
    global recs
    recs = []
    for j in range(900, 750,-35):
        for i in range(50,1000, 90):
            recs.append(rectangle(80,30,i,j))

def passiveMotion(x,y):
    paddle.x = (x*(1000/glutGet(GLUT_WINDOW_WIDTH)))

def mouseFunc(k, s,x,y):
    global state
    if k == GLUT_LEFT_BUTTON:
        if state == 0:
            state =1
def keys(k,x,y):
    global state
    if k == b" " and state == 2:
        state = 0
    elif k == b"\x1b" and state ==2:
        glutDestroyWindow()

# Start Scene function
def start():
    global score,ball
    init_rectangles()
    text(400,500, (1,1,0), "Click to Start")
    score = 0
    ball.x = 500
    ball.y = 500
    ball.speedx= 0.9 if randint(0,1) else -0.9 #randint(7,15) if randint(0,1) else -1 * randint(7,15)
    ball.speedy = 0.9

# Game Scene function
def game():
    global ball, paddle, score, recs, state, f
    ball.prevy = ball.y
    ball.prevx = ball.x
    ball.y += ball.speedy
    ball.x += ball.speedx
    if dcrc(ball, paddle):
        ball.speedy *=-1
    wall_collision = bcc(ball) 

    if wall_collision == "right" or wall_collision == "left":
        ball.speedx *= -1
    elif wall_collision == "top":
        ball.speedy *= -1
    elif wall_collision == "bottom":
        state = 2
        init_rectangles()

    for i in recs:
        brick_collision = dcrc(ball, i)
        if brick_collision:
            score += 1
            
        if brick_collision == "right" or brick_collision == "left":
            recs.remove(i)
            if  len(recs)==0:
                init_rectangles()
            ball.speedx *= -1 
        elif brick_collision == "bottom" or brick_collision ==  "top" or brick_collision == "corner":
            recs.remove(i)
            if len(recs)==0:
                init_rectangles()
            ball.speedy *= -1
    glColor(1,0,0)
    ball.draw()
    glColor(1,0.3,0.3)
    paddle.draw()
    for brick in recs:
        brick.draw()

# Score Scene function
def display_score():
    global score
    text(400,500,(1,1,0), f"score: {score}")
    text(250, 450,(1,1,0),"press space bar to continue" )
    text(300, 400, (1,0,0),"press ESC to exit")


def animate_scene( ):
    global ball
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if state == 0:
        start()
    elif state == 1:
        game()
    elif state == 2: 
        display_score()
    glutSwapBuffers()



def initialize_world():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1000, 0, 1000, 0.0, 1.0) # world coordinates from 0 , 1000 x-axis and 0, 1000 y-axis
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(500, 50)
    glutCreateWindow("OpenGL Coding Practice")
    initialize_world()
    glutPassiveMotionFunc(passiveMotion)
    glutMouseFunc(mouseFunc)
    glutKeyboardFunc(keys)
    glutDisplayFunc(animate_scene)
    glutIdleFunc(animate_scene)
    glutMainLoop()


if __name__ == "__main__":
    main()
