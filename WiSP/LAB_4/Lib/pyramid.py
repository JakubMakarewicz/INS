from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.triangle import triangle
from Lib.line import line

class pyramid:
  walls = [] 

  def __init__(self,x,y,z,a,h, color,posx=0,posy=0,posz=0):
    r = a / (2 * np.sin(a / 2))
    vertices = np.array([
      (x+r, y+r, z+0.),
      ((x+r) * np.cos(120), (y+r) * np.sin(120), z+0.),
      ((x+r) * np.cos(240), (y+r) * np.sin(240), z+0.),
      (x+r, y+r + a * np.sqrt(3)/2, z+h),
    ])

    self.poz = [posx, posy, posz]

    self.walls = [
      triangle(*vertices[[0,1,2]], color),
      triangle(*vertices[[0,1,3]], color),
      triangle(*vertices[[1,3,2]], color),
      triangle(*vertices[[2,0,3]], color)
    ]

  def draw(self):
    for wall in self.walls:
      wall.draw()