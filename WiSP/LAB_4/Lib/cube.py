from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import json
import vectorOperations
from Lib.rectangle import rectangle
from Lib.fig_base import fig_base

class cube(fig_base):
  walls = [] 

  def __init__(self,x,y,z,a,b,c, color,posx,posy,posz):
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
    self.poz = [posx,posy,posz]

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

  def get_triangles(self):
    triangles = []
    for wall in self.walls:
      for triangle in wall.get_triangles():
        triangles.append(triangle)
    return triangles

  def handle_collision(self, collision:bool):
    if self.is_colliding != collision:
      self.is_colliding = collision
      self.color = [self.init_color, np.array([1,0,0]*len(self.vertices), dtype=np.float32)][int(collision)]
      for wall in self.walls:
        wall.handle_collision(collision)

  def export(self, file_path):
    with open(file_path, 'w') as f:
      json.dump({ "triangles": self.get_triangles() }, f)