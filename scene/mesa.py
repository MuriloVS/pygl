from classes.colors import COLORS
from classes.cylinder import Cylinder
from classes.vertex import *
from textures.loader import *
from classes.group import *

textura = TEXTURES['MADEIRA']

class customGroup(Group):
    def draw(self, own_matrix):
        #textura
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glTranslatef(self.position_x, self.position_y, self.position_z)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, textura['width'], textura['height'], 0, GL_RGBA, GL_UNSIGNED_BYTE, textura['data'])
        glGenerateMipmap(GL_TEXTURE_2D)
        #tampa
        glPushMatrix()
        glScalef(1.0, 0.12, 1.0)
        glutSolidCube(0.35)
        glPopMatrix()
        #perna_esquerda_frontal
        glPushMatrix()
        glTranslatef(-0.15, -0.35*0.8/2, 0.15)
        glScalef(0.07, 0.8, 0.07)
        glutSolidCube(0.35)
        glPopMatrix()
        #perna_esquerda_traseira
        glPushMatrix()
        glTranslatef(-0.15, -0.35*0.8/2, -0.15)
        glScalef(0.07, 0.8, 0.07)
        glutSolidCube(0.35)
        glPopMatrix()
        #perna_direita_frontal
        glPushMatrix()
        glTranslatef(0.15, -0.35*0.8/2, 0.15)
        glScalef(0.07, 0.8, 0.07)
        glutSolidCube(0.35)
        glPopMatrix()
        #perna_direita_traseira
        glPushMatrix()
        glTranslatef(0.15, -0.35*0.8/2, -0.15)
        glScalef(0.07, 0.8, 0.07)
        glutSolidCube(0.35)
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


def generate_group_mesa(position_x, position_y, position_z):
    mesa = customGroup('Mesa', position_x, position_y, position_z)

    # tampa = Vertex(
    #     0.0, 0.0, 0.0,
    #     GL_QUADS,
    #     [
    #         #face superior
    #         [-comprimento,  altura-largura, comprimento],
    #         [comprimento,   altura-largura, comprimento],
    #         [comprimento,   altura-largura, -comprimento],
    #         [-comprimento,  altura-largura, -comprimento],
    #         #face inferior
    #         [-comprimento,  altura,         -comprimento],
    #         [comprimento,   altura,         -comprimento],
    #         [comprimento,   altura,         comprimento],
    #         [-comprimento,  altura,         comprimento],
    #         #face esquerda
    #         [-comprimento,  altura-largura, comprimento],
    #         [-comprimento,  altura-largura, -comprimento],
    #         [-comprimento,  altura, -       comprimento],
    #         [-comprimento,  altura,         comprimento],
    #         #face direita
    #         [comprimento,   altura-largura, comprimento],
    #         [comprimento,   altura-largura, -comprimento],
    #         [comprimento,   altura,         -comprimento],
    #         [comprimento,   altura,         comprimento],
    #         #face frontal
    #         [-comprimento,  altura-largura, comprimento],
    #         [comprimento,   altura-largura, comprimento],
    #         [comprimento,   altura,         comprimento],
    #         [-comprimento,  altura,         comprimento],
    #         #face traseira
    #         [-comprimento,  altura-largura, -comprimento],
    #         [comprimento,   altura-largura, -comprimento],
    #         [comprimento,   altura,         -comprimento],
    #         [-comprimento,  altura,         -comprimento],
    #     ],
    # )
    # tampa.setTexture(TEXTURES['MADEIRA'])
    # mesa.addObject(tampa)
    
    return mesa