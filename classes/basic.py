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

    def animate(self):
        try:
            direction = self.animation['direction']
            distance_x =  self.animation[direction][0] - self.position_x
            distance_y =  self.animation[direction][1] - self.position_y
            distance_z =  self.animation[direction][2] - self.position_z

            if distance_x != 0:
                movement_x = self.animation['speed'] * math.copysign(1, distance_x)
                if abs(movement_x) < abs(distance_x):
                    self.position_x += self.animation['speed'] * math.copysign(1, distance_x)
                else:
                    self.position_x = self.animation[direction][0]

            if distance_y != 0:
                movement_y = self.animation['speed'] * math.copysign(1, distance_y)
                if abs(movement_y) < abs(distance_y):
                    self.position_y += self.animation['speed'] * math.copysign(1, distance_y)
                else:
                    self.position_y = self.animation[direction][1]

            if distance_z != 0:
                movement_z = self.animation['speed'] * math.copysign(1, distance_z)
                if abs(movement_z) < abs(distance_z):
                    self.position_z += self.animation['speed'] * math.copysign(1, distance_z)
                else:
                    self.position_z = self.animation[direction][2]

            if distance_x == 0 and distance_y == 0 and distance_z == 0:
                self.animation['direction'] = "start" if direction == "end" else "end"
        except:
            return


    def setAnimation(self, speed, end_x, end_y, end_z, start_x=None, start_y=None, start_z=None):
        self.animation = {
            "direction": "end",
            "speed": speed,
            "start": [
                start_x if start_x != None else self.position_x,
                start_y if start_y != None else self.position_y,
                start_z if start_z != None else self.position_z,
            ],
            "end": [
                end_x,
                end_y,
                end_z
            ]
        }