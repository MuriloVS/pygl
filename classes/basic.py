from OpenGL.GL import *
from OpenGL.GL.images import ImageInputConverter
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy
import math

class Basic:
    def __init__(self, position_x, position_y, position_z, size, color=[0.0, 0.0, 0.0]):
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.size       = size
        self.color      = color
        self.opacity    = 1
        self.type       = 'basic'
        self.lightning  = True

    def setTexture(self, texture):#file_name):
        #grass_image = Image.open(file_name).convert('RGBA')
        # self.image = {
        #     "height":   grass_image.height,
        #     "width":    grass_image.width,
        #     "data":     numpy.array(list(grass_image.getdata()), numpy.uint8)
        # }
        self.image = texture

    def setOpacity(self, opacity):
        self.opacity = opacity

    def setLightning(self, lightning):
        self.lightning = lightning
    
    def load_texture(self):
        if(hasattr(self,'image')):
            glEnable(GL_TEXTURE_2D)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.image['width'], self.image['height'], 0, GL_RGBA, GL_UNSIGNED_BYTE, self.image['data'])
            glGenerateMipmap(GL_TEXTURE_2D)
        else:
            glDisable(GL_TEXTURE_2D)
    
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
