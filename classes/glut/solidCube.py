from classes.basic import *

def drawBox(size, type):
    n = [
        [-1.0, 0.0,  0.0],
        [0.0,  1.0,  0.0],
        [1.0,  0.0,  0.0],
        [0.0, -1.0,  0.0],
        [0.0,  0.0,  1.0],
        [0.0,  0.0, -1.0],
    ]
    faces = [
        [0, 1, 2, 3],
        [3, 2, 6, 7],
        [7, 6, 5, 4],
        [4, 5, 1, 0],
        [5, 6, 2, 1],
        [7, 4, 0, 3]
    ]
    
    v = []
    i = 5

    v[0][0] = v[1][0] = v[2][0] = v[3][0] = -size / 2
    v[4][0] = v[5][0] = v[6][0] = v[7][0] = size / 2
    v[0][1] = v[1][1] = v[4][1] = v[5][1] = -size / 2
    v[2][1] = v[3][1] = v[6][1] = v[7][1] = size / 2
    v[0][2] = v[3][2] = v[4][2] = v[7][2] = -size / 2
    v[1][2] = v[2][2] = v[5][2] = v[6][2] = size / 2

    while(i >= 0):
        glBegin(type)
        glNormal3fv(n[i][0])
        glVertex3fv(v[faces[i][0]][0])
        glVertex3fv(v[faces[i][1]][0])
        glVertex3fv(v[faces[i][2]][0])
        glVertex3fv(v[faces[i][3]][0])
        glEnd();
        i += 1

def glutSolidCube(size):
  drawBox(size, GL_QUADS)
