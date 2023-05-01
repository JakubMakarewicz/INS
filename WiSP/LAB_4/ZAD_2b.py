from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

d = float(input("Please provide d: "))
z = float(input("Please provide z: "))
n = 3


r = d / (2 * np.sin(d / 2))
vertices = np.array([
	(r, r, 0.),
	(r * np.cos(120), r * np.sin(120), 0.),
	(r * np.cos(240), r * np.sin(240), 0.),
	(r, r+ d * np.sqrt(3)/2, z),
])

walls = [
	((1,0,0),vertices[[0,1,2]]),
	((0,1,0),vertices[[0,1,3]]),
	((1,1,0),vertices[[1,3,2]]),
	((1,0,1),vertices[[2,0,3]])
]

def draw_cube():
	glBegin(GL_TRIANGLES)
	for wall in walls:
		glColor3f(*wall[0])
		for i in range(3):
			glVertex3f(*wall[1][i])

	glEnd()

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
	draw_cube()
	glPopMatrix()
	glTranslate(-1 ,2, -3)
	draw_cube()
	glTranslate(-3 ,2, -3)
	draw_cube()
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 02")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()

