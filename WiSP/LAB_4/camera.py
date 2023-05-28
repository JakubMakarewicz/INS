import numpy as np

def get_orto_matrix(near, far):
	return np.array([
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, -2 / (far - near), - (far + near) / (far - near)],
      [0, 0, 0, 1],
   ], dtype=np.float32)
def get_perspective_matrix(near, far):
	 return np.array([
      [2*near/2, 0, 0, 0],
      [0, 2 * near / 2, 0, 0],
      [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
      [0, 0, -1, 0],
   ], dtype=np.float32)

def get_pos_rot_matrix(rotation_x = 0, rotation_z = 0, distance = 2):
   x = distance * np.sin(rotation_x) * np.cos(rotation_z)
   y = distance * np.sin(rotation_z)
   z = distance * np.cos(rotation_x) * np.cos(rotation_z)
   xyz = np.array([0, 0, 0], dtype=np.float32)
   target = np.array([x, y, z], dtype = np.float32)
   direction = xyz - target
   direction = direction / np.linalg.norm(direction)
   xyz = np.array([direction[0] * distance, direction[1] * distance, direction[2] * distance], dtype=np.float32)

   up = np.array([0, 1, 0], dtype = np.float32)
   right = np.cross(direction, up) * 1
   up = np.cross(right, direction) * 1
	 
   pos = np.array([
      [1, 0, 0, -xyz[0]],
      [0, 1, 0, -xyz[1]],
      [0, 0, 1, -xyz[2]],
      [0, 0, 0, 1]
      ], dtype=np.float32
   )

   rot = np.array([
      [right[0], right[1], right[2], 0],
      [up[0], up[1], up[2], 0],
      [direction[0], direction[1], direction[2], 0],
      [0, 0, 0, 1]
   ], dtype=np.float32)

   return np.matmul(rot, pos)

def get_camera(camera_type=0, distance = 3, rotation_x = 0, rotation_z = 0, near = 0, far = 0):
	cam_matrix = get_orto_matrix(near, far) if camera_type == 1 else get_perspective_matrix(near, far)
	return np.matmul(cam_matrix, get_pos_rot_matrix(rotation_x, rotation_z, distance)).transpose()