import OpenGL.GL as gl
import glfw
import sys
import time
import numpy as np

from shader import *
import vectorOperations as vo
from Lib.cone import cone
from Lib.cylinder import cylinder
from Lib.pyramid import pyramid
from Lib.cube import cube
from Lib.sphere import sphere
from Lib.regular_fig import regular_fig
from Lib.triangles import triangles
from camera import *

class WindowState:
    def __init__(self):
        self.rotationType = vo.Rotation.OX
        self.distance = 2.
        self.near = 1.
        self.far = 10.
        self.rotation = [0., 0.]
        self.currentColor = [1., 1., 1.]
        self.circleQuality = 20
        self.rotationQuality = 100
        self.camera = 0

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

      self.figs = []
      self.currently_selected=-1
      
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
         print('vertex shader: ', str(gl.glGetShaderInfoLog(self.vertexShaderId).decode()), file=sys.stderr)
      gl.glCompileShader(self.fragmentShaderId)
      if not gl.glGetShaderiv(self.fragmentShaderId, gl.GL_COMPILE_STATUS):
         print('fragment shader: ',str(gl.glGetShaderInfoLog(self.fragmentShaderId).decode()), file=sys.stderr)

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
      self.cameraLocationId = gl.glGetUniformLocation(self.glProgramId, "camera")
      
      # self.vertexShaderId = gl.glCreateShader(gl.GL_VERTEX_SHADER)
      # self.fragmentShaderId = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
      # gl.glShaderSource(self.vertexShaderId, vertexShaderCode)
      # gl.glShaderSource(self.fragmentShaderId, fragmentShaderCode)
      # gl.glCompileShader(self.vertexShaderId)
      # if not gl.glGetShaderiv(self.vertexShaderId, gl.GL_COMPILE_STATUS):
      #    print(str(gl.glGetShaderInfoLog(self.vertexShaderId).decode()), file=sys.stderr)
      # gl.glCompileShader(self.fragmentShaderId)
      # if not gl.glGetShaderiv(self.fragmentShaderId, gl.GL_COMPILE_STATUS):
      #    print(str(gl.glGetShaderInfoLog(self.fragmentShaderId).decode()), file=sys.stderr)

      # self.glProgramId = gl.glCreateProgram()
      # gl.glAttachShader(self.glProgramId, self.vertexShaderId)
      # gl.glAttachShader(self.glProgramId, self.fragmentShaderId)
      # gl.glLinkProgram(self.glProgramId)
      # if not gl.glGetProgramiv(self.glProgramId, gl.GL_LINK_STATUS):
      #    print("p:" + str(gl.glGetProgramInfoLog(self.glProgramId)), file=sys.stderr)
      
      # gl.glDetachShader(self.glProgramId, self.vertexShaderId)
      # gl.glDetachShader(self.glProgramId, self.fragmentShaderId)

      # gl.glDeleteShader(self.vertexShaderId)
      # gl.glDeleteShader(self.fragmentShaderId)
      
      # gl.glUseProgram(self.glProgramId)
      # self.matrixLocationId = gl.glGetUniformLocation(self.glProgramId, "position")
      # self.rotationLocationId = gl.glGetUniformLocation(self.glProgramId, "rotation")
      # self.cameraLocationId = gl.glGetUniformLocation(self.glProgramId, "camera")

   def _setup_draw(self):
      self.vao = gl.glGenVertexArrays(1)
      gl.glBindVertexArray(self.vao)

   def _key_callback(self, window, key: int, scancode: int, action: int, mods: int):
      if (action == glfw.PRESS) | (action == glfw.REPEAT):
         if self.currently_selected == -1:
            # camera rotation
            if key == glfw.KEY_L:
               self.state.rotation = [self.state.rotation[0] - np.pi/self.state.rotationQuality, self.state.rotation[1]]
            elif key == glfw.KEY_J:
               self.state.rotation = [self.state.rotation[0] + np.pi/self.state.rotationQuality, self.state.rotation[1]]
            elif key == glfw.KEY_I:
               self.state.rotation = [self.state.rotation[0], self.state.rotation[1] - np.pi/self.state.rotationQuality]
            elif key == glfw.KEY_K:
               self.state.rotation = [self.state.rotation[0], self.state.rotation[1] + np.pi/self.state.rotationQuality]
            # camera movement
            elif key == glfw.KEY_Q:
               self.state.near = self.state.near - 0.1
               print("near=",self.state.near)
            elif key == glfw.KEY_A:
               self.state.near = self.state.near + 0.1
               print("near=", self.state.near)
            elif key == glfw.KEY_W:
               self.state.distance = self.state.distance - 0.1
               print("distance=", self.state.distance)
            elif key == glfw.KEY_S:
               self.state.distance = self.state.distance + 0.1
               print("distance=", self.state.distance)
            elif key == glfw.KEY_E:
               self.state.far = self.state.far - 0.1
               print("far=", self.state.far)
            elif key == glfw.KEY_D:
               self.state.far = self.state.far + 0.1
               print("far=", self.state.far)
         else:
            # fig movement
            pass
         if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(self.window, glfw.TRUE)

         if key == glfw.KEY_V:

            self.load_fig("test.json",1)        # cube

         if key == glfw.KEY_2:

            self.load_fig("test.json",2)        # stozek

         if key == glfw.KEY_3:

            self.load_fig("test.json",3)        # kula


         if key == glfw.KEY_4:

            self.load_fig("test.json",4)

         if key == glfw.KEY_5:

            self.load_fig("test.json",5)

         if key == glfw.KEY_6:

            self.load_fig("test.json",6)

         elif key == glfw.KEY_B:
            self.delete_fig(len(self.figs)-1)

         elif key in [glfw.KEY_0, glfw.KEY_1] :
            self.state.camera = int(key != glfw.KEY_0)
            self.distance = 2.
            self.near = 1.
            self.far = 10.

   def load_fig(self,filename,fignum):
      #self.figs.append(triangles(filename))
      if fignum==1:
         self.figs.append(cube(0.4, 0.4, 0.4, 1, 1, 1, (1, 0, 1), 3+ (len(self.figs) - 1) * 3, 0, 0))
      elif fignum==2:
         self.figs.append(cone(-.4,-.4,0,1,1, (0,0,1),40, 3+(len(self.figs) - 1) * 3, 0, 0))
      elif fignum == 3:
         self.figs.append(sphere(0, 0, 0, 1, 2, 40, (0, 0, 1),3+(len(self.figs) - 1) * 3, 1, 0))
      elif fignum == 4:
         self.figs.append(cylinder(-.4, -.4, 0, 1, 1, (0, 0, 1),40,3+(len(self.figs) - 1) * 3, 1, 0))
      elif fignum == 5:
         self.figs.append(pyramid(-.4,-.4,0,1,1, (0,0,1),3+(len(self.figs) - 1) * 3, 0, 0))
      elif fignum == 6:
         self.figs.append(triangles(filename))

   def delete_fig(self,idx):
      if idx >= 0 and idx < len(self.figs):
         del self.figs[idx]

   def run_main_loop(self):
      self._setup_draw()
      self.n=0
      self.hor_approx = 3
      self.vert_approx = 0

      self._prepareShaders(vsc, fsc)

      while not glfw.window_should_close(self.window):
         self.framebuffer_size = glfw.get_framebuffer_size(self.window)
         gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
         # draw
         gl.glUseProgram(self.glProgramId)
         gl.glUniformMatrix4fv(
            self.cameraLocationId,
            1,
            gl.GL_FALSE,
            get_camera(self.state.camera,self.state.distance, *self.state.rotation, self.state.near, self.state.far)
            )
            

         for fig in self.figs:
            gl.glUniform3f(self.matrixLocationId, *fig.poz)
            gl.glUniform3f(self.rotationLocationId, *[0.,0.,0.])
            # gl.glUniform3f(self.matrixLocationId, *[0.,0.,0.])
            # gl.glUniform3f(self.matrixLocationId, *[0.,0.,0.])
            fig.draw()
         # end draw

         glfw.swap_buffers(self.window)
         glfw.poll_events()

      glfw.terminate()
      exit(0)

window = Window_glfw()
window.setup_window()
window.run_main_loop()
