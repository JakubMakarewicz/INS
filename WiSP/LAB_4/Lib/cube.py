from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import json
import vectorOperations
from Lib.rectangle import rectangle
from Lib.fig_base import fig_base

class cube(fig_base):
  walls = []
  vertices = []
  
  def __init__(self,x,y,z,a,b,c, color,posx,posy,posz):
    self.vertices = np.array([
      (x-a/2,y-b/2,z-c/2), 
      (x+a/2,y-b/2,z-c/2),
      (x+a/2,y+b/2,z-c/2),
      (x-a/2,y+b/2,z-c/2),
      (x-a/2,y-b/2,z+c/2),
      (x+a/2,y-b/2,z+c/2),
      (x+a/2,y+b/2,z+c/2),
      (x-a/2,y+b/2,z+c/2) 
    ])
    self.poz = [posx,posy,posz]
    self.color = color
    self.init_color = color

  def draw(self):
    vertices_rotated = np.array([
      np.dot(self.get_rotation(), np.array(vertex, dtype=np.float32))[0]
        + self.get_pos()
      for vertex in self.vertices
    ])
    print(vertices_rotated)

    self.walls = [
      rectangle(*vertices_rotated[[0,1,2,3]], self.color),
      rectangle(*vertices_rotated[[1,5,6,2]], self.color),
      rectangle(*vertices_rotated[[2,6,7,3]], self.color),
      rectangle(*vertices_rotated[[0,4,7,3]], self.color),
      rectangle(*vertices_rotated[[0,1,5,4]], self.color),
      rectangle(*vertices_rotated[[4,5,6,7]], self.color)
    ]
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