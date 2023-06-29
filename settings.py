from numba import njit
import numpy as np
import glm
import math

# resolution
WIN_RES = glm.vec2(1600, 900)

# chunk
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE ** 2
CHUNK_VOL = CHUNK_SIZE **3

# world
WORLD_W, WORLD_H = 10, 3
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_H

# world center
CENTER_XZ = (WORLD_W // 2) * CHUNK_SIZE
CENTER_Y = (WORLD_H // 2) * CHUNK_SIZE

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 60
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2.0 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 1000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.05
PLAYER_ROT_SPEED = 0.005
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CENTER_Y, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

# colors
BG_COLOR = glm.vec3(0.10, 0.16, 0.25)
