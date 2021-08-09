from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

COLORS = {
    'WHITE': [1.0, 1.0, 1.0],
    'BLACK': [0.0, 0.0, 0.0],
    'GREEN': [0.0, 1.0, 0.0]
}

def drawCube(pos_x, pos_y, pos_z, size=1.0, color=[0.0, 0.0, 0.0]):
    glColor3f(color[0], color[1], color[2])
    glPushMatrix()                    # Duplica a matriz atual
    glTranslatef(pos_x, pos_y, pos_z)  # Rotaciona a matriz atual
    glutSolidCube(size)
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
        self.background_color = COLORS['WHITE']
        self.title  = title
        self.width  = width
        self.height = height
        # Configurações do OpenGL
        self.ligh_position  = [1.0, 1.0, 1.0, 0.0]
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
        self.rotation = 0
        # Inicalização OpenGL
        if initialize:
            self.initialize()

    def initialize(self):
        # Inicializando Glut
        glutInit()
        # Definindo modo de exibição
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
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
        glMaterialf(GL_FRONT, GL_SHININESS, 25.0)
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
        glutMainLoop()
    
    def glutDisplay(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
        glPushMatrix()
        glTranslatef(self.position['x'], self.position['y'], self.position['z'])
        glRotatef(self.rotation, 0, 1, 0)
        for obj in self.objects:
            obj.draw(True)
        glTranslatef(-self.position['x'], -self.position['y'], -self.position['z'])
        glPopMatrix()
        glFlush()

    def glutReshape(self, width, height):
        glViewport(0, 0, GLsizei(width), GLsizei(height))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum (-0.5, 0.5, -0.5, 0.5, 0.5, 20)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def glutKeyDown(self, key, x, y):
        self.position['x']  += (0.1) if (key == b'a') else (-0.1) if (key == b'd') else 0 
        self.position['z']  += (0.1) if (key == b'w') else (-0.1) if (key == b's') else 0 
        self.rotation       += (1) if (key == b'e') else (-1) if (key == b'q') else 0 
        glutPostRedisplay()

    def addObject(self, obj):
        self.objects.append(obj)

window = Window('OpenGL Practice', 500, 500)

cube_01 = Cube(2.0, 0.0, -6.0, 1.0, COLORS['GREEN'])
window.objects.append(cube_01)

cube_02 = Cube(-2.0, 0.0, -6.0, 1.0, COLORS['GREEN'])
window.objects.append(cube_02)

cube_03 = Cube(2.0, 0.0, -4.0, 0.5, COLORS['GREEN'])
window.objects.append(cube_03)

cube_04 = Cube(-2.0, 0.0, -4.0, 0.5, COLORS['GREEN'])
window.objects.append(cube_04)

cube_05 = Cube(2.0, 0.0, -2.0, 0.75, COLORS['GREEN'])
window.objects.append(cube_05)

cube_06 = Cube(-2.0, 0.0, -2.0, 0.75, COLORS['GREEN'])
window.objects.append(cube_06)

window.configureOpenGl()
window.configureGlutEvents()

