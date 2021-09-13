
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

