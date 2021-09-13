from classes.colors import COLORS
from classes.cylinder import Cylinder
from classes.vertex import *
from textures.loader import *
from classes.group import *


def generate_group_quiosque_principal(position_x, position_y, position_z):
    quiosque = Group('Quiosque', position_x, position_y, position_z)

    #Posição: x:0 z:-3 raio:1.5
    raio = 1.8
    altura_base = 0.7
    altura_pontas = 0.2
    distancia_pilares = 0.6
    telhado = Vertex(
        0.0, 0.0, 0.0,
        GL_POLYGON,
        [
            [0.0, altura_base, 0.0],
            [-raio, altura_pontas, +distancia_pilares],
            [-raio, altura_pontas, -distancia_pilares],
            [-distancia_pilares, altura_pontas, -raio],
            [+distancia_pilares, altura_pontas, -raio],
            [+raio, altura_pontas, -distancia_pilares],
            [+raio, altura_pontas, +distancia_pilares],
            [+distancia_pilares, altura_pontas, +raio],
            [-distancia_pilares, altura_pontas, +raio],
            [-raio, altura_pontas, +distancia_pilares]
        ],
        [
            [0, 0.7, 0],
            [-0.9, 0.4, -0.9],
            [-0.9, 0.4, 0.9],
            [-0.9, 0.4, -0.9],
            [0.9, 0.4, -0.9],
            [0.9, 0.4, -0.9],
            [0.9, 0.4, 0.9],
            [0.9, 0.4, -0.9],
            [-0.9, 0.4, -0.9],
            [0,0,1]
        ]
    )
    telhado.setTexture(TEXTURES['PALHA'])
    quiosque.addObject(telhado)

    raio = 1.6
    altura_chao = -0.489
    chao = Vertex(
        0.0, altura_chao, 0.0,
        GL_POLYGON,
        [
            [0.0, 0.0, 0.0],
            [-raio, 0.0, +distancia_pilares],
            [-raio, 0.0, -distancia_pilares],
            [-distancia_pilares, 0.0, -raio],
            [+distancia_pilares, 0.0, -raio],
            [+raio, 0.0, -distancia_pilares],
            [+raio, 0.0, +distancia_pilares],
            [+distancia_pilares, 0.0, +raio],
            [-distancia_pilares, 0.0, +raio],
            [-raio, 0.0, +distancia_pilares]
        ]
    )
    chao.setTexture(TEXTURES['CONCRETO'])
    quiosque.addObject(chao)


    coluna_01 = Cylinder(1.5, 0.25, - 0.55, 0.045, 1.0, COLORS['WHITE'])
    coluna_01.setTexture(TEXTURES['MADEIRA'])
    #quiosque.addObject(coluna_01)

    coluna_02 = Cylinder(1.5, 0.25, + 0.55, 0.045, 1.0, COLORS['WHITE'])
    coluna_02.setTexture(TEXTURES['MADEIRA'])
    quiosque.addObject(coluna_02)

    coluna_03 = Cylinder(-1.5, 0.25, - 0.55, 0.045, 1.0, COLORS['WHITE'])
    coluna_03.setTexture(TEXTURES['MADEIRA'])
    quiosque.addObject(coluna_03)

    coluna_04 = Cylinder(-1.5, 0.25,+ 0.55, 0.045, 1.0, COLORS['WHITE'])
    coluna_04.setTexture(TEXTURES['MADEIRA'])
    quiosque.addObject(coluna_04)

    coluna_05 = Cylinder(0.55, 0.25, + 1.5, 0.045, 1.0, COLORS['WHITE'])
    coluna_05.setTexture(TEXTURES['MADEIRA'])
    quiosque.addObject(coluna_05)

    coluna_06 = Cylinder(-0.55, 0.25, + 1.5, 0.045, 1.0, COLORS['WHITE'])
    coluna_06.setTexture(TEXTURES['MADEIRA'])
    quiosque.addObject(coluna_06)

    coluna_07 = Cylinder(0.55, 0.25, - 1.5, 0.045, 1.0, COLORS['WHITE'])
    coluna_07.setTexture(TEXTURES['MADEIRA'])
    #quiosque.addObject(coluna_07)

    coluna_08 = Cylinder(-0.55, 0.25, - 1.5, 0.045, 1.0, COLORS['WHITE'])
    coluna_08.setTexture(TEXTURES['MADEIRA'])
    # quiosque.addObject(coluna_08)

    # # X, Y, Z, RAIO, ALTURA, COR
    pilar = Cylinder(0.0, 0.5, 0.0, 0.7, 2.5, COLORS['WHITE'])
    pilar.setTexture(TEXTURES['CONCRETO'])
    quiosque.addObject(pilar)
    
    return quiosque