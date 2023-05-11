from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.rectangle import rectangle
from Lib.line import line

class cube:
  vertices, walls, line = [],[], None 

  def __init__(self,x,y,z,a,b,c, color):
    self.vertices = np.array([
      (x+0,y+0,z+0), 
      (x+a,y+0,z+0),
      (x+a,y+b,z+0),
      (x+0,y+b,z+0),
      (x+0,y+0,z+c), 
      (x+a,y+0,z+c),
      (x+a,y+b,z+c),
      (x+0,y+b,z+c)  
    ])

    self.walls = [
      rectangle(*self.vertices[[0,1,2,3]], color),
      rectangle(*self.vertices[[1,5,6,2]], color),
      rectangle(*self.vertices[[2,6,7,3]], color),
      rectangle(*self.vertices[[0,4,7,3]], color),
      rectangle(*self.vertices[[0,1,5,4]], color),
      rectangle(*self.vertices[[4,5,6,7]], color)
    ]

    self.line = line((0,1,0),*self.vertices)

  def draw(self):
    self.line.draw()
    for wall in self.walls:
      wall.draw()