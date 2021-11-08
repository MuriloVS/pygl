
import math
from scene.poste import generate_group_poste
from scene.mesa import generate_group_mesa
from scene.agua import generate_vertex_agua
from scene.quiosque_principal import generate_group_quiosque_principal
from scene.quiosque_secundario import generate_group_quiosque_secundario
from scene.gramado import generate_group_gramado
from PIL import Image
import numpy as np
from classes.window import *
from classes.vertex import *
from textures.loader import TEXTURES

window = Window('OpenGL Practice', 450, 450)

agua        = generate_vertex_agua(0.0, -0.7, 0.0, 6.0)
gramado     = generate_group_gramado(1, 0.0, -0.5)
quiosque_01 = generate_group_quiosque_principal(-0.5, 0.0001, -3.1)
quiosque_02 = generate_group_quiosque_secundario(0.5, 0.0, -4.1)


mesa_01     = generate_group_mesa(-0.5, -0.22, -1.8)
mesa_02     = generate_group_mesa(-1.7, -0.22, -3.1)
mesa_03     = generate_group_mesa(0.7, -0.22, -2.6)

mesa_04     = generate_group_mesa(0.6, -0.22, -2.6)
mesa_05     = generate_group_mesa(0.5, -0.22, -2.6)
mesa_06     = generate_group_mesa(0.4, -0.22, -2.6)
mesa_07     = generate_group_mesa(0.3, -0.22, -2.6)
mesa_08     = generate_group_mesa(0.2, -0.22, -2.6)
mesa_09     = generate_group_mesa(0.1, -0.22, -2.6)
mesa_10     = generate_group_mesa(0.0, -0.22, -2.6)

poste_01    = generate_group_poste(2.2, -0.22, -2.3)
poste_02    = generate_group_poste(3.2, -0.22, -2.3)
poste_03    = generate_group_poste(4.2, -0.22, -2.3)


agua.setAnimation(
    0.001,
    0.06, -0.7, 0.0,
    -0.06, -0.7, 0.0
)


agua.setLightning(False)
window.addObject(agua)
window.addObject(gramado)
window.addObject(quiosque_01)
window.addObject(quiosque_02)

window.addObject(mesa_01)
window.addObject(mesa_02)
window.addObject(mesa_03)


window.addObject(poste_01)
window.addObject(poste_02)
window.addObject(poste_03)

print('✔️ Loading complete! Initalizing...')
window.configureOpenGl()
window.configureGlutEvents()

