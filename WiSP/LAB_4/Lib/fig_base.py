from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.line import line
from Lib.base import base
import random
import numpy as np

class fig_base(base):
  line = None
  init_color = None
  is_colliding = False

  def _color(self):
    return (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
  
  def __init__(self, vertices, color, line_vertices = [], draw_line=True, randomize_color = True):
    super().__init__(vertices, self._color() if randomize_color else color)
    self.init_color = self.color
    if draw_line:
      self.line = line(line_vertices if line_vertices != [] else line.linify(self.vertices))

  def handle_collision(self, collision:bool):
    if self.is_colliding != collision:
      self.is_colliding = collision
      self.color = [self.init_color, np.array([1,0,0]*len(self.vertices), dtype=np.float32)][int(collision)]

  def check_collision(self, other: 'fig_base'):
    return True
  
  def draw(self):
    self.apply_color()
    self._draw()
    self.disable_color()
    # if self.line:
      # self.line.draw()

  def _draw(self):
    raise Exception("not implemented")
  
  def get_triangles(self):
    raise Exception("not implemented")