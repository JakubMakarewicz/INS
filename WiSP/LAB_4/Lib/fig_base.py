from OpenGL.GLUT import *
from OpenGL.GL import *
from Lib.line import line
from Lib.base import base
import random
import numpy as np

class fig_base(base):
  line = None
  init_color = None
  is_colliding = False

  def _color(self):
    return (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
  
  def __init__(self, vertices, color, line_vertices = [], draw_line=True, randomize_color = True):
    super().__init__(vertices, self._color() if randomize_color else color)
    self.init_color = self.color
    if draw_line:
      self.line = line(line_vertices if line_vertices != [] else line.linify(self.vertices))

  def handle_collision(self, collision:bool):
    if self.is_colliding != collision:
      self.is_colliding = collision
      self.color = [self.init_color, np.array([1,0,0]*len(self.vertices), dtype=np.float32)][int(collision)]
      self.setup()
  
  def draw(self):
    self.apply_color()
    self._draw()
    self.disable_color()
    # if self.line:
      # self.line.draw()

  def _draw(self):
    raise Exception("not implemented")
  
  def get_triangles(self):
    raise Exception("not implemented")
  
  def get_pos(self):
    return np.array(
        [
          np.array(vertex, dtype=np.float32)
          for vertex in self.poz
        ], 
        dtype=np.float32)

  def check_collision(self, otherFigure: 'fig_base'):
    triangles = [
      np.array(
        [
          np.array(vertex, dtype=np.float32) + self.get_pos()
          for vertex in triangle["vertices"]
        ], 
        dtype=np.float32) 
      for triangle in self.get_triangles()]
    
    other_triangles = [
      np.array(
        [
          np.array(vertex, dtype=np.float32) + otherFigure.get_pos()
          for vertex in triangle["vertices"]
        ], 
        dtype=np.float32) 
      for triangle in otherFigure.get_triangles()]
    
    epsilon = 0.05

    for otherTriangle in other_triangles:
        for triangle in triangles:
          n2 = self.__n_param(otherTriangle)
          d2 = self.__d_param(n2, otherTriangle)

          if self.__check_plane_overlap(d2, n2, triangle) is False:
              continue

          n1 = self.__n_param(triangle)
          d1 = self.__d_param(n1, triangle)
          if self.__check_plane_overlap(d1, n1, otherTriangle) is False:
              continue
          
          dv10 = np.dot(n2, triangle[0]) + d2
          dv11 = np.dot(n2, triangle[1]) + d2
          dv12 = np.dot(n2, triangle[2]) + d2

          dv20 = np.dot(n1, otherTriangle[0]) + d1
          dv21 = np.dot(n1, otherTriangle[1]) + d1
          dv22 = np.dot(n1, otherTriangle[2]) + d1

          if dv10 < epsilon:
            dv10 = 0
          if dv11 < epsilon:
            dv11 = 0
          if dv12 < epsilon:
            dv12 = 0
          if dv20 < epsilon:
            dv20 = 0
          if dv21 < epsilon:
            dv21 = 0
          if dv22 < epsilon:
            dv22 = 0
        
          if dv10 == dv11 == dv12 == 0:
            if self.__2d_collisionCheck(triangle, otherTriangle):
              return True
            continue

          D = np.cross(n1, n2)
          p10 = self.__get_p_param(triangle[0], D)
          p11 = self.__get_p_param(triangle[1], D)
          p12 = self.__get_p_param(triangle[2], D)
          p20 = self.__get_p_param(otherTriangle[0], D)
          p21 = self.__get_p_param(otherTriangle[1], D)
          p22 = self.__get_p_param(otherTriangle[2], D)

          t11 = p10 + (p11 - p10) * dv10 / (dv10 - dv11)
          t12 = p11 + (p12 - p11) * dv11 / (dv11 - dv12)

          t21 = p20 + (p21 - p20) * dv20 / (dv20 - dv21)
          t22 = p21 + (p22 - p21) * dv21 / (dv21 - dv22)
          if t11 < t21 < t12 or t11 < t22 < t12 or t21 < t11 < t22 or t21 < t12 < t22 \
              or t11 > t21 > t12 or t11 > t22 > t12 or t21 > t11 > t22 or t21 > t12 > t22:
              return True
    return False

  def __get_p_param(self, vertex, D):
    absD = np.absolute(D)
    if np.absolute(D[0]) == np.max(absD):
        return vertex[0]
    elif np.absolute(D[1]) == np.max(absD):
        return vertex[1]
    elif np.absolute(D[2]) == np.max(absD):
        return vertex[2]
    return 0

  def __check_segments_overlap(self, p1, p2, q1, q2):
    min1 = [np.minimum(p1[0], p2[0]), np.minimum(p1[1], p2[1]), np.minimum(p1[2], p2[2])]
    max1 = [np.maximum(p1[0], p2[0]), np.maximum(p1[1], p2[1]), np.maximum(p1[2], p2[2])]
    min2 = [np.minimum(q1[0], q2[0]), np.minimum(q1[1], q2[1]), np.minimum(q1[2], q2[2])]
    max2 = [np.maximum(q1[0], q2[0]), np.maximum(q1[1], q2[1]), np.maximum(q1[2], q2[2])]
    
    minIntersection = [np.maximum(min1[0], min2[0]), np.maximum(min1[1], min2[1]), np.maximum(min1[2], min2[2])]
    maxIntersection = [np.minimum(max1[0], max2[0]), np.minimum(max1[1], max2[1]), np.minimum(max1[2], max2[2])]

    return minIntersection[0] < maxIntersection[0] and minIntersection[1] < maxIntersection[1] and minIntersection[2] < maxIntersection[2]

  def __2d_collisionCheck(self, triangle, otherTriangle):
    for point in otherTriangle:
        if self.__sameSide(point, triangle[0], triangle[1], triangle[2]) \
          and self.__sameSide(point, triangle[1], triangle[0], triangle[2]) \
          and self.__sameSide(point, triangle[2], triangle[0], triangle[1]):
          return True
    return False

  def __sameSide(self, p1, p2, a, b):
    cp1 = np.cross(b - a, p1 - a)
    cp2 = np.cross(b - a, p2 - a)
    if np.dot(cp1, cp2) >= 0:
        return True
    return False

  def __n_param(self, triangle: 'list[list[float]]'):
    return np.cross(triangle[1] - triangle[0], triangle[2] - triangle[0])

  def __d_param(self, n, triangle: 'list[list[float]]'):
    return np.dot(-n, triangle[0])
  
  def __check_plane_overlap(self, d, n, triangle):
    distance1 = np.matmul(n, triangle[0]) + d
    distance2 = np.matmul(n, triangle[1]) + d
    distance3 = np.matmul(n, triangle[2]) + d
    if (distance1 != 0 or distance2 != 0 or distance3 != 0) and np.sign(distance1) == np.sign(distance2) == np.sign(distance3):
        return False
    return True