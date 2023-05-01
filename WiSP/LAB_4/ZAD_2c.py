from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

h = float(input("Please provide h: "))
r = float(input("Please provide r: "))

n=30 # circle approximation

def draw_circle(z):
	glBegin(GL_TRIANGLE_FAN)
	angleIncrement = 360. / n
	angleIncrement *= np.pi / 180.

	angle = 0.

	for _ in range(n):
		glVertex3f(r * np.cos(angle), r * np.sin(angle), z)
		angle += angleIncrement
	glEnd()

def draw_side():
	angleIncrement = 360. / n
	angleIncrement *= np.pi / 180.

	angle = 0.

	for _ in range(n):
		glBegin(GL_QUADS)
		glVertex3f(r * np.cos(angle), r * np.sin(angle), 0)
		glVertex3f(r * np.cos(angle), r * np.sin(angle), h)
		angle += angleIncrement
		glVertex3f(r * np.cos(angle), r * np.sin(angle), h)
		glVertex3f(r * np.cos(angle), r * np.sin(angle), 0)
		glEnd()

def draw_cilinder():
	glColor3f(1,0,0)
	draw_circle(0)
	glColor3f(0,0,1)
	draw_side()
	glColor3f(0,1,0)
	draw_circle(h)

def show():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glViewport(0, 0, 640, 480)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# Program 05a
	glFrustum(-2, 2, -2, 2, 1, 10)
	# Program 05b
	#glOrtho(-2, 2, -2, 2, 1, 10)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glPushMatrix()
	glTranslate(2, 2, -3)
	draw_cilinder()
	glPopMatrix()
	glTranslate(-1 ,2, -3)
	draw_cilinder()
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 02")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()

