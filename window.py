
import math
from PIL import Image
import numpy as np
from classes.window import *
from classes.cylinder import *
from classes.cone import *
from classes.cube import *
from classes.sphere import *

COLORS = {
    'WHITE': [1.0, 1.0, 1.0],
    'BLACK': [0.0, 0.0, 0.0],
    'GREEN': [0.0, 1.0, 0.0],
    'BLUE':  [0.0, 0.0, 1.0],
    'BROWN': [1.0, 0.9, 0.6],
    'SKY':   [0.53, 0.91, 0.92]
}

window = Window('OpenGL Practice', 500, 500)

class Telhado(Basic):
    def draw(self, own_matrix):
        if own_matrix:
            glPushMatrix()

        raio = 1.8
        altura_base = 0.6
        altura_pontas = 0.2
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

#Posição: x:0 z:-3 raio:1.5
custom = Telhado(0.0, 0.0, -3.0, 1.5, [1.0, 1.0, 1.0])
custom.set_texture('palha.jpg')
window.objects.append(custom)

coluna_01 = Cylinder(1.5, 0.2, -3 - 0.55, 0.045, 1.0, COLORS['WHITE'])
coluna_01.set_texture('wood.jpg')
window.objects.append(coluna_01)

coluna_02 = Cylinder(1.5, 0.2, -3 + 0.55, 0.045, 1.0, COLORS['WHITE'])
coluna_02.set_texture('wood.jpg')
window.objects.append(coluna_02)

coluna_03 = Cylinder(-1.5, 0.2, -3 - 0.55, 0.045, 1.0, COLORS['WHITE'])
coluna_03.set_texture('wood.jpg')
window.objects.append(coluna_03)

coluna_04 = Cylinder(-1.5, 0.2, -3 + 0.55, 0.045, 1.0, COLORS['WHITE'])
coluna_04.set_texture('wood.jpg')
window.objects.append(coluna_04)

coluna_05 = Cylinder(0.55, 0.2, -3 + 1.5, 0.045, 1.0, COLORS['WHITE'])
coluna_05.set_texture('wood.jpg')
window.objects.append(coluna_05)

coluna_06 = Cylinder(-0.55, 0.2, -3 + 1.5, 0.045, 1.0, COLORS['WHITE'])
coluna_06.set_texture('wood.jpg')
window.objects.append(coluna_06)

coluna_07 = Cylinder(0.55, 0.2, -3 - 1.5, 0.045, 1.0, COLORS['WHITE'])
coluna_07.set_texture('wood.jpg')
window.objects.append(coluna_07)

coluna_08 = Cylinder(-0.55, 0.2, -3 - 1.5, 0.045, 1.0, COLORS['WHITE'])
coluna_08.set_texture('wood.jpg')
window.objects.append(coluna_08)

# # X, Y, Z, RAIO, ALTURA, COR
pilar = Cylinder(0.0, 0.35, -3, 0.45, 2.5, COLORS['WHITE'])
pilar.set_texture('concrete.jpeg')
window.objects.append(pilar)


# coluna_01 = Cylinder(0.0, 0.6, -1.0, 0.09, 1.5, COLORS['WHITE'])
# coluna_01.set_texture('wood.jpg')
# window.objects.append(coluna_01)

# coluna_02 = Cylinder(-1.0, 0.6, -2.0, 0.09, 1.5, COLORS['WHITE'])
# coluna_02.set_texture('wood.jpg')
# window.objects.append(coluna_02)

# coluna_03 = Cylinder(1.0, 0.6, -2.0, 0.09, 1.5, COLORS['WHITE'])
# coluna_03.set_texture('wood.jpg')
# window.objects.append(coluna_03)

# coluna_04 = Cylinder(-1.0, 0.6, -3.0, 0.09, 1.5, COLORS['WHITE'])
# coluna_04.set_texture('wood.jpg')
# window.objects.append(coluna_04)

# coluna_05 = Cylinder(1.0, 0.6, -3.0, 0.09, 1.5, COLORS['WHITE'])
# coluna_05.set_texture('wood.jpg')
# window.objects.append(coluna_05)

# coluna_06 = Cylinder(0.0, 0.6, -4.0, 0.09, 1.5, COLORS['WHITE'])
# coluna_06.set_texture('wood.jpg')
# window.objects.append(coluna_06)

# # X, Y, Z, RAIO, ALTURA, COR
# pilar = Cylinder(0.0, 1.1, -2.5, 0.45, 2.5, COLORS['WHITE'])
# pilar.set_texture('concrete.jpeg')
# window.objects.append(pilar)

# cone = Cone(0.0, 0.5, -2.5, 2.1, 0.9, COLORS['BROWN'])
# cone.set_texture('palha.jpg')
# window.objects.append(cone)

window.configureOpenGl()
window.configureGlutEvents()

