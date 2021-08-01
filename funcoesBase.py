from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

#As funções devem estar funcionando para o 3D também

#Falta
#Função para projeções perspectiva e ortogonal(pesquisar sobre)
#Aplicação de um dos algoritmos de visibilidade(pesquisar sobre)

#Ideias
#Criar classe para definir e manipular objetos sem a necessidade de enviar tantas referências as funções

#Dúvidas
#glutIdleFunc(showScreen) Animação?
# https://www.dca.ufrn.br/~ambj/opengl/projecoes-exercicios.html
# https://www.inf.pucrs.br/~pinho/CG-PPGCC/PraticaOpenGL2/PraticaOpenGL2.html
#(ARRUMADO) Porque chama iterate dentro de showScreen? Pq não posso chamar por main?
# Pq tão estranho trabalhar com pilhas?? dificuldade para manipular objetos com pilhas (push e pop)
# na teoria é mais fácil que na prática

w, h = 500, 500
x_inicial, y_inicial, z_inicial, tamanho = 100, 200, 20, 100


def nosso_translate(x, y, z):
    matrix = [[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0], 
              [x, y, z, 1]]
    return glMultMatrixf(matrix)

def nosso_scale(x, y, z, s):
    nosso_translate(x, y, z) #empilha objeto na posição inicial
    matrix = [[s,0,0,0],
              [0,s,0,0],
              [0,0,s,0],
              [0,0,0,1]]
    glMultMatrixf(matrix) #escala objeto          
    return nosso_translate(-x, -y, -z) #empilha objeto trazido para origem  
    
def nosso_rotate(x, y, z, angle, axis):
    nosso_translate(x, y, z) #empilha objeto na posição inicial
    radians = math.radians(angle)
    c = math.cos(radians)
    s = math.sin(radians)
    if axis == 'x': #escolhe eixo de referência para rotação
        matrix = [[1, 0, 0, 0],
                  [0, c, -s, 0],
                  [0, s, c, 0], 
                  [0, 0, 0, 1]]
    elif axis == 'y':
        matrix = [[c, 0, s, 0],
                  [0, 1, 0, 0],
                  [-s, 0, c, 0], 
                  [0, 0, 0, 1]]
    else: #axis == 'z'
        matrix = [[c, s, 0, 0],
                [-s, c, 0, 0],
                [0, 0, 1, 0], 
                [0, 0, 0, 1]]
    glMultMatrixf(matrix) #rotacionando objeto
    return nosso_translate(-x, -y, -z) #empilha objeto trazido para origem

def empty_square(x, y, size):   
    glBegin(GL_LINE_LOOP) 
    glVertex2f(x, y)
    glVertex2f(x+size, y)
    glVertex2f(x+size, y+size)
    glVertex2f(x, y+size)
    glEnd()

def iterate(width, height): #Projeção
    glViewport(0, 0, GLsizei(width), GLsizei(height))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    #glFrustum(-3.0, 3.0, -3.0, 3.0, 2, 30.0) #Para testes com objetos 3D dá p usar o exercício
    #glOrtho(-4.0, 4.0, -4.0, 4.0, 2, 30.0) #da aula para praticar - parâmetros já ajustados
    glMatrixMode (GL_MODELVIEW)

def showScreen():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
    glColor3f(0.0, 0.0, 0.0)
    glLoadIdentity()

    empty_square(x_inicial, y_inicial, tamanho)
    nosso_scale(x_inicial, y_inicial, 0, 2)
    nosso_rotate(x_inicial, y_inicial, 0, -45, 'z') 
    empty_square(x_inicial, y_inicial, tamanho)

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding Practice")   

    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutReshapeFunc(iterate)
    
    glutMainLoop() #Eventos
    return

main()
