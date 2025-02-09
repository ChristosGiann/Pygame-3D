import math

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 2 * SCREEN_HEIGHT
MAP_SIZE = 19
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV = 60 * math.pi / 180 
HALF_FOV = FOV / 2
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE) * 2
SCALE = SCREEN_WIDTH / CASTED_RAYS
SPEED = 1
