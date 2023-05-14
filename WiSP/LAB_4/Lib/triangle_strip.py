from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.fig_base import fig_base
from Lib.circle import circle

class triangle_strip(fig_base):
  
  def __init__(self, vertices, color, line_vertices = [], draw_line=True): 
    super().__init__(vertices, color, line_vertices, draw_line)

  @staticmethod
  def from_circles(lhs:circle, rhs:circle, color, draw_line=True):
    return triangle_strip(
      np.array([(_a,_b) for _a,_b in zip(lhs.fan.vertices, rhs.fan.vertices)]).reshape(2*len(lhs.fan.vertices), 3), 
      color, 
      draw_line=draw_line)

  def _draw(self):
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer)
    glVertexAttribPointer(
      0,        
      3,        
      GL_FLOAT, 
      GL_FALSE, 
      self.vertices.strides[0],        
      ctypes.c_void_p(0)  
    )
    glDrawArrays(GL_TRIANGLE_STRIP, 0, self.vertices.size)
    glDisableVertexAttribArray(0)