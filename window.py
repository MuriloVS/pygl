
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

def translate(x, y, z):
    matrix = [
        [1,     0,      0,      0],
        [0,     1,      0,      0],
        [0,     0,      1,      0],
        [x,     y,      z,      1],
    ]
    return glMultMatrixf(matrix)

def rotate(x, y, z, angle, axis):
    translate(x, y, z)
    radians = math.radians(angle)
    cos = math.cos(radians)
    sin = math.sin(radians)
    if axis == 'x':
        matrix = [
            [1,     0,      0,      0],
            [0,     cos,    -sin,   0],
            [0,     sin,    cos,    0],
            [0,     0,      0,      1],
        ]
    elif axis == 'y':
        matrix = [
            [cos,   0,      sin,    0],
            [0,     1,      0,      0],
            [-sin,  0,      cos,    0],
            [0,     0,      0,      1],
        ]
    elif axis == 'z':
        matrix = [
            [cos,   sin,    0,      0],
            [-sin,  cos,    0,      0],
            [0,     0,      1,      0],
            [0,     0,      0,      1],
        ]
    else:
        return print(f'Rotate({x}, {y}, {z}, {angle}, {axis}) - Undefined axis')
    glMultMatrixf(matrix)
    return translate(-x, -y, -z)    

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

pilar = Cylinder(0.0, 0.6, -2.5, 0.2, 1.5, COLORS['WHITE'])
window.objects.append(pilar)

cone = Cone(0.0, 0.5, -2.5, 1.8, 1.8, COLORS['BROWN'])
window.objects.append(cone)

window.configureOpenGl()
window.configureGlutEvents()

