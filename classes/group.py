from classes.basic import *

class Group:
    def __init__(self, name, position_x, position_y, position_z):
        self.name = name
        self.type = 'group'
        self.objects = []
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z

    def addObject(self, object):
        self.objects.append(object)

    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
            glTranslatef(self.position_x, self.position_y, self.position_z)

        for obj in self.objects:
            if obj.type != 'group':
                obj.load_texture()
            obj.draw(own_matrix)

        if own_matrix:
            glPopMatrix()


    
