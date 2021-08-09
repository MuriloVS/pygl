from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
X, Y, Z, W, H = 0, 0, 0, 200, 200
ROTATION = 0
AXIS = 'z'
SCALE = 2
SPINING = False


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
        return print(f'Rotate({x}, {y}, {z}, {angle}, {axis}) - Undefined axis')
    glMultMatrixf(matrix)
    return translate(-x, -y, -z)


def drawSquare(x, y, width, height=None):
    height = height if height else width
    glBegin(GL_LINE_LOOP)
    glVertex2f(x,           y)
    glVertex2f(x + width,   y)
    glVertex2f(x + width,   y + height)
    glVertex2f(x,           y + height)
    glEnd()


def drawCube(pos_x, pos_y, pos_z, size=1.0, color=[0.0, 0.0, 0.0]):
    glColor3f(color[0], color[1], color[2])
    glPushMatrix()                    # Duplica a matriz atual
    glTranslatef(pos_x, pos_y, pos_z)  # Rotaciona a matriz atual
    glutWireCube(size)
    glPopMatrix()


def makeFrustum(l, r, b, t, n, f):
    glLoadIdentity()
    elem1 = (2*n)/(r-l)
    elem2 = (2*n)/(t-b)
    A = (r+l)/(r-l)
    B = (t+b)/(t-b)
    C = -(f+n)/(f-n)
    D = -(2*f*n)/(f-n)
    matrix = [[elem1, 0,  A,  0],
              [0, elem2,  B,  0],
              [0,     0,  C,  D],
              [0,     0, -1,  0]]
    matrix = np.transpose(matrix)
    return glMultMatrixf(matrix)


def makeOrtho(l, r, b, t, n, f):
    glLoadIdentity()
    elem1 = 2.0/(r-l)
    elem2 = 2.0/(t-b)
    elem3 = -2.0/(f-n)
    tx = -(r+l)/(r-l)
    ty = -(t+b)/(t-b)
    tz = -(f+n)/(f-n)
    matrix = [[elem1, 0, 0, tx],
              [0, elem2, 0, ty],
              [0, 0, elem3, tz],
              [0, 0,     0, 1]]
    matrix = np.transpose(matrix)
    return glMultMatrixf(matrix)


def reshape(width, height):
    glViewport(0, 0, GLsizei(width), GLsizei(height))
    glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    makeFrustum(-1.0, 1.0, -1.0, 1.0, 0.5, 10)
    # glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    # glFrustum(-3.0, 3.0, -3.0, 3.0, 2, 30.0) #Para testes com objetos 3D dá p usar o exercício
    #glFrustum(-1.0, 1.0, -1.0, 1.0, 0.5, 10)
    # glOrtho(-4.0, 4.0, -4.0, 4.0, 2, 30.0) #da aula para praticar - parâmetros já ajustados
    glMatrixMode(GL_MODELVIEW)


def display():
    global ROTATION, X, Y, Z, W, H, SCALE, AXIS
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if SPINING:
        ROTATION += 0.1
        
    x = 1 if AXIS == 'x' else 0
    y = 1 if AXIS == 'y' else 0
    z = 1 if AXIS == 'z' else 0
    # glutSwapBuffers()
    glShadeModel(GL_SMOOTH)

    # MATRIX é uma lista de configurações
    glPushMatrix()                      # Duplica a matriz atual
    glTranslatef(X, Y, Z-6.0)           # Rotaciona a matriz atual
    # glRotatef(ROTATION, x, y, z)
    rotate(x, y, z, ROTATION, AXIS)

    drawCube(-2,    -2,     0,      1,  COLORS["RED"])
    drawCube(-1,    -1,     0,      1,  COLORS["GREEN"])
    drawCube(0,     0,      0,      1,  COLORS["BLUE"])
    drawCube(1,     1,      0,      1,  COLORS["RED"])
    drawCube(2,     2,      0,      1,  COLORS["GREEN"])

    glPopMatrix()

    glFlush()

def keyPressed(key, x, y):
    global X, Y, Z, W, H, SCALE, AXIS, SPINING
    if key[0] == 97:        # A
        X -= 0.1
    elif key[0] == 100:     # D
        X += 0.1
    elif key[0] == 119:     # S
        Y += 0.1
    elif key[0] == 115:     # W
        Y -= 0.1
    elif key[0] == 101:     # E
        Z += 0.1
    elif key[0] == 113:     # Q
        Z -= 0.1
    elif key[0] == 122:     # Z
        SCALE -= 0.1
    elif key[0] == 120:     # X
        SCALE += 0.1
    elif key[0] == 118:     # V
        SPINING = not SPINING
    elif key[0] == 99:      # C
        if AXIS == 'z':
            AXIS = 'x'
        elif AXIS == 'x':
            AXIS = 'y'
        elif AXIS == 'y':
            AXIS = 'z'


def main():
    print('Inicializando...')
    print('\nTeclas:')
    print('[ A / D ]\tMover eixo X')
    print('[ w / s ]\tMover eixo y')
    print('[ E / Q ]\tMover eixo Z')
    print('[ Z / X ]\tAumentar/Diminuir escala')
    print('[ V ]\t\tLigar/Desligar rotação')
    print('[ C ]\t\tAlterar eixo de rotação')

    # glutInit()
    glutInit()
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize (500, 500)
    glutInitWindowPosition (100, 100)
    glutCreateWindow("OpenGL Coding Practice")
    init ()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()



    # glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)
    # glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    # glutInitWindowPosition(0, 0)
    # wind = glutCreateWindow("OpenGL Coding Practice")

    # mat_specular = [ 1.0, 1.0, 1.0, 1.0 ]
    # mat_shininess = [ 50.0 ]
    # light_position = [ 1.0, 1.0, 1.0, 0.0 ]
    # glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    # glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    # glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # glutDisplayFunc(display)
    # glutIdleFunc(display)
    # glutReshapeFunc(reshape)
    # glutKeyboardFunc(keyPressed)

    # glutMainLoop()
    return


main()
