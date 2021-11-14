from classes.basic import *
import math

class DDA(Basic):
	def __init__(self, position_x, position_y, position_z, points, color = [0.0, 0.0, 0.0], gl_mode=GL_POINTS):
		self.position_x = position_x
		self.position_y = position_y
		self.position_z = position_z
		self.points     = points
		self.color      = color
		self.opacity    = 1
		self.type       = "Points"
		self.lightning = False

	def draw(self, own_matrix):

		if own_matrix:
		    glPushMatrix()
		    glTranslatef(self.position_x, self.position_y, self.position_z)

		if not self.lightning:
			glDisable(GL_LIGHTING)
			glDisable(GL_LIGHT0)
		else:
			glEnable(GL_LIGHTING)
			glEnable(GL_LIGHT0)

		glColor3f(self.color[0], self.color[1], self.color[2])
		glPointSize(3)

		glBegin(GL_POINTS)

		for index in range (0, len(self.points)-1):
			self.rasterization(self.points[index][0], self.points[index+1][0],
			                   self.points[index][1], self.points[index+1][1])

		glEnd()

		if own_matrix:
		    glPopMatrix()

	def rasterization(self, x1, x2, y1, y2):

		dx = x2 - x1
		dy = y2 - y1

		if abs(dx) > abs(dy):
			# valores muito pequenos, por isso * 100
			steps = abs(dx)*100
		else:
			steps = abs(dy)*100

		incrementx = dx/steps
		incrementy = dy/steps

		x = x1
		y = y1
		i = 0

		while i < steps:
			i += 1
			glVertex3f(x, y, self.position_z)
			x += incrementx
			y += incrementy

		return