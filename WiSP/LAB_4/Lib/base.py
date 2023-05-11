
from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

class base:
  vertices = []
  vertex_buffer = None
  color_buffer = None
  color = None
  
  def __init__(self, vertices, color):
    self.vertices = np.array(vertices, dtype=np.float32)
    self.color = np.array([*color]*len(vertices), dtype=np.float32)
    self.setup()

  def setup(self):
    self.vertex_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer)
    glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices,GL_DYNAMIC_DRAW)
    self.color_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, self.color_buffer)
    glBufferData(GL_ARRAY_BUFFER, self.color.nbytes, self.color, GL_DYNAMIC_DRAW)

  def draw(self):
    self.apply_color()
    self._draw()
    self.disable_color()

  def apply_color(self):
    glEnableVertexAttribArray(1)
    glBindBuffer(GL_ARRAY_BUFFER, self.color_buffer)
    glVertexAttribPointer(
      1,        
      3,        
      GL_FLOAT, 
      GL_FALSE, 
      0,        
      ctypes.c_void_p(0)  
    )
		
  def disable_color(self): 
    glDisableVertexAttribArray(1)

  def _draw(self):
    raise Exception("not implemented")