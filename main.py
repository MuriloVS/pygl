
import math
from scene.agua import generate_vertex_agua
from scene.quiosque import generate_group_quiosque
from scene.gramado import generate_group_gramado
from PIL import Image
import numpy as np
from classes.window import *
from classes.vertex import *
from textures.loader import TEXTURES

window = Window('OpenGL Practice', 500, 500)


agua        = generate_vertex_agua(0.0, -0.7, 0.0, 6.0)
gramado     = generate_group_gramado(0.5, 0.0, 0.0)
quiosque_01 = generate_group_quiosque(0.0, 0.0, -3.0)
quiosque_02 = generate_group_quiosque(1.0, 0.0, -4.0)

agua.setLightning(False)
window.addObject(agua)
window.addObject(gramado)
window.addObject(quiosque_01)
window.addObject(quiosque_02)

print('✔️ Loading complete! Initalizing...')
window.configureOpenGl()
window.configureGlutEvents()

