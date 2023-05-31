from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import random 
from Lib.circle import circle
from Lib.triangle_strip import triangle_strip
from Lib.triangle_fan import triangle_fan

class sphere:
  circles, strips, fans = list(), list(), list()

  def _color(self):
    return (random.randint(0,1),random.randint(0,1),random.randint(0,1))

  def __init__(self,x,y,z,r,approximation_vertical, approximation_horizontal, color,posx, posy, posz):
    self.circles.clear()
    self.strips.clear()
    self.fans.clear()
    self.circles.append(circle(x,y,z,r,self._color(),approximation_horizontal))
    self.poz = [posx, posy, posz]
    for i in range(1,approximation_vertical+1):
      hn = i*r/(approximation_vertical+1)
      rn = np.sqrt(np.power(r,2) - np.power(hn,2))
      self.circles.append(circle(x,y,z+hn,rn,self._color(),approximation_horizontal))
      self.circles.append(circle(x,y,z-hn,rn,self._color(),approximation_horizontal))
      self.strips.append(triangle_strip.from_circles(self.circles[-3], self.circles[-1], self._color()))
      self.strips.append(triangle_strip.from_circles(self.circles[max(-len(self.circles),-4)], self.circles[-2], self._color()))

    self.fans.append(triangle_fan(np.concatenate(([(x,y,z-r)], self.circles[-1].fan.vertices)), self._color()))
    self.fans.append(triangle_fan(np.concatenate(([(x,y,z+r)], self.circles[max(-len(self.circles),-2)].fan.vertices)), self._color()))

  def draw(self):
    for circle in self.circles:
      circle.draw()
    for strip in self.strips:
      strip.draw()
    for fan in self.fans:
      fan.draw()