import OpenGL.GL as gl
import glfw
import sys
import numpy as np

from shader import *
import vectorOperations as vo
from Lib.cone import cone
from Lib.cylinder import cylinder
from Lib.pyramid import pyramid
from Lib.cube import cube
from Lib.sphere import sphere
from Lib.regular_fig import regular_fig

class WindowState:
    def __init__(self):
        self.currentRotationType = vo.Rotation.OX
        self.currentPosition = [0., 0., 0.]
        self.currentRotation = [0., 0., 0.]
        self.currentColor = [1., 1., 1.]
        self.circleQuality = 20
        self.rotationQuality = 100

class Window_glfw:
   
   def __init__(self, width = 720, height = 720, title = "GLFW Window", monitor = None, share = None) -> None:
      self.window = None
      self.width = width
      self.height = height
      self.title = title
      self.monitor = monitor
      self.share = share
      self.framebuffer_size = None
      self.vao = 0
      self.vertexBuffer = 0
      self.vertexShaderId = 0
      self.fragmentShaderId = 0
      self.vertexes = []
      self.glProgramId = None
      self.state = WindowState()

   def setup_window(self) -> None:
      if not glfw.init():
         exit(-1)
      self.window = glfw.create_window(self.width, self.height, self.title, self.monitor, self.share)

      if not self.window:
         glfw.terminate()
         exit(-2)

      glfw.make_context_current(self.window)
      glfw.set_key_callback(self.window, self._key_callback)

      glfw.window_hint(glfw.SAMPLES, 8)
      glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
      glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
      gl.glEnable(gl.GL_DEPTH_TEST)
      gl.glDepthFunc(gl.GL_LESS)
      glfw.swap_interval(2)

   def _prepareShaders(self, vertexShaderCode, fragmentShaderCode):
      self.vertexShaderId = gl.glCreateShader(gl.GL_VERTEX_SHADER)
      self.fragmentShaderId = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
      gl.glShaderSource(self.vertexShaderId, vertexShaderCode)
      gl.glShaderSource(self.fragmentShaderId, fragmentShaderCode)
      gl.glCompileShader(self.vertexShaderId)
      if not gl.glGetShaderiv(self.vertexShaderId, gl.GL_COMPILE_STATUS):
         print(str(gl.glGetShaderInfoLog(self.vertexShaderId).decode()), file=sys.stderr)
      gl.glCompileShader(self.fragmentShaderId)
      if not gl.glGetShaderiv(self.fragmentShaderId, gl.GL_COMPILE_STATUS):
         print(str(gl.glGetShaderInfoLog(self.fragmentShaderId).decode()), file=sys.stderr)

      self.glProgramId = gl.glCreateProgram()
      gl.glAttachShader(self.glProgramId, self.vertexShaderId)
      gl.glAttachShader(self.glProgramId, self.fragmentShaderId)
      gl.glLinkProgram(self.glProgramId)
      if not gl.glGetProgramiv(self.glProgramId, gl.GL_LINK_STATUS):
         print("p:" + str(gl.glGetProgramInfoLog(self.glProgramId)), file=sys.stderr)
      
      gl.glDetachShader(self.glProgramId, self.vertexShaderId)
      gl.glDetachShader(self.glProgramId, self.fragmentShaderId)

      gl.glDeleteShader(self.vertexShaderId)
      gl.glDeleteShader(self.fragmentShaderId)
      
      gl.glUseProgram(self.glProgramId)
      self.matrixLocationId = gl.glGetUniformLocation(self.glProgramId, "position")
      self.rotationLocationId = gl.glGetUniformLocation(self.glProgramId, "rotation")

   def _setup_draw(self):
      self.vao = gl.glGenVertexArrays(1)
      gl.glBindVertexArray(self.vao)

   def _key_callback(self, window, key: int, scancode: int, action: int, mods: int):
      if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(self.window, glfw.TRUE)
      elif key == glfw.KEY_A:
         self.state.currentPosition = [self.state.currentPosition[0] - 0.1, self.state.currentPosition[1], self.state.currentPosition[2]]
      elif key == glfw.KEY_D:
         self.state.currentPosition = [self.state.currentPosition[0] + 0.1, self.state.currentPosition[1], self.state.currentPosition[2]]
      elif key == glfw.KEY_S:
         self.state.currentPosition = [self.state.currentPosition[0], self.state.currentPosition[1] - 0.1, self.state.currentPosition[2]]
      elif key == glfw.KEY_W:
         self.state.currentPosition = [self.state.currentPosition[0], self.state.currentPosition[1] + 0.1, self.state.currentPosition[2]]
      elif key == glfw.KEY_Q:
         self.state.currentPosition = [self.state.currentPosition[0], self.state.currentPosition[1], self.state.currentPosition[2] - 0.1]
      elif key == glfw.KEY_E:
         self.state.currentPosition = [self.state.currentPosition[0], self.state.currentPosition[1], self.state.currentPosition[2] + 0.1]

      elif key == glfw.KEY_K:
         self.state.currentRotation = [self.state.currentRotation[0] - np.pi/self.state.rotationQuality, self.state.currentRotation[1], self.state.currentRotation[2]]
      elif key == glfw.KEY_I:
         self.state.currentRotation = [self.state.currentRotation[0] + np.pi/self.state.rotationQuality, self.state.currentRotation[1], self.state.currentRotation[2]]
      elif key == glfw.KEY_L:
         self.state.currentRotation = [self.state.currentRotation[0], self.state.currentRotation[1] - np.pi/self.state.rotationQuality, self.state.currentRotation[2]]
      elif key == glfw.KEY_J:
         self.state.currentRotation = [self.state.currentRotation[0], self.state.currentRotation[1] + np.pi/self.state.rotationQuality, self.state.currentRotation[2]]
      elif key == glfw.KEY_U:
         self.state.currentRotation = [self.state.currentRotation[0], self.state.currentRotation[1], self.state.currentRotation[2] - np.pi/self.state.rotationQuality]
      elif key == glfw.KEY_O:
         self.state.currentRotation = [self.state.currentRotation[0], self.state.currentRotation[1], self.state.currentRotation[2] + np.pi/self.state.rotationQuality]

      elif key == glfw.KEY_KP_SUBTRACT:
         self.vert_approx = max(0, self.vert_approx-1)
         self.hor_approx = max(3, self.hor_approx-1)
         self.figs[4]= sphere(0,0,0,1,self.vert_approx, self.hor_approx, (0,0,1))
         self.figs[5] = regular_fig(1,self.hor_approx,(0,0,1))
      elif key == glfw.KEY_KP_ADD:
         self.vert_approx = min(100, self.vert_approx+1)
         self.hor_approx = min(100, self.hor_approx+1)
         self.figs[4] = sphere(0,0,0,1,self.vert_approx, self.hor_approx, (0,0,1))
         self.figs[5] = regular_fig(1,self.hor_approx,(0,0,1))

      elif key in [glfw.KEY_0, glfw.KEY_1, glfw.KEY_2, glfw.KEY_3, glfw.KEY_4, glfw.KEY_5] :
         n = 0 if key == glfw.KEY_0 else 1 if key == glfw.KEY_1 else 2 if key == glfw.KEY_2 else 3 if key == glfw.KEY_3 else 4 if key==glfw.KEY_4 else 5
         self.fig = self.figs[n]

   def run_main_loop(self):
      self._setup_draw()
      self.n=0
      self.hor_approx = 3
      self.vert_approx = 0
      self.figs = [cube(-.4,-.4,0,1,1,1, (0,0,1)), 
                   cone(-.4,-.4,0,1,1, (0,0,1)), 
                   cylinder(-.4,-.4,0,1,1, (0,0,1)),
                   pyramid(-.4,-.4,0,0.2,0.2, (0,0,1)),
                   sphere(0,0,0,1,self.vert_approx,self.hor_approx,(0,0,1)),
                   regular_fig(1,self.hor_approx,(0,0,1))]
      self.fig = self.figs[self.n]
      # fig = cube(-.4,-.4,0,1,1,1, (0,0,1)) # fix lines
      # fig = cone(-.4,-.4,0,1,1, (0,0,1)) # this one works
      # fig = cylinder(-.4,-.4,0,1,1, (0,0,1)) # this doesnt draw the top line
      # fig = pyramid(-.4,-.4,0,0.2,0.2, (0,0,1)) # hmmmm
      # fig = sphere(0,0,0,1,2,40,(0,0,1)) # for some reason only the first line gets drawn
      # fig = regular_fig(1,6,(0,0,1)) 

      self._prepareShaders(vsc, fsc)

      while not glfw.window_should_close(self.window):       
         self.framebuffer_size = glfw.get_framebuffer_size(self.window)
         gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

         # draw
         gl.glUseProgram(self.glProgramId)
         gl.glUniformMatrix4fv(self.matrixLocationId, 1, gl.GL_FALSE, vo.createPositionMatrix(self.state.currentPosition))
         gl.glUniform3f(self.rotationLocationId, *self.state.currentRotation)
 
         self.fig.draw()
         # end draw

         glfw.swap_buffers(self.window)
         glfw.poll_events()

      glfw.terminate()
      exit(0)

window = Window_glfw()
window.setup_window()
window.run_main_loop()