from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.line import line
from Lib.base import base

class fig_base(base):
  line = None
	 
  def __init__(self, vertices, color, line_vertices = [], draw_line=True):
    super().__init__(vertices, color)
    if draw_line:
        print("heyo")
        print(vertices)
        self.line = line(line_vertices if line_vertices != [] else line.linify(self.vertices))

  def draw(self):
    self.apply_color()
    self._draw()
    self.disable_color()
    if self.line:
      self.line.draw()

  def _draw(self):
    raise Exception("not implemented")