from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
vertices = np.array([
	(0,0,0), 
	(a,0,0),
	(a,b,0),
	(0,b,0),
	(0,0,c), 
	(a,0,c),
	(a,b,c),
	(0,b,c)	
])

walls = [
	((1,0,0),vertices[[0,1,2,3]]),
	((0,1,0),vertices[[1,5,6,2]]),
	((1,1,0),vertices[[2,6,7,3]]),
	((0,1,1),vertices[[0,4,7,3]]),
	((0,0,1),vertices[[0,1,5,4]]),
	((1,0,1),vertices[[4,5,6,7]])
]

def draw_cube():
	glBegin(GL_QUADS)
	for wall in walls:
		glColor3f(*wall[0])
		for i in range(4):
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
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 640)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 05a")
# glutCreateWindow("Program 05b")
glClearColor(1.0, 1.0, 1.0, 1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glutDisplayFunc(show)
glutMainLoop()