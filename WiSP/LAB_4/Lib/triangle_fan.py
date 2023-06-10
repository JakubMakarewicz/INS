from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.fig_base import fig_base
import Lib.base as base
import json

class triangle_fan(fig_base):
  
  def __init__(self, vertices, color, line_vertices = [], draw_line=True): 
    super().__init__(vertices, color, line_vertices, draw_line)
    
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
    glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertices.size)
    glDisableVertexAttribArray(0)

  def get_triangles(self):
    ret_list = []
    for i in range(2, len(self.vertices)):
      ret_list.append({
        "vertices": list(map(base.map_vertex, [self.vertices[0],self.vertices[i-1], self.vertices[i]])),
        "color": list(map(float, self.color[0:3]))
      })
    return ret_list

  def export(self, file_path):
    with open(file_path, 'w') as f:
      json.dump(self.get_triangles(), f)

