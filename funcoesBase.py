from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

x_inicial, y_inicial, z_inicial, tamanho = 100, 200, 20, 100
X, Y, Z, W, H = 0, 0, 0, 200, 200

ROTATION = 0
AXIS = 'z'
SCALE = 2
SPINING = False

# Projeção


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


# TRANSFORMAÇÃO


def makeTranslate(x, y, z):
    matrix = [[1, 0, 0, x],
              [0, 1, 0, y],
              [0, 0, 1, z],
              [0, 0, 0, 1]]
    # faz a transposta para realizar a multiplicação
    matrix = np.transpose(matrix)
    return glMultMatrixf(matrix)


def makeScale(x, y, z, s):
    makeTranslate(x, y, z)  # empilha objeto na posição inicial
    matrix = [[s, 0, 0, 0],
              [0, s, 0, 0],
              [0, 0, s, 0],
              [0, 0, 0, 1]]
    glMultMatrixf(matrix)  # escala objeto
    return makeTranslate(-x, -y, -z)  # empilha objeto trazido para origem


def makeRotate(x, y, z, angle, axis):
    makeTranslate(x, y, z)  # empilha objeto na posição inicial
    radians = math.radians(angle)
    c = math.cos(radians)
    s = math.sin(radians)
    if axis == 'x':  # escolhe eixo de referência para rotação
        matrix = [[1, 0, 0, 0],
                  [0, c, -s, 0],
                  [0, s, c, 0],
                  [0, 0, 0, 1]]
    elif axis == 'y':
        matrix = [[c, 0, s, 0],
                  [0, 1, 0, 0],
                  [-s, 0, c, 0],
                  [0, 0, 0, 1]]
    else:  # axis == 'z'
        matrix = [[c, s, 0, 0],
                  [-s, c, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]
    glMultMatrixf(matrix)  # rotacionando objeto
    return makeTranslate(-x, -y, -z)  # empilha objeto trazido para origem


# OBJETOS


def drawCube(pos_x, pos_y, pos_z, size=1.0, color=[0.0, 0.0, 0.0]):
    glColor3f(color[0], color[1], color[2])
    glPushMatrix()                    # Duplica a matriz atual
    glTranslatef(pos_x, pos_y, pos_z)  # Rotaciona a matriz atual
    glutWireCube(size)
    glPopMatrix()


def drawSquare(x, y, width, height=None):
    height = height if height else width
    glBegin(GL_LINE_LOOP)
    glVertex2f(x,           y)
    glVertex2f(x + width,   y)
    glVertex2f(x + width,   y + height)
    glVertex2f(x,           y + height)
    glEnd()


# JANELA, VISUALIZAÇÃO E DESENHO


def reshape(width, height):  # Projeção
    glViewport(0, 0, GLsizei(width), GLsizei(height))
    glMatrixMode(GL_PROJECTION)
    # glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    # makeOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    #glFrustum(-3.0, 3.0, -3.0, 3.0, 2, 30.0)
    #makeFrustum(-1.0, 1.0, -1.0, 1.0, 0.5, 10)
    makeOrtho(-10.0, 10.0, -10.0, 10.0, 0.0, 30)

    glMatrixMode(GL_MODELVIEW)


def display():
    global ROTATION, X, Y, Z, W, H, SCALE, AXIS
    glClearColor(0, 0, 0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glLoadIdentity()

    if SPINING:
        ROTATION += 0.1

    # scale(X, Y, 0, SCALE)
    # rotate(X, Y, 0, ROTATION, 'z')
    # drawSquare(X, Y, W, H)
    x = 1 if AXIS == 'x' else 0
    y = 1 if AXIS == 'y' else 0
    z = 1 if AXIS == 'z' else 0

    glShadeModel(GL_SMOOTH)

    # teste 2D (projeção, translação, rotação, escala)
    # drawSquare(x_inicial, y_inicial, tamanho)
    # makeScale(x_inicial, y_inicial, 0, 2)
    # makeRotate(x_inicial, y_inicial, 0, -45, 'z')
    # drawSquare(x_inicial, y_inicial, tamanho)

    # teste 3D (projeção)
    glPushMatrix()
    glTranslatef(X, Y, Z-6.0)
    makeRotate(x, y, z, ROTATION, AXIS)
    drawCube(-1, -1, 0, 2, [.5, 0, 0])
    drawCube(-1, 0, 0, 1.5, [1, 0, 0])
    drawCube(0, -1, 0, 1, [1, .5, 0])
    drawCube(0, 0, 0, .5, [1, 1, 0])
    drawCube(0, 1, 0, 1, [1, 1, .5])
    drawCube(1, 1, 0, 1.5, [1, 1, 1])
    drawCube(1, 0, 0, 2, [1, 1, .5])
    drawCube(1, -1, 0, 1.5, [1, .5, 0])
    drawCube(-1, 1, 0, 1, [.5, 0, 0])
    glPopMatrix()

    glutSwapBuffers()


# INICIALIZAÇÃO E MOVIMENTAÇÃO


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


def manualKeyboard():
    print('Inicializando...')
    print('\nTeclas:')
    print('[ A / D ]\tMover eixo X')
    print('[ w / s ]\tMover eixo y')
    print('[ E / Q ]\tMover eixo Z')
    print('[ Z / X ]\tAumentar/Diminuir escala')
    print('[ V ]\t\tLigar/Desligar rotação')
    print('[ C ]\t\tAlterar eixo de rotação')


def main():

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding Practice")

    manualKeyboard()

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyPressed)

    glutMainLoop()  # Eventos
    return


main()
