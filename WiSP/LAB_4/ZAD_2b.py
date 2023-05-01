from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.pyramid import pyramid

d = float(input("Please provide d: "))
z = float(input("Please provide z: "))

def show():
	glClearColor(0, 0, 0, 1)
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
	pyramid(0,0,0,d,z).draw((1,1,0))
	glPopMatrix()
	glTranslate(-1 ,2, -3)
	pyramid(0,0,0,d,z).draw((1,1,0))
	glTranslate(-3 ,2, -3)
	pyramid(0,0,0,d,z).draw((1,1,0))
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 02")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()

