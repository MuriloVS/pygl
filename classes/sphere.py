from classes.basic import *
import math

class Sphere(Basic):
    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
        
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glutSolidSphere(self.size, 10, 10)

        if own_matrix:
            glPopMatrix()