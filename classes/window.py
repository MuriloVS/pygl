from classes.basic import *
import math

COLORS = {
    'WHITE': [1.0, 1.0, 1.0],
    'BLACK': [0.0, 0.0, 0.0],
    'GREEN': [0.0, 1.0, 0.0],
    'BLUE':  [0.0, 0.0, 1.0],
    'BROWN': [1.0, 0.8, 0.6],
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
        self.ligh_position  = [0.0, 1.0, 0.0, 13.0]
        self.materials      = {
            "AMBIENT":  [0.2, 0.2, 0.2, 1.0],
            "DIFUSE":   [0.1, 0.1, 0.1, 1.0],
            "SPECULAR": [0.1, 0.1, 0.1, 1.0]
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
        glClearColor(self.background_color[0], self.background_color[1], self.background_color[2], 0.0)
        # Configurando shader
        glShadeModel(GL_SMOOTH)
        # Habilitando profundidade
        glEnable(GL_DEPTH_TEST)
        # Definindo materiais
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.materials['AMBIENT'])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.materials['DIFUSE'])
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.materials['SPECULAR'])
        glMaterialf(GL_FRONT, GL_SHININESS, 5.0)
        # Definindo e habilitando luzes
        glLightfv(GL_LIGHT0, GL_POSITION, self.ligh_position)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        # Definindo e habilitando modo de coloração
        glColorMaterial(GL_FRONT, GL_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        # Permitindo a mistura de cores e opacidade
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def configureGlutEvents(self):       
        glutDisplayFunc(self.glutDisplay)
        glutIdleFunc(self.glutDisplay)
        glutReshapeFunc(self.glutReshape)
        glutKeyboardFunc(self.glutKeyDown)
        glutKeyboardUpFunc(self.glutKeyUp)
        glutMotionFunc(self.glutMouseMove)
        glutMainLoop()
    
    def drawMinimap(self):
        glPushMatrix()

        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)

        map_max = 9

        size = 0.15
        dist = 0.52
        glTranslatef(-0.3, +0.3, 0.0)
        glColor([0.0, 0.0, 0.0, 0.75])
        glBegin(GL_POLYGON)
        glVertex3f(-size , -size, -dist)
        glVertex3f(-size , size, -dist)
        glVertex3f(size , size, -dist)
        glVertex3f(size , -size, -dist)
        glEnd()

        player_x = (self.position['x']/map_max)*size
        player_y = -(self.position['z']/map_max)*size

        dist = 0.51
        dot_size = 0.005
        glColor([0.6, 1.0, 0.6, 1])
        glPushMatrix()
        
        glTranslatef(player_x, player_y, 0.0)
        glRotatef(self.rotation, 0.0, 0.0, 1.0)
        glTranslatef(-player_x, -player_y, 0.0)

        glBegin(GL_POLYGON)
        glVertex3f(player_x-0.009,   player_y-0.0095,     -0.51)
        glVertex3f(player_x+0.009,   player_y-0.0095,     -0.51)
        glVertex3f(player_x+0.0,    player_y+0.0095,     -0.51)
        glEnd()

        glPopMatrix()
        # glBegin(GL_POLYGON)
        # glVertex3f(player_x-dot_size , player_y-dot_size, -dist)
        # glVertex3f(player_x-dot_size , player_y+dot_size, -dist)
        # glVertex3f(player_x+dot_size , player_y+dot_size, -dist)
        # glVertex3f(player_x+dot_size , player_y-dot_size, -dist)
        # glEnd()

        for obj in self.objects:
            dot_size = 0.01 * obj.size
            obj_x = (obj.position_x/map_max)*size
            obj_y = -(obj.position_z/map_max)*size
            color = [obj.color[0]+0.2, obj.color[1]+0.2, obj.color[2]+0.2]
            glColor(color)
            glBegin(GL_POLYGON)
            glVertex3f(obj_x-dot_size , obj_y-dot_size, -dist)
            glVertex3f(obj_x-dot_size , obj_y+dot_size, -dist)
            glVertex3f(obj_x+dot_size , obj_y+dot_size, -dist)
            glVertex3f(obj_x+dot_size , obj_y-dot_size, -dist)
            glEnd()


        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glPopMatrix()

    def glutDisplay(self):
        self.glutMovement()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        glPushMatrix()

        glTranslatef(self.position['x'], self.position['y'], self.position['z']) 

        glPushMatrix()
        glTranslatef(-self.position['x']*2, -self.position['y']*2, -self.position['z']*2) 
        rotate(self.position['x'], self.position['y'], self.position['z'], self.rotation, 'y')

        glPushMatrix()
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        glVertex3f(-60.0,   -0.5, -60.0)
        glVertex3f(60.0,    -0.5, -60.0)
        glVertex3f(60.0,    -0.5, 60.0)
        glVertex3f(-60.0,   -0.5, 60.0)
        glEnd()
        glPopMatrix()

        for obj in self.objects:
            obj.draw(True)

        glPopMatrix()
        glPopMatrix()

        # Interface
        self.drawMinimap()

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
        self.mouse_pos['x'] = x
        self.mouse_pos['x'] = y

    def glutKeyDown(self, key, x, y):
        self.key_buffer.append(key)

    def glutKeyUp(self, key, x, y):
        self.key_buffer.remove(key)

    def glutMovement(self):

        if self.jump_buffer > 0:
            self.position['y'] += 0.015 * self.jump_buffer/200 if self.jump_buffer > 600 else - 0.010 * 600/self.jump_buffer
            self.jump_buffer -= 1
            if self.position['y'] <= 0:
                self.position['y'] = 0
                self.jump_buffer = 0
        
        self.jump_buffer = 800 if (b' ' in self.key_buffer and self.jump_buffer <= 0) else self.jump_buffer

        self.rotation = self.rotation - 360 if self.rotation > 360 else self.rotation

        horizontal_movement = 0.002 if (b'd' in self.key_buffer) else -0.002 if (b'a' in self.key_buffer) else 0
        vertical_movement   = 0.002 if (b'w' in self.key_buffer) else -0.002 if (b's' in self.key_buffer) else 0

        x_movement = vertical_movement * math.sin(math.radians(self.rotation)) + horizontal_movement * math.sin(math.radians(self.rotation - 90))
        z_movement = vertical_movement * math.cos(math.radians(self.rotation)) + horizontal_movement * math.cos(math.radians(self.rotation - 90))

        can_walk_x = True
        can_walk_z = True

        # for obj in self.objects:
        #     x = self.position['x'] + x_movement
        #     z = self.position['z'] + z_movement
        #     print(can_walk_x)
        #     print(can_walk_z)
        #     can_walk_x = can_walk_x and obj.colliding_x(x)
        #     can_walk_z = can_walk_z and obj.colliding_z(z)

        


        self.position['x'] -= x_movement if can_walk_x == True else 0
        self.position['z'] -= z_movement if can_walk_z == True else 0

            # in_x = self.position['x'] < obj.position_x + obj.size*1.5 and self.position['x'] > obj.position_x - obj.size*1.5
            # in_z = self.position['z'] < obj.position_z + obj.size*1.5 and self.position['z'] > obj.position_z - obj.size*1.5
            # in_y = self.position['y'] < obj.position_y + obj.size*1.5 and self.position['y'] > obj.position_y - obj.size*1.5
            # if not (in_x and in_z and in_y):

        #self.position['y']  -= (0.002)    if (b'z' in self.key_buffer) else (-0.002)    if (b'x' in self.key_buffer) else 0 
        self.rotation       += (0.15)     if (b'q' in self.key_buffer) else (-0.15)     if (b'e' in self.key_buffer) else 0 

    def addObject(self, obj):
        self.objects.append(obj)
