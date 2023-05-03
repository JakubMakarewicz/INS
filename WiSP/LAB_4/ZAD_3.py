import pygame as pg
import sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from Lib.cylinder import cylinder
from Lib.cube import cube
from Lib.cone import cone
from Lib.pyramid import pyramid

def running_loop(clock):
  running = True
  rotate = True
  obj = 'cube'
  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        sys.exit(0)
      elif event.type == pg.KEYDOWN:
        if event.unicode == 'r':
          rotate = not rotate
        elif event.unicode == 'c':
          obj = 'cube'
        elif event.unicode == 'l':
          obj = 'cylinder'
        elif event.unicode == 'p':
          obj = 'pyramid'
        elif event.unicode == 'o':
          obj = 'cone'
        
    if rotate:
      glRotatef(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    if obj == 'cube':
      cube(0,0,-1, 1,1, 1).draw((1,1,0))
    elif obj == 'cylinder':
      cylinder(0,0,-1,1,1).draw((1,1,0)) 
    elif obj == 'pyramid':
      pyramid(0,0,-1,1,1).draw((1,1,0))
    elif obj == 'cone':
      cone(0,0,-1,1,1).draw((1,1,0))
    
    pg.display.flip()
    clock.tick(20)

display = (1920,1080)
pg.init()
pg.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glEnable(GL_DEPTH_TEST)
glTranslatef(0.0, 0.0, -5)

running_loop(pg.time.Clock())