from classes.basic import *
import math

class Cone(Basic):
    def __init__(self, position_x, position_y, position_z, size, height, color=[0.0, 0.0, 0.0]):
        print('🧊 Creating "CONE" on '+position_x+', '+position_y+', '+position_z)
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.size       = size
        self.color      = color
        self.height     = height
        self.type       = 'cone'

    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
        
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glRotatef(-90, 1.0, 0.0, 0.0)
        glutSolidCone(self.size, self.height, 10, 10)
        # glutWireCone(self.size, self.height, 10, 10)

        if own_matrix:
            glPopMatrix()
