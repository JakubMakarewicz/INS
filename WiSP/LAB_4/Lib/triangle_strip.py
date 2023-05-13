from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.fig_base import fig_base

class triangle_strip(fig_base):
  
  def __init__(self, vertices, color, line_vertices = [], draw_line=True): 
    super().__init__(vertices, color, line_vertices, draw_line)

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
    glDrawArrays(GL_TRIANGLE_STRIP, 0, self.vertices.size)
    glDisableVertexAttribArray(0)