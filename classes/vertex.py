from classes.basic import *
import math

class Vertex(Basic):
    def __init__(self, position_x, position_y, position_z, gl_mode=GL_POLYGON, vertexes=[], normals=None, tex_coords=None):
        self.color      = [1.0, 1.0, 1.0]
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.type       = 'Vertex'
        self.vertexes   = vertexes
        self.normals    = normals
        self.gl_mode    = gl_mode
        self.size       = 0
        self.tex_coords = tex_coords
        self.opacity    = 1
        self.lightning  = True

    def setMode(self, gl_mode):
        self.gl_mode = gl_mode

    def setVertexes(self, vertexes):
        self.vertexes   = vertexes

    def setNormals(self, normals):
        self.normals    = normals

    def setTexcoords(self, tex_coords):
        self.tex_coords = tex_coords
    
    def set(self, normals, vertexes):
        self.setVertexes(vertexes)
        self.setNormals(normals)

    def addVertex(self, vertex):
        self.vertexes.append(vertex)
    
    def addNormal(self, normal):
        self.normals.append(normal)

    def add(self, vertex, normal):
        self.addVertex(vertex)
        self.addNormal(normal)

    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()
            glTranslatef(self.position_x, self.position_y, self.position_z)

        if not self.lightning:
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
        else:
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)

        glColor([1.0, 1.0, 1.0, self.opacity])
        glBegin(self.gl_mode)
        for index, vertex in enumerate(self.vertexes):
            glVertex3f(vertex[0], vertex[1], vertex[2])
            if self.normals != None:
                normal = self.normals[index]
                glNormal3f(normal[0], normal[1], normal[2])
            else:
                glNormal3f(0.5, 0.7, 0.5)
            if self.tex_coords != None:
                coord = self.tex_coords[index]
                glTexCoord(coord[0], coord[1])
        glEnd()

        if own_matrix:
            glPopMatrix()