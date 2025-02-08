import pygame
import math
from settings import *
from map import MAP

# Φόρτωση των υφών
wall_texture = None
floor_texture = None

def load_texture():
    """Φορτώνει τις υφές μετά την αρχικοποίηση του pygame.display"""
    global wall_texture, floor_texture
    wall_texture = pygame.image.load('wall_texture.png').convert()
    floor_texture = pygame.image.load('floor_texture.png').convert()

def cast_rays(win, player):
    start_angle = player.angle - HALF_FOV
    for rays in range(CASTED_RAYS):
        for depth in range(1, MAX_DEPTH):
            # Υπολογισμός κατεύθυνσης της ακτίνας
            ray_dir_x = -math.sin(start_angle)
            ray_dir_y = math.cos(start_angle)

            target_x = player.x + ray_dir_x * depth
            target_y = player.y + ray_dir_y * depth

            # Έλεγχος κελιού στον χάρτη
            row = int(target_y / TILE_SIZE)
            column = int(target_x / TILE_SIZE)
            square = row * MAP_SIZE + column

            if MAP[square] == '#':
                # Διόρθωση βάθους για ομαλή προοπτική
                depth_corrected = depth * math.cos(player.angle - start_angle)
                wall_height = TILE_SIZE / (depth_corrected + 0.0001) * SCREEN_HEIGHT

                # Υπολογισμός της σωστής στήλης υφής
                if abs(ray_dir_x) > abs(ray_dir_y):
                    offset = target_y % TILE_SIZE
                else:
                    offset = target_x % TILE_SIZE
                tex_x = int((offset / TILE_SIZE) * wall_texture.get_width())

                # Κλιμάκωση υφής για τοίχο
                texture_column = wall_texture.subsurface((tex_x, 0, 1, wall_texture.get_height()))
                texture_column = pygame.transform.scale(texture_column, (SCALE, int(wall_height)))

                # Σχεδίαση της στήλης στην οθόνη
                win.blit(texture_column, (rays * SCALE, SCREEN_HEIGHT // 2 - wall_height // 2))
                break
        start_angle += STEP_ANGLE

def cast_floor(win, player):
    """Αποδίδει το πάτωμα με υφή"""
    for y in range(SCREEN_HEIGHT // 2, SCREEN_HEIGHT):
        # Αποφυγή διαίρεσης με το μηδέν
        denominator = 2.0 * y - SCREEN_HEIGHT
        if denominator == 0:
            continue

        # Υπολογισμός της απόστασης από την κάμερα
        ray_distance = (SCREEN_HEIGHT / denominator) / (math.cos(player.angle) + 0.0001)

        # Υπολογισμός των παγκόσμιων συντεταγμένων
        floor_x = player.x + ray_distance * math.sin(player.angle)
        floor_y = player.y - ray_distance * math.cos(player.angle)

        # Συντεταγμένες μέσα στο κελί του χάρτη
        tex_x = int(floor_x % TILE_SIZE / TILE_SIZE * floor_texture.get_width())
        tex_y = int(floor_y % TILE_SIZE / TILE_SIZE * floor_texture.get_height())

        # Απόδοση γραμμής του πατώματος
        color = floor_texture.get_at((tex_x, tex_y))
        pygame.draw.line(win, color, (0, y), (SCREEN_WIDTH, y))
