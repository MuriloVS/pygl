from classes.basic import *
import math

class Cube(Basic):
    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
        
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glutSolidCube(self.size)

        if own_matrix:
            glPopMatrix()