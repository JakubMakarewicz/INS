from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.line import line
from Lib.base import base
import random
class fig_base(base):
  line = None
	 
  def _color(self):
    return (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
  def __init__(self, vertices, color, line_vertices = [], draw_line=True, randomize_color = True):
    super().__init__(vertices, self._color() if randomize_color else color)
    if draw_line:
      self.line = line(line_vertices if line_vertices != [] else line.linify(self.vertices))

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