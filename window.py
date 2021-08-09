from OpenGL.GL import *
from OpenGL.GL.images import ImageInputConverter
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from PIL import Image
import numpy as np

COLORS = {
    'WHITE': [1.0, 1.0, 1.0],
    'BLACK': [0.0, 0.0, 0.0],
    'GREEN': [0.0, 1.0, 0.0],
    'BLUE':  [0.0, 0.0, 1.0],
    'SKY':   [0.53, 0.81, 0.92]
}

def translate(x, y, z):
    matrix = [
        [1,     0,      0,      0],
        [0,     1,      0,      0],
        [0,     0,      1,      0],
        [x,     y,      z,      1],
    ]
    return glMultMatrixf(matrix)

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

def drawFloor():
    glPushMatrix()
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(-60.0,   -0.5, -60.0)
    glVertex3f(60.0,    -0.5, -60.0)
    glVertex3f(60.0,    -0.5, 60.0)
    glVertex3f(-60.0,   -0.5, 60.0)
    glEnd()
    glPopMatrix()       

class Cube:
    def __init__(self, position_x, position_y, position_z, size, color=[0.0, 0.0, 0.0]):
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.size       = size
        self.color      = color

    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
        
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glutSolidCube(self.size)

        if own_matrix:
            glPopMatrix()
    
    def move(self, x, y, z):
        self.position_x += x
        self.position_y += y
        self.position_z += z


class Window:
    def __init__(self, title, width, height, initialize=True):
        # Configurações da janela
        self.background_color = COLORS['SKY']
        self.title  = title
        self.width  = width
        self.height = height
        # Configurações do OpenGL
        self.key_buffer = []
        self.mouse_pos = {
            "x": 0,
            "y": 0
        }
        self.ligh_position  = [0.0, 1.0, 0.0, 13.0]
        self.materials      = {
            "DIFUSE":   [0.5, 0.5, 0.5, 1.0],
            "SPECULAR": [0.5, 0.5, 0.5, 1.0]
        }
        # Configurações próprias
        self.objects = []
        self.position = {
            "x": 0,
            "y": 0,
            "z": 0
        }
        self.jump_buffer = 0
        self.rotation = 0
        # Inicalização OpenGL
        if initialize:
            self.initialize()


    def initialize(self):
        # Inicializando Glut
        glutInit()
        # Definindo modo de exibição
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(self.title)
    
    def configureOpenGl(self):
        # Definindo cor de fundo
        glClearColor (self.background_color[0], self.background_color[1], self.background_color[2], 0.0)
        # Configurando shader
        glShadeModel (GL_SMOOTH)
        # Habilitando profundidade
        glEnable(GL_DEPTH_TEST)
        # Definindo materiais
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.materials['DIFUSE'])
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.materials['SPECULAR'])
        glMaterialf(GL_FRONT, GL_SHININESS, 20.0)
        # Definindo e habilitando luzes
        glLightfv(GL_LIGHT0, GL_POSITION, self.ligh_position)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        # Definindo e habilitando modo de coloração
        glColorMaterial(GL_FRONT, GL_DIFFUSE);
        glEnable(GL_COLOR_MATERIAL);

    def configureGlutEvents(self):       
        glutDisplayFunc(self.glutDisplay)
        glutIdleFunc(self.glutDisplay)
        glutReshapeFunc(self.glutReshape)
        glutKeyboardFunc(self.glutKeyDown)
        glutKeyboardUpFunc(self.glutKeyUp)
        glutMotionFunc(self.glutMouseMove)
        glutMainLoop()
    
    def glutDisplay(self):
        self.glutMovement()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        glPushMatrix()

        glTranslatef(self.position['x'], self.position['y'], self.position['z']) 

        glPushMatrix()
        glTranslatef(-self.position['x']*2, -self.position['y']*2, -self.position['z']*2) 
        rotate(self.position['x'], self.position['y'], self.position['z'], self.rotation, 'y')

        drawFloor()

        for obj in self.objects:
            in_x = self.position['x'] < obj.position_x + obj.size*1.5 and self.position['x'] > obj.position_x - obj.size*1.5
            in_z = self.position['z'] < obj.position_z + obj.size*1.5 and self.position['z'] > obj.position_z - obj.size*1.5
            in_y = self.position['y'] < obj.position_y + obj.size*1.5 and self.position['y'] > obj.position_y - obj.size*1.5
            if(in_x and in_z and in_y):
                move_x = math.copysign(0.2,  obj.position_x - self.position['x']) if abs(obj.position_x - self.position['x']) > obj.size/2 else 0
                move_z = math.copysign(0.2,  obj.position_z - self.position['z']) if abs(obj.position_z - self.position['z']) > obj.size/2 else 0
                obj.move(move_x, 0, move_z)
                print(move_x)
            else:
                obj.draw(True)

        glPopMatrix()
        glPopMatrix()
        glutSwapBuffers()

    def glutReshape(self, width, height):
        glViewport(0, 0, GLsizei(width), GLsizei(height))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum (-0.5, 0.5, -0.5, 0.5, 0.5, 20)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def glutMouseMove(self, x, y):
        x_diff = self.mouse_pos['x'] - x
        print(x_diff)
        self.mouse_pos['x'] = x
        self.mouse_pos['x'] = y

    def glutKeyDown(self, key, x, y):
        self.key_buffer.append(key)

    def glutKeyUp(self, key, x, y):
        self.key_buffer.remove(key)

    def glutMovement(self):


        if(self.jump_buffer > 0):
            if(self.jump_buffer >= 750):
                self.position['y'] += 0.015 * self.jump_buffer/1000
            else:
                if(self.position['y'] > 0):
                    self.position['y'] -= 0.0035 * 1000/self.jump_buffer
            if(self.position['y'] > 0):
                self.jump_buffer -= 1
            else:
                self.jump_buffer = 0

        self.jump_buffer = 1000 if (b' ' in self.key_buffer and self.jump_buffer == 0) else self.jump_buffer


        self.rotation = self.rotation - 360 if self.rotation > 360 else self.rotation

        horizontal_movement = 0.002 if (b'a' in self.key_buffer) else -0.002 if (b'd' in self.key_buffer) else 0
        vertical_movement   = 0.002 if (b'w' in self.key_buffer) else -0.002 if (b's' in self.key_buffer) else 0
        self.position['x'] -= horizontal_movement * math.cos(math.radians(self.rotation)) + vertical_movement * math.sin(math.radians(self.rotation))
        self.position['z'] -= vertical_movement * math.cos(math.radians(self.rotation)) + horizontal_movement * math.sin(math.radians(self.rotation))

        #self.position['y']  -= (0.002)    if (b'z' in self.key_buffer) else (-0.002)    if (b'x' in self.key_buffer) else 0 
        self.rotation       += (0.1)     if (b'q' in self.key_buffer) else (-0.1)     if (b'e' in self.key_buffer) else 0 

    def addObject(self, obj):
        self.objects.append(obj)

window = Window('OpenGL Practice', 500, 500)

cube_01 = Cube(2.0, 0.0, -6.0, 1.0, COLORS['BLUE'])
window.objects.append(cube_01)

cube_02 = Cube(-2.0, 0.0, -6.0, 1.0, COLORS['BLUE'])
window.objects.append(cube_02)

cube_03 = Cube(2.0, 0.0, -4.0, 0.5, COLORS['BLUE'])
window.objects.append(cube_03)

cube_04 = Cube(-2.0, 0.0, -4.0, 0.5, COLORS['BLUE'])
window.objects.append(cube_04)

cube_05 = Cube(2.0, 0.0, -2.0, 0.75, COLORS['BLUE'])
window.objects.append(cube_05)

cube_06 = Cube(-2.0, 0.0, -2.0, 0.75, COLORS['BLUE'])
window.objects.append(cube_06)

window.configureOpenGl()
window.configureGlutEvents()

