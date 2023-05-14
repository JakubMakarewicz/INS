from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
from Lib.triangle_fan import triangle_fan

class regular_fig:
  fan = None

  def __init__(self,a,n,color, draw_line=True): 
    angleIncrement = 360. / n
    angleIncrement *= np.pi / 180.

    angle = 0.
    r = a / (2 * np.sin(a / 2))
    vertices = []
    for _ in range(n):
      vertices.append((r * np.cos(angle), r * np.sin(angle), 0.))
      angle += angleIncrement

    self.fan = triangle_fan(vertices, color = color, draw_line=draw_line)

  def draw(self):
    self.fan.draw()