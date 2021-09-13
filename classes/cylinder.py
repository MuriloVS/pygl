from classes.basic import *
import math

class Cylinder(Basic):
    def __init__(self, position_x, position_y, position_z, size, height, color=[0.0, 0.0, 0.0]):
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.size       = size
        self.color      = color
        self.height     = height
        self.type       = 'cilinder'
        self.opacity    = 1
        self.lightning  = True

    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
        
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glRotatef(90, 1.0, 0.0, 0.0)
        glutSolidCylinder(self.size, self.height, 6, 6)

        if own_matrix:
            glPopMatrix()
