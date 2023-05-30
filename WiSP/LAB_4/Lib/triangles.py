import json

from Lib.triangle import triangle

class triangles:
	triangle_list = []

	def __init__(self, file_path):
		with open(file_path, "r") as f:
			data = json.load(f)
			for x in data["triangles"]:
				assert len(x["vertices"]) == 3
				self.triangle_list.append(triangle(*x["vertices"], x["color"]))
	
	def draw(self):
		for triangle in self.triangle_list:
			triangle.draw()
			