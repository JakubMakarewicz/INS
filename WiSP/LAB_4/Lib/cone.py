from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.triangle_fan import triangle_fan
from Lib.circle import circle
from Lib.line import line
from Lib.fig_base import fig_base
class cone(fig_base):
  wall, base= None, None

  def __init__(self,x,y,z,r,h, color, approximation=40,posx=0,posy=0,posz=0):
    self.base = circle(x,y,z,r,color,approximation)
    self.wall = triangle_fan(np.concatenate(([(x,y,z+h)], self.base.fan.vertices)), color, draw_line=False)
    self.poz = [posx, posy, posz]

  def draw(self):
    self.wall.draw()
    self.base.draw()