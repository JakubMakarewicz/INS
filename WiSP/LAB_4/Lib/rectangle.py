from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.fig_base import fig_base
from Lib.line import line
import json

class rectangle(fig_base):
   
  def __init__(self,a,b,c,d, color, draw_line=True):
    super().__init__([a,b,d,b,d,c], color, line.linify([a,b,c,d]), draw_line)

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
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 6)
    glDisableVertexAttribArray(0)

  def get_triangles(self):
    return [
      {
        "vertices": list(map(list, self.vertices[0:3])),
        "color": list(self.color[0:3])
      },
      {
        "vertices": list(map(list,self.vertices[3:])),
        "color": list(self.color[0:3])
      }
    ]
  
  def export(self, file_path):
    with open(file_path, 'w') as f:
      json.dump({ "triangles": self.get_triangles() }, f)