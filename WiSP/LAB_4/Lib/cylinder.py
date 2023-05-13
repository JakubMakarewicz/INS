from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.triangle_strip import triangle_strip
from Lib.circle import circle
from Lib.line import line

class cylinder:
  wall, base, top  = None, None, None

  def __init__(self,x,y,z,r,h, color, approximation=40):
    self.base = circle(x,y,z,r,color, approximation)
    self.top  = circle(x,y,z+h,r,color,approximation)
    self.wall = triangle_strip(
      np.array([(_a,_b) for _a,_b in zip(self.base.fan.vertices, self.top.fan.vertices)]).reshape(2*approximation+2, 3), 
      color,
      draw_line = False)
  
  def draw(self):
    self.wall.draw()
    self.base.draw()
    self.top.draw()