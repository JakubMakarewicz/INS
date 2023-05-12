from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.base import base

class triangle_fan(base):
  
  def __init__(self, vertices, color): 
    super().__init__(vertices, color)

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