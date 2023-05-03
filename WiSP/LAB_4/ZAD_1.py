from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

a = float(input("Please provide a: "))
n = int(input("Please provide n: "))


def show():
  angleIncrement = 360. / n
  angleIncrement *= np.pi / 180.
  glBegin(GL_TRIANGLE_FAN)

  angle = 0.

  #(s / 2) / r = sin(a / 2)
  #s / 2 = r * sin(a / 2)
  r = a / (2 * np.sin(a / 2))

  for _ in range(n):
    glVertex3f(r * np.cos(angle), r * np.sin(angle), 0.)
    angle += angleIncrement
  glEnd()
  glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 02")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()
