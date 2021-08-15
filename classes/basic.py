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
    
    def move(self, x, y, z):
        self.position_x += x
        self.position_y += y
        self.position_z += z

    def draw():
        print('Oi')
