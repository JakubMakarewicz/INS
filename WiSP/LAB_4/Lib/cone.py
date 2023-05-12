from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.triangle_fan import triangle_fan
from Lib.circle import circle
from Lib.line import line

class cone:
  wall, base, line = None, None, None

  def __init__(self,x,y,z,r,h, color, approximation=40): 
    self.base = circle(x,y,z,r,color,approximation)
    self.wall = triangle_fan(np.concatenate(([(x,y,z+h)], self.base.fan.vertices)), color)
    self.line = line(self.base.fan.vertices, (1,1,1))

  def draw(self):
    self.wall.draw()
    self.base.draw()
    self.line.draw()