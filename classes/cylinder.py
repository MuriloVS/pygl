from classes.basic import *
import math

class Cylinder(Basic):
    def __init__(self, position_x, position_y, position_z, radius, height, around_z, along_z, color=[0.0, 0.0, 0.0]):
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.radius     = radius
        self.height     = height
        self.around_z   = around_z
        self.along_z    = along_z
        self.color      = color
        self.type       = 'cilinder'
        self.opacity    = 1
        self.lightning  = True
        self.size       = radius

    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
        
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glRotatef(90, 1.0, 0.0, 0.0)
        glutSolidCylinder(self.radius, self.height, self.around_z, self.along_z)

        if own_matrix:
            glPopMatrix()
