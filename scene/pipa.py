from classes.dda import *

def generate_dda_pipa(position_x, position_y, position_z, color = [0, 0, 1]):
    pipa = DDA(
        position_x, position_y, position_z,
        [
            [0.0,  0.0, 0.0], #chão
            [1.0,  2.0, 0.0], #ponta baixo
            [1.1,  2.3, 0.0], #ponta lado 1
            [1.5,  2.2, 0.0], #ponta topo
            [1.4,  1.9, 0.0], #ponta lado 2
            [1.0,  2.0, 0.0], #ponta baixo (fechar)
            [1.5,  2.2, 0.0], #ponta topo (linha vertical x)
            [1.4,  1.9, 0.0], #ponta lado 2 (linha horizontal x)
            [1.1,  2.3, 0.0]  #ponta lado 1 (linha horizontal x)

        ],
        color
    )

    return pipa