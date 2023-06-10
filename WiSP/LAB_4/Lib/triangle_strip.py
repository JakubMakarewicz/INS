from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import json
from Lib.fig_base import fig_base
from Lib.circle import circle
import Lib.base as base

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

  def get_triangles(self):
    ret_list = []
    for i in range(0, len(self.vertices)-2):
      ret_list.append({
        "vertices": list(map(base.map_vertex, [self.vertices[i],self.vertices[i+1], self.vertices[i+2]])),
        "color": list(map(float, self.color[0:3]))
      })
    return ret_list

  def export(self, file_path):
    with open(file_path, 'w') as f:
      json.dump(self.get_triangles(), f)