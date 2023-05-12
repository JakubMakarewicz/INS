from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.base import base
import numpy as np

class line(base):

  def __init__(self, vertices, color=(1,1,1)):      
    super().__init__(vertices, color)

  def _draw(self):
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer)
    glVertexAttribPointer(
      0,        
      2,        
      GL_FLOAT, 
      GL_FALSE, 
      self.vertices.strides[0],        
      ctypes.c_void_p(0)  
    )
    glDrawArrays(GL_LINES, 0, len(self.vertices))
    glDisableVertexAttribArray(0)

  @staticmethod
  def linify(arr) -> list:
    return np.concatenate((np.repeat(arr,2,axis=0)[1:], [arr[0]]))
