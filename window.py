
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
    'BROWN': [1.0, 0.8, 0.6],
    'SKY':   [0.53, 0.81, 0.92]
}

window = Window('OpenGL Practice', 500, 500)

coluna_01 = Cylinder(0.0, 0.6, -1.0, 0.09, 1.5, COLORS['WHITE'])
window.objects.append(coluna_01)

coluna_02 = Cylinder(-1.0, 0.6, -2.0, 0.09, 1.5, COLORS['WHITE'])
window.objects.append(coluna_02)

coluna_03 = Cylinder(1.0, 0.6, -2.0, 0.09, 1.5, COLORS['WHITE'])
window.objects.append(coluna_03)

coluna_04 = Cylinder(-1.0, 0.6, -3.0, 0.09, 1.5, COLORS['WHITE'])
window.objects.append(coluna_04)

coluna_05 = Cylinder(1.0, 0.6, -3.0, 0.09, 1.5, COLORS['WHITE'])
window.objects.append(coluna_05)

coluna_06 = Cylinder(0.0, 0.6, -4.0, 0.09, 1.5, COLORS['WHITE'])
window.objects.append(coluna_06)

# X, Y, Z, RAIO, ALTURA, COR
pilar = Cylinder(0.0, 1.1, -2.5, 0.45, 2.5, COLORS['WHITE'])
window.objects.append(pilar)

cone = Cone(0.0, 0.5, -2.5, 2.1, 0.8, COLORS['BROWN'])
window.objects.append(cone)

window.configureOpenGl()
window.configureGlutEvents()

