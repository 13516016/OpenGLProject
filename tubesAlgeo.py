import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0
width = 800
height = 600

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_line():
    glBegin(GL_LINES)
    glVertex2f(0, height/2)                                   # bottom left point
    glVertex2f(width, height/2)                           # bottom right point
    glVertex2f(width/2, height)                  # top right point
    glVertex2f(width/2, 0)                          # top left point
    glEnd()

def draw_shape():
    shape = raw_input()
    if (shape=='rectangle'):                                # start drawing a rectangle
        glBegin(GL_QUADS)
        glVertex2f(0, 0)                                   # bottom left point
        glVertex2f(0 + 200, 0)                           # bottom right point
        glVertex2f(0 + 200, 0 + 200)                  # top right point
        glVertex2f(0, 0 + 200)
        glColor3f(0.0, 0.0, 1.0)                           # set color to                          # top left point
        glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width,height)
    draw_line()
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
