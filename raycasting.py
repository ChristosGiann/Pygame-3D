import pygame
import math
from settings import *
from map import MAP

#Textures
wall_texture = None
floor_texture = None
gate_texture = None

def load_textures():
    """Φορτώνει όλες τις υφές."""
    global wall_texture, floor_texture, gate_texture
    try:
        wall_texture = pygame.image.load('wall_texture.png').convert() 
        floor_texture = pygame.image.load('floor_texture.png').convert()
        gate_texture = pygame.image.load('blue_gate_texture.jpg').convert() 
    except pygame.error as e:
        print("Αποτυχία φόρτωσης υφής:", e)


def render_sky(win):
    """Σχεδιάζει τον ουρανό με βαθύ μπλε χρώμα."""
    sky_color = (48, 25, 52)
    pygame.draw.rect(win, sky_color, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2)) 

def cast_rays(win, player):
    """Αποδίδει τοίχους και πύλες με raycasting."""
    start_angle = player.angle - HALF_FOV  
    for rays in range(CASTED_RAYS): 
        for depth in range(1, MAX_DEPTH):  
            ray_dir_x = -math.sin(start_angle)
            ray_dir_y = math.cos(start_angle) 

            target_x = player.x + ray_dir_x * depth  
            target_y = player.y + ray_dir_y * depth  

            row = int(target_y / TILE_SIZE)  
            column = int(target_x / TILE_SIZE)  
            square = row * MAP_SIZE + column 

            if MAP[square] == '#':  # Έλεγχος για τοίχο
                depth_corrected = depth * math.cos(player.angle - start_angle)  
                wall_height = TILE_SIZE / (depth_corrected + 0.0001) * SCREEN_HEIGHT 

                offset = target_x % TILE_SIZE if abs(ray_dir_x) > abs(ray_dir_y) else target_y % TILE_SIZE
                tex_x = int((offset / TILE_SIZE) * wall_texture.get_width())  

                texture_column = wall_texture.subsurface((tex_x, 0, 1, wall_texture.get_height()))
                texture_column = pygame.transform.scale(texture_column, (SCALE, int(wall_height)))  

                win.blit(texture_column, (rays * SCALE, SCREEN_HEIGHT // 2 - wall_height // 2))  
                break
            elif MAP[square] == 'G':  
                depth_corrected = depth * math.cos(player.angle - start_angle) 
                wall_height = TILE_SIZE / (depth_corrected + 0.0001) * SCREEN_HEIGHT  

                offset = target_x % TILE_SIZE if abs(ray_dir_x) > abs(ray_dir_y) else target_y % TILE_SIZE
                tex_x = int((offset / TILE_SIZE) * gate_texture.get_width()) 

                texture_column = gate_texture.subsurface((tex_x, 0, 1, gate_texture.get_height()))
                texture_column = pygame.transform.scale(texture_column, (SCALE, int(wall_height)))  

                win.blit(texture_column, (rays * SCALE, SCREEN_HEIGHT // 2 - wall_height // 2))  
                break
        start_angle += STEP_ANGLE  

def cast_floor(win, player):
    """Αποδίδει το πάτωμα με υφές."""
    for y in range(SCREEN_HEIGHT // 2, SCREEN_HEIGHT): 
        denominator = 2.0 * y - SCREEN_HEIGHT 
        if denominator == 0:
            continue

        ray_distance = (SCREEN_HEIGHT / denominator) / (math.cos(player.angle) + 0.0001)
        floor_x = player.x + ray_distance * math.sin(player.angle)  
        floor_y = player.y - ray_distance * math.cos(player.angle) 

        tex_x = int(floor_x % TILE_SIZE / TILE_SIZE * floor_texture.get_width())  
        tex_y = int(floor_y % TILE_SIZE / TILE_SIZE * floor_texture.get_height())  

        color = floor_texture.get_at((tex_x, tex_y))  
        pygame.draw.line(win, color, (0, y), (SCREEN_WIDTH, y))  

def check_gate_interaction(player):
    """Ελέγχει αν ο παίκτης είναι κοντά στην πύλη και αλληλεπιδρά."""
    player_row = int(player.y / TILE_SIZE)  
    player_col = int(player.x / TILE_SIZE)  
    gate_row, gate_col = 11, 30  

    if abs(player_row - gate_row) <= 1 and abs(player_col - gate_col) <= 1:  
        return True
    return False
