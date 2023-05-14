from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.rectangle import rectangle

class cube:
  walls = [] 

  def __init__(self,x,y,z,a,b,c, color):
    vertices = np.array([
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
      rectangle(*vertices[[0,1,2,3]], color),
      rectangle(*vertices[[1,5,6,2]], color),
      rectangle(*vertices[[2,6,7,3]], color),
      rectangle(*vertices[[0,4,7,3]], color),
      rectangle(*vertices[[0,1,5,4]], color),
      rectangle(*vertices[[4,5,6,7]], color)
    ]

  def draw(self):
    for wall in self.walls:
      wall.draw()