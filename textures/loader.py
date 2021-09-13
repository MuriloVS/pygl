from PIL import Image
import numpy as np

def load_texture(path):
    print('📦 Loading texture: '+path)
    grass_image = Image.open(path).convert('RGBA')
    return {
        "height":   grass_image.height,
        "width":    grass_image.width,
        "data":     np.array(list(grass_image.getdata()), np.uint8)
    }

TEXTURES = {
    'PALHA':    load_texture('textures/palha.jpg'),
    'MADEIRA':  load_texture('textures/wood.jpg'),
    'CONCRETO': load_texture('textures/concrete.jpeg'),
    'GRAMA':    load_texture('textures/grass.jpg'),
    'AGUA':     load_texture('textures/agua.jpeg')
}