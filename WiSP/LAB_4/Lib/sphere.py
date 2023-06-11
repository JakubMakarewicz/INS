from OpenGL.GLUT import *
import json
from OpenGL.GL import *
import numpy as np
import random 
from Lib.circle import circle
from Lib.triangle_strip import triangle_strip
from Lib.triangle_fan import triangle_fan

from Lib.fig_base import fig_base

class sphere(fig_base):
  circles, strips, fans = list(), list(), list()

  def _color(self):
    return (random.randint(0,1),random.randint(0,1),random.randint(0,1))

  def __init__(self,x,y,z,r,approximation_vertical, approximation_horizontal, color,posx, posy, posz):
    self.circles.clear()
    self.strips.clear()
    self.fans.clear()
    self.circles.append(circle(x,y,z,r,self._color(),approximation_horizontal))
    self.poz = [posx, posy, posz]
    for i in range(1,approximation_vertical+1):
      hn = i*r/(approximation_vertical+1)
      rn = np.sqrt(np.power(r,2) - np.power(hn,2))
      self.circles.append(circle(x,y,z+hn,rn,self._color(),approximation_horizontal))
      self.circles.append(circle(x,y,z-hn,rn,self._color(),approximation_horizontal))
      self.strips.append(triangle_strip.from_circles(self.circles[-3], self.circles[-1], self._color()))
      self.strips.append(triangle_strip.from_circles(self.circles[max(-len(self.circles),-4)], self.circles[-2], self._color()))

    self.fans.append(triangle_fan(np.concatenate(([(x,y,z-r)], self.circles[-1].fan.vertices)), self._color()))
    self.fans.append(triangle_fan(np.concatenate(([(x,y,z+r)], self.circles[max(-len(self.circles),-2)].fan.vertices)), self._color()))

  def draw(self):
    for circle in self.circles:
      circle.draw()
    for strip in self.strips:
      strip.draw()
    for fan in self.fans:
      fan.draw()

  def get_triangles(self):
    triangles = []
    for fan in self.fans:
      triangles+=fan.get_triangles()
    for strip in self.strips:
      triangles+=strip.get_triangles()
    return triangles
  
  def handle_collision(self, collision:bool):
    if self.is_colliding != collision:
      self.is_colliding = collision
      self.color = [self.init_color, np.array([1,0,0]*len(self.vertices), dtype=np.float32)][int(collision)]
      for circle in self.circles:
        circle.handle_collision(collision)
      for strip in self.strips:
        strip.handle_collision(collision)
      for fan in self.fans:
        fan.handle_collision(collision)


  def export(self, file_path):
    with open(file_path, 'w') as f:
      json.dump({"triangles": self.get_triangles() }, f)