
import math
from scene.agua import generate_vertex_agua
from scene.quiosque_principal import generate_group_quiosque_principal
from scene.quiosque_secundario import generate_group_quiosque_secundario
from scene.gramado import generate_group_gramado
from PIL import Image
import numpy as np
from classes.window import *
from classes.vertex import *
from textures.loader import TEXTURES

window = Window('OpenGL Practice', 500, 500)


agua        = generate_vertex_agua(0.0, -0.7, 0.0, 6.0)
gramado     = generate_group_gramado(1, 0.0, -0.5)
quiosque_01 = generate_group_quiosque_principal(0.0, 0.0001, -3.0)
quiosque_02 = generate_group_quiosque_secundario(1.0, 0.0, -4.0)

agua.setLightning(False)
window.addObject(agua)
window.addObject(gramado)
window.addObject(quiosque_01)
window.addObject(quiosque_02)

print('✔️ Loading complete! Initalizing...')
window.configureOpenGl()
window.configureGlutEvents()

