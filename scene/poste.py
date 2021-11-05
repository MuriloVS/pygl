from classes.colors import COLORS
from classes.cylinder import Cylinder
from classes.sphere import Sphere
from classes.vertex import *
from textures.loader import *
from classes.group import *


def generate_group_poste(position_x, position_y, position_z):
    poste = Group('Poste', position_x, position_y, position_z)

    base = Cylinder(
        0.0, -0.25, 0.0,
        0.025,
        0.025,
        10, 10)
    poste.addObject(base)

    corpo = Cylinder(
        0.0, 0.45, 0.0,
        0.020,
        0.7,
        10, 10)
    poste.addObject(corpo)

    lampada = Sphere(
        0.0, 0.5, 0.0,
        0.09,
        [1.0, 1.0, 1.0])
    poste.addObject(lampada)

    tampa =  Cylinder(
        0.0, 0.5 + 0.09 + 0.005, 0.0,
        0.025,
        0.010,
        10, 10)
    poste.addObject(tampa)
    
    return poste