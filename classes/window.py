import numpy
from classes.basic import *
from PIL import Image
import math
import sys
from classes.colors import *

testing = (sys.argv[1] == 'dev') if (len(sys.argv) > 1) else False

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
        self.ligh_position  = [1.5, 2.0, -1.5, 13.0]
        self.materials      = {
            "AMBIENT":  [0.2, 0.2, 0.2, 1.0],
            "DIFUSE":   [0.1, 0.1, 0.1, 1.0],
            "SPECULAR": [0.1, 0.1, 0.1, 1.0]
        }
        # Configuração de Projeção
        self.projection = "frustum"
        # Configurações de texturas
        self.textures = []
        # Configurações próprias
        self.objects = []
        self.position = {
            "x": 0,
            "y": 0,
            "z": 0
        }

        self.rotation = 0
        self.bobbing = 'up'
        # Inicalização OpenGL
        if initialize:
            self.initialize()

    def loadTextures(self):
        grass_image = Image.open('grass.jpeg').convert('RGBA')
        self.textures.append({
            "height":   grass_image.height,
            "width":    grass_image.width,
            "data":     numpy.array(list(grass_image.getdata()), numpy.uint8)
        });

    def initialize(self):
        # Inicializando Glut
        glutInit()
        # Definindo modo de exibição
        glRenderMode(GL_RENDER)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(self.title)
    
    def configureOpenGl(self):
        # Definindo cor de fundo
        glClearColor(self.background_color[0], self.background_color[1], self.background_color[2], 0.0)
        # Configurando shader
        glShadeModel(GL_SMOOTH)
        # Habilitando profundidade
        glEnable(GL_DEPTH_TEST)
        # Definindo materiais
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.materials['AMBIENT'])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.materials['DIFUSE'])
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.materials['SPECULAR'])
        glMaterialf(GL_FRONT, GL_SHININESS, 3.0)
        # Definindo e habilitando luzes
        glLightfv(GL_LIGHT0, GL_AMBIENT,  [0.0, 0.0, 0.0, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  [1.0, 1.0, 0.9, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        glLightfv(GL_LIGHT0, GL_POSITION, self.ligh_position)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
        # Definindo e habilitando modo de coloração
        glColorMaterial(GL_FRONT, GL_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        # Permitindo a mistura de cores e opacidade
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        # # Configurações e habilitação de texturas
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)

        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);

        texgen_s = [0.0, 0.0, 1.0, 0.0]
        texgen_t = [1.0, 0.0, 0.0, 1.0]

        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
        glTexGenfv(GL_S, GL_OBJECT_PLANE, texgen_s, 0);
        glTexGenfv(GL_T, GL_OBJECT_PLANE, texgen_t, 0);
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)


    def configureGlutEvents(self):       
        glutDisplayFunc(self.glutDisplay)
        if not testing:
            glutIdleFunc(self.glutDisplay)
        glutReshapeFunc(self.glutReshape)
        glutKeyboardFunc(self.glutKeyDown)
        glutKeyboardUpFunc(self.glutKeyUp)
        glutMotionFunc(self.glutMouseMove)
        glutMainLoop()
    
    
    def glutDisplay(self):
        self.glutChangeProjection()
        self.glutMovement()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        glPushMatrix()

        glTranslatef(self.position['x'], self.position['y'], self.position['z']) 

        glPushMatrix()
        glTranslatef(-self.position['x']*2, -self.position['y']*2, -self.position['z']*2) 
        rotate(self.position['x'], self.position['y'], self.position['z'], self.rotation, 'y')

        glDisable(GL_TEXTURE_2D)

        for obj in self.objects:
            if obj.type != 'group':
                obj.load_texture()
            obj.animate()
            obj.draw(True)

        glPopMatrix()
        glPopMatrix()

        glutSwapBuffers()

    def glutReshape(self, width, height):
        glViewport(0, 0, GLsizei(width), GLsizei(height))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        if self.projection == "frustum":
            left    = -0.5
            right   = 0.5
            top     = -0.5
            bottom  = 0.25
            near    = 0.5
            far     = 10
            glFrustum (left, right, top, bottom, near, far)

        else: #self.projection == "ortho":
            left    = -0.5*4
            right   = 0.5*4
            top     = -0.5*3
            bottom  = 0.25*3
            near    = 0.5
            far     = 8
            glOrtho (left, right, top, bottom, near, far)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def glutChangeProjection(self):
        if b'o' in self.key_buffer:
            self.projection = 'ortho'
        if b'p' in self.key_buffer:
            self.projection = 'frustum'
        self.glutReshape(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))

    def glutMouseMove(self, x, y):
        x_diff = self.mouse_pos['x'] - x
        self.mouse_pos['x'] = x
        self.mouse_pos['x'] = y

    def glutKeyDown(self, key, x, y):
        self.key_buffer.append(key)

    def glutKeyUp(self, key, x, y):
        if key in self.key_buffer:
            self.key_buffer.remove(key)

    def glutMovement(self):

        speed = 2.0 if b' ' in self.key_buffer else 1.0

        self.rotation = self.rotation - 360 if self.rotation > 360 else self.rotation

        horizontal_movement = 0.006 if (b'd' in self.key_buffer) else -0.006 if (b'a' in self.key_buffer) else 0
        vertical_movement   = 0.006 if (b'w' in self.key_buffer) else -0.006 if (b's' in self.key_buffer) else 0

        x_movement = vertical_movement * math.sin(math.radians(self.rotation)) + horizontal_movement * math.sin(math.radians(self.rotation - 90))
        z_movement = vertical_movement * math.cos(math.radians(self.rotation)) + horizontal_movement * math.cos(math.radians(self.rotation - 90))

        can_walk_x = True
        can_walk_z = True

        if self.bobbing == 'up':
            if self.position['y'] < 0.008:
                self.position['y'] += 0.0007 * speed
            else:
                self.bobbing = 'down'

        if self.bobbing == 'down':
            if self.position['y'] > 0:
                self.position['y'] -= 0.00035 * speed
            if self.position['y'] <= 0 and (x_movement != 0 or z_movement != 0):
                self.bobbing = 'up'

        self.position['x'] -= x_movement * speed if can_walk_x == True else 0
        self.position['z'] -= z_movement * speed if can_walk_z == True else 0

        self.position['y']  -= (0.08*speed)    if (b'z' in self.key_buffer) else ((-0.08*speed)    if (b'x' in self.key_buffer) else 0)
        self.rotation       += (0.8*speed)     if (b'q' in self.key_buffer) else ((-0.8*speed)     if (b'e' in self.key_buffer) else 0)

    def addObject(self, obj):
        if obj.type == 'group':
            print('🧊 Adding GROUP on \t['+str(obj.position_x)+'\t'+str(obj.position_y)+'\t'+str(obj.position_z)+'] \t "'+obj.name+'"')
        else:
            print('🧊 Adding OBJECT on \t['+str(obj.position_x)+'\t'+str(obj.position_y)+'\t'+str(obj.position_z)+'] \t "'+obj.type+'"')
        self.objects.append(obj)
