
import math
from scene.quiosque import generate_group_quiosque
from scene.gramado import generate_group_gramado
from PIL import Image
import numpy as np
from classes.window import *
from classes.cylinder import *
from classes.cone import *
from classes.cube import *
from classes.sphere import *
from classes.vertex import *
from classes.group import *
from textures.loader import TEXTURES

window = Window('OpenGL Practice', 500, 500)

class Telhado(Basic):
    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()

        raio = 1.8
        altura_base = 0.6
        altura_pontas = 0.1
        distancia_pilares = 0.6
        
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glColor(self.color)
        glBegin(GL_TRIANGLE_FAN)

        #Ponto central
        glVertex3f(0.0, altura_base, 0.0)
        glNormal3f(0, 0.7, 0)

        #Pilares leste
        glVertex3f(-raio, altura_pontas, +distancia_pilares)
        glNormal3f(-0.9, 0.4, -0.9)
        glVertex3f(-raio, altura_pontas, -distancia_pilares)
        glNormal3f(-0.9, 0.4, 0.9)

        #Pilares norte
        glVertex3f(-distancia_pilares, altura_pontas, -raio)
        glNormal3f(-0.9, 0.4, -0.9)
        glVertex3f(+distancia_pilares, altura_pontas, -raio)
        glNormal3f(0.9, 0.4, -0.9)

        #Pilares oeste
        glVertex3f(+raio, altura_pontas, -distancia_pilares)
        glNormal3f(0.9, 0.4, -0.9)
        glVertex3f(+raio, altura_pontas, +distancia_pilares)
        glNormal3f(0.9, 0.4, 0.9)

        #Pilares sul
        glVertex3f(+distancia_pilares, altura_pontas, +raio)
        glNormal3f(0.9, 0.4, -0.9)
        glVertex3f(-distancia_pilares, altura_pontas, +raio)
        glNormal3f(-0.9, 0.4, -0.9)

        #Voltando para o inicio
        glVertex3f(-raio, altura_pontas, +distancia_pilares)
        glNormal3f(0,0,1)

        glEnd()
        # glutWireCone(self.size, self.height, 10, 10)

        if own_matrix:
            glPopMatrix()

agua = Vertex(
    0.0, -0.8, 0.0,
    GL_POLYGON,
    [
        [-6.0, 0.0, -6.0],
        [-6.0, 0.0, 6.0],
        [6.0, 0.0, 6.0],
        [6.0, 0.0, -6.0],
    ]
)
agua.setTexture(TEXTURES['AGUA'])
window.addObject(agua)

gramado = generate_group_gramado(0.5, 0.0, 0.0)
quiosque_01 = generate_group_quiosque(0.0, 0.0, -3.0)
quiosque_02 = generate_group_quiosque(1.0, 0.0, -4.0)

window.addObject(gramado)
window.addObject(quiosque_01)
window.addObject(quiosque_02)

print('✔️ Loading complete! Initalizing...')
window.configureOpenGl()
window.configureGlutEvents()

