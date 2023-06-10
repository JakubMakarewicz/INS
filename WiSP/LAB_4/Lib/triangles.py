import json

from Lib.triangle import triangle
from Lib.base import base
from Lib.fig_base import fig_base

class triangles(fig_base):
  triangle_list = []

  def __init__(self, file_path, posx, posy, posz):
    self.poz = [posx,posy,posz]
    with open(file_path, "r") as f:
      data = json.load(f)
      for x in data["triangles"]:
        assert len(x["vertices"]) == 3
        self.triangle_list.append(triangle(*x["vertices"], x["color"]))
  
  def draw(self):
    for triangle in self.triangle_list:
      triangle.draw()
  
  def get_triangles(self):
    triangles = []
    for triangle in self.triangle_list():
      triangles.append({
        "vertices": list(map(base.map_vertex, triangle.vertices)),
        "color": list(map(float, triangle.color))
      })
    return {
      "triangles": triangles
    }

  def export(self, file_path):
    with open(file_path, 'w') as f:
      json.dump(self.get_triangles(), f)