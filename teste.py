from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w, h = 500, 500
x_inicial, y_inicial, tamanho = 100, 100, 100

def nosso_translate(x, y, option):
    if option == 'to_origin':
        matrix = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0], 
                  [-x,-y,0, 1]]
        return matrix
    
    if option == 'to_position':
        matrix = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0], 
                  [x, y, 0, 1]]
        return matrix

def nosso_rotate(angle):
    radians = math.radians(angle)
    c = math.cos(radians)
    s = math.sin(radians)
    matrix = [[c, s, 0, 0],
              [-s, c, 0, 0],
              [0, 0, 1, 0], 
              [0, 0, 0, 1]]
    return matrix    

def empty_square(x, y, size):    
    glBegin(GL_LINE_LOOP) 
    glVertex2f(x, y)
    glVertex2f(x+size, y)
    glVertex2f(x+size, y+size)
    glVertex2f(x, y+size) 
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glLoadIdentity()
    iterate()    
    glColor3f(0.0, 0.0, 0.0)

    empty_square(x_inicial, y_inicial, tamanho)     

    matrix = nosso_translate(x_inicial, y_inicial, 'to_position') 
    glMultMatrixf(matrix)

    matrix = nosso_rotate(15) 
    glMultMatrixf(matrix)

    matrix = nosso_translate(x_inicial, y_inicial, 'to_origin') 
    glMultMatrixf(matrix)     

    empty_square(x_inicial, y_inicial, tamanho)
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()