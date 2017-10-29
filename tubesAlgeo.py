import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0
width = 800
height = 600

def refresh2d(width, height):
    glViewport(width/2, height/2, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,width,0,height);
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_line():
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINES)
    glVertex2d(1,height/2)                                   # bottom left point
    glVertex2d(1, -1*(height/2))                           # bottom right point

    glVertex2d(width/2, 0)                  # top right point
    glVertex2d(0, 0)                          # top left point

    glEnd()


def draw_shape(shape):
    glColor3f(0.0, 0.0, 1.0)                           # set color to                          # top left point
    glLoadIdentity()
    if (shape=='rectangle'):                                # start drawing a rectangle
        glBegin(GL_QUADS)
        glVertex2f(10, 10)                                   # bottom left point
        glVertex2f(10+ 200, 10)                           # bottom right point
        glVertex2f(10 + 200, 10 + 200)                  # top right point
        glVertex2f(10, 10 + 200)
        glEnd()
    glFlush()

def draw():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    refresh2d(width,height)
    draw_line()

    glLoadIdentity()
    shape = raw_input()
    draw_shape(shape)
    glutSwapBuffers()


def main():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("noobtuts.com")              # create window with title
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()

main()
