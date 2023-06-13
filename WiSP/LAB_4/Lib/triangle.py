from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.fig_base import fig_base
import numpy as np

class triangle(fig_base):
  
  def __init__(self,a,b,c, color, draw_line=True):      
    super().__init__([a,b,c], color, [], draw_line)

  def move(self, vec):
    super().move(vec)
     
    self.vertices = np.array([
      np.dot(self.get_rotation(), np.array(vertex, dtype=np.float32))[0]
        + self.get_pos()
      for vertex in self.vertices
    ])
    self.setup()
  
  def rotate(self, vec):
    super().rotate(vec)
     
    self.vertices = np.array([
      np.dot(self.get_rotation(), np.array(vertex, dtype=np.float32))[0]
        + self.get_pos()
      for vertex in self.vertices
    ])
    self.setup()

  def get_triangles(self):
    return [
      {
        "vertices": list(map(list, self.vertices)),
        "color": list(self.color[0:3])
      }
      ]
  
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
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 3)
    glDisableVertexAttribArray(0)