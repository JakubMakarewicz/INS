from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.rectangle import rectangle
from Lib.line import line

class cube:
  vertices, walls = [],[] 

  def __init__(self,x,y,z,a,b,c):      
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
      self.vertices[[0,1,2,3]],
      self.vertices[[1,5,6,2]],
      self.vertices[[2,6,7,3]],
      self.vertices[[0,4,7,3]],
      self.vertices[[0,1,5,4]],
      self.vertices[[4,5,6,7]]
    ]

  def draw(self, color):
    for wall in self.walls:
      line(*wall).draw((1,1,1))
    for wall in self.walls:
      rectangle(*wall).draw(color)