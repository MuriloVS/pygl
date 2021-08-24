from OpenGL.GL import *
from OpenGL.GL.images import ImageInputConverter
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

class Basic:
    def __init__(self, position_x, position_y, position_z, size, color=[0.0, 0.0, 0.0]):
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.size       = size
        self.color      = color
        self.type       = 'basic'
    
    def move(self, x, y, z):
        self.position_x += x
        self.position_y += y
        self.position_z += z

    def colliding_x(self, x):
        raio = 2
        in_x = self.position_x < (x + self.size*raio) and self.position_x > (x - self.size*raio)
        return self.type != 'cone' and in_x

    def colliding_z(self, z):
        raio = 2
        in_z = self.position_z < (z + self.size*raio) and self.position_z > (z - self.size*raio)
        return self.type != 'cone' and in_z

    def colliding_y(self, y):
        raio = 2
        in_y = self.position_y < (y + self.size*raio) and self.position_y > (y - self.size*raio)
        return self.type != 'cone' and in_y

    def draw():
        print('Oi')
