from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.fig_base import fig_base

class triangle(fig_base):
  
  def __init__(self,a,b,c, color, draw_line=True):      
    super().__init__([a,b,c], color, self.vertices, draw_line)

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