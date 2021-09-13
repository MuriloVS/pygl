from classes.vertex import *
from textures.loader import *

def generate_vertex_agua(position_x, position_y, position_z, size):
    agua = Vertex(
        position_x, position_y, position_z,
        GL_POLYGON,
        [
            [-size, 0.0, -size],
            [-size, 0.0, size],
            [size, 0.0,  size],
            [size, 0.0, -size],
        ]
    )
    agua.setTexture(TEXTURES['AGUA'])
    return agua