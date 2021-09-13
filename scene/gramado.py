from classes.vertex import *
from textures.loader import *
from classes.group import *


def generate_group_gramado(position_x, position_y, position_z):
    gramado = Group('Entrada Lago', position_x, position_y, position_z)

    entrada_lago_esq = Vertex(
        0.0, -0.5, 0.0,
        GL_POLYGON,
        [
            [0.0, 0.0,  0.0],
            [0.0, 0.0, -0.8],
            [0.5, -0.5, -0.8],
            [0.5, -0.5, 0.0],
        ]
    )
    entrada_lago_esq.setTexture(TEXTURES['GRAMA'])
    gramado.addObject(entrada_lago_esq)

    entrada_lago_sup = Vertex(
        0.0, -0.5, 0.0,
        GL_POLYGON,
        [
            [0.5, 0.0, -1.3],
            [3, 0.0, -1.3],
            [3, -0.5,-.8],
            [0.5, -0.5, -.8],
        ]
    )
    entrada_lago_sup.setTexture(TEXTURES['GRAMA'])
    gramado.addObject(entrada_lago_sup)

    fundo_lago = Vertex(
        0.0, 0.0, 0.0,
        GL_POLYGON,
        [
            [0.5, -1.0, 0.0],
            [0.5, -1.0, -.8],
            [1.5, -1.0, -.8],
            [1.5, -1.0, 0.0],
        ]
    )
    fundo_lago.setTexture(TEXTURES['GRAMA'])
    gramado.addObject(fundo_lago)

    entrada_lago_diag = Vertex(
        0.0, -0.5, 0.0,
        GL_POLYGON,
        [
            [0.0, 0.0, -0.8],
            [0.5, 0.0, -1.3],
            [0.5, -0.5, -.8],
        ]
    )
    entrada_lago_diag.setTexture(TEXTURES['GRAMA'])
    gramado.addObject(entrada_lago_diag)

    grama_sup_esq = Vertex(
        0.0, 0.0, 0.0,
        GL_POLYGON,
        [
            [-5.0, -0.5, 0.0],
            [-5.0, -0.5, -6.0],
            [0.0, -0.5, -6.0],
            [0.0, -0.5, 0.0],
        ],
    )
    grama_sup_esq.setTexture(TEXTURES['GRAMA'])
    gramado.addObject(grama_sup_esq)

    grama_sup_dir = Vertex(
        0.0, 0.0, 0.0,
        GL_POLYGON,
        [
            [0.0, -0.5, -1.3],
            [0.0, -0.5, -6.0],
            [3.0, -0.5, -6.0],
            [3.0, -0.5, -1.3],
        ],
    )
    grama_sup_dir.setTexture(TEXTURES['GRAMA'])
    gramado.addObject(grama_sup_dir)

    grama_sup_centro = Vertex(
        0.0, 0.0, 0.0,
        GL_POLYGON,
        [
            [0.0, -0.5, -1.3],
            [0.5, -0.5, -1.3],
            [0.0, -0.5, -0.8],
        ],
    )
    grama_sup_centro.setTexture(TEXTURES['GRAMA'])
    gramado.addObject(grama_sup_centro)

    return gramado