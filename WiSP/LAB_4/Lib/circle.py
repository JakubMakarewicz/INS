from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
from Lib.triangle_fan import triangle_fan

class circle:
  fan = None

  def __init__(self,x,y,z,r, color, approximation=40): 
    angleIncrement = 360. / approximation
    angleIncrement *= np.pi / 180.

    angle = 0.
    vertices = []

    for _ in range(approximation):
      vertices.append((x+r * np.cos(angle), y+r * np.sin(angle), z))
      angle += angleIncrement

    self.fan = triangle_fan(vertices, color = color)

  def draw(self):
    self.fan.draw()