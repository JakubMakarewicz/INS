from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

from Lib.rectangle import rectangle
from Lib.circle import circle

class cylinder:
	x,y,z,r,h,approximation=0,0,0,0,0,0
	walls = []

	def __init__(self,x,y,z,r,h, approximation=40):			
		self.x=x
		self.y=y
		self.z=z
		self.r=r
		self.h=h
		self.approximation=approximation
		
		angleIncrement = 360. / approximation
		angleIncrement *= np.pi / 180.

		angle = 0.

		for _ in range(approximation):
			self.walls.append((
				((x+r) * np.cos(angle), (y+r) * np.sin(angle), z+0),
				((x+r) * np.cos(angle), (y+r) * np.sin(angle), z+h),
				((x+r) * np.cos(angle+angleIncrement), (y+r) * np.sin(angle+angleIncrement), z+h),
				((x+r) * np.cos(angle+angleIncrement), (y+r) * np.sin(angle+angleIncrement), z+0)))
			angle+=angleIncrement

	def draw(self, color):
		circle(self.x,self.y,self.z,self.r,self.approximation).draw(color)
		circle(self.x,self.y,self.z+self.h,self.r,self.approximation).draw(color)
		for wall in self.walls:
			rectangle(*wall).draw(color)