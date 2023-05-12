from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.triangle_strip import triangle_strip
from Lib.circle import circle
from Lib.line import line

class cylinder:
  wall, base, top, line_base, line_top  = None, None, None, None, None

  def __init__(self,x,y,z,r,h, color, approximation=40):
    self.base = circle(x,y,z,r,color, approximation)
    self.top  = circle(x,y,z+h,r,color,approximation)
    self.line_base = line(self.base.fan.vertices, (1,1,1))
    self.line_top = line(self.top.fan.vertices, (1,1,1))
    self.wall = triangle_strip(np.array([(_a,_b) for _a,_b in zip(self.base.fan.vertices, self.top.fan.vertices)]).reshape(2*approximation, 3), color)
  
  def draw(self):
    self.base.draw()
    self.top.draw()
    self.wall.draw()
    self.line_base.draw()
    self.line_top.draw()