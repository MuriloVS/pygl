from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

WINDOW_HEIGHT   = 500
WINDOW_WIDTH    = 500
X, Y, W, H      = 0, 0, 200, 200
ROTATION        = 0
AXIS            = 'z'
SCALE           = 2

def translate(x, y, z):
    matrix = [
        [1,     0,      0,      0],
        [0,     1,      0,      0],
        [0,     0,      1,      0],
        [x,     y,      z,      1],
    ]
    return glMultMatrixf(matrix)

def scale(x, y, z, s):
    translate(x, y, z)
    matrix = [
        [s,     0,      0,      0],
        [0,     s,      0,      0],
        [0,     0,      s,      0],
        [0,     0,      0,      1],
    ]
    glMultMatrixf(matrix)
    return translate(-x, -y, -z)

def rotate(x, y, z, angle, axis):
    translate(x, y, z)
    radians = math.radians(angle)
    cos = math.cos(radians)
    sin = math.sin(radians)
    if axis == 'x':
        matrix = [
            [1,     0,      0,      0],
            [0,     cos,    -sin,   0],
            [0,     sin,    cos,    0],
            [0,     0,      0,      1],
        ]
    elif axis == 'y':
        matrix = [
            [cos,   0,      sin,    0],
            [0,     1,      0,      0],
            [-sin,  0,      cos,    0],
            [0,     0,      0,      1],
        ]
    elif axis == 'z':
        matrix = [
            [cos,   sin,    0,      0],
            [-sin,  cos,    0,      0],
            [0,     0,      1,      0],
            [0,     0,      0,      1],
        ]
    else:
        return print(f'Rotate({x}, {y}, {z}, {angle}, {axis}) - Undefined axis');
    glMultMatrixf(matrix)
    return translate(-x, -y, -z)

def drawSquare(x, y, width, height = None):
    height = height if height else width
    glBegin(GL_LINE_LOOP)
    glVertex2f(x,           y)
    glVertex2f(x + width,   y)
    glVertex2f(x + width,   y + height)
    glVertex2f(x,           y + height)
    glEnd()

def reshape(width, height):
    glViewport(0, 0, GLsizei(width), GLsizei(height))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    #glFrustum(-3.0, 3.0, -3.0, 3.0, 2, 30.0) #Para testes com objetos 3D dá p usar o exercício
    glFrustum (-1.0, 1.0, -1.0, 1.0, 0.5, 10)
    #glOrtho(-4.0, 4.0, -4.0, 4.0, 2, 30.0) #da aula para praticar - parâmetros já ajustados
    glMatrixMode (GL_MODELVIEW)

def display():
    global ROTATION, X, Y, W, H, SCALE, AXIS
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glLoadIdentity()

    ROTATION += 0.1

    # scale(X, Y, 0, SCALE)
    # rotate(X, Y, 0, ROTATION, 'z')
    # drawSquare(X, Y, W, H)
    x = 1 if AXIS == 'x' else 0
    y = 1 if AXIS == 'y' else 0
    z = 1 if AXIS == 'z' else 0
    # glutSwapBuffers()

    # MATRIX é uma lista de configurações

    glPushMatrix()                    # Duplica a matriz atual
    glTranslatef(0.0, 0.0, -6.0)      # Rotaciona a matriz atual
    glRotatef(ROTATION, 1, 1, 1)

    # Cubo do centro
    glPushMatrix()                    # Duplica a matriz atual
    glTranslatef(0.0+X, 0.0+Y, -3.0)  # Rotaciona a matriz atual
    glutSolidSphere(1.0, 100, 100)    # A partir da matriz atual, desenha um cubo
    glPopMatrix()                     # Remova a matriz atual

    # Direita
    glPushMatrix()
    glTranslatef(2.0+X, 0.0+Y, -3.0)
    glutWireCube(1.0)
    glPopMatrix()

    # Esquerda
    glPushMatrix()
    glTranslatef(-2.0+X, 0.0+Y, -3.0)
    glutWireCube(1.0)
    glPopMatrix()


    glPopMatrix()

    glFlush ()

def keyPressed(key, x, y):
    global ROTATION, X, Y, W, H, SCALE, AXIS
    print(f'{key} - {key[0]}')
    if key[0] == 97:        # A
        X -= 0.1
    elif key[0] == 100:     # D
        X += 0.1
    elif key[0] == 119:     # S
        Y += 0.1
    elif key[0] == 115:     # W
        Y -= 0.1
    elif key[0] == 101:     # E
        ROTATION += 10
    elif key[0] == 113:     # Q 
        ROTATION -= 10
    elif key[0] == 122:     # Z
        SCALE -= 0.1
    elif key[0] == 120:     # X
        SCALE += 0.1
    elif key[0] == 99:      # C
        if AXIS == 'z':
            AXIS = 'x'
        elif AXIS == 'x':
            AXIS = 'y'
        elif AXIS == 'y':
            AXIS = 'z'

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding Practice")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyPressed)

    glutMainLoop()
    return

main()