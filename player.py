import pygame
import math
from settings import *
from map import MAP

class Player:
    def __init__(self):
        self.x = (SCREEN_WIDTH / 2) / 2
        self.y = (SCREEN_WIDTH / 2) / 2
        self.angle = 180 * math.pi / 180
        self.speed = SPEED

    def move(self, keys):
        new_x = self.x
        new_y = self.y
        
        # Έλεγχος για κίνηση αριστερά/δεξιά (γωνία)
        if keys[pygame.K_a]:  # A -> αριστερά
            self.angle -= 0.1
        if keys[pygame.K_d]:  # D -> δεξιά
            self.angle += 0.1

        # Έλεγχος για κίνηση μπροστά/πίσω
        if keys[pygame.K_w]:  # W -> μπροστά
            new_x = self.x + -math.sin(self.angle) * self.speed
            new_y = self.y + +math.cos(self.angle) * self.speed
        if keys[pygame.K_s]:  # S -> πίσω
            new_x = self.x + +math.sin(self.angle) * self.speed
            new_y = self.y + -math.cos(self.angle) * self.speed
        
        # Έλεγχος αν η νέα θέση είναι σε τοίχο
        if self.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def is_valid_position(self, x, y):
        """ Ελέγχει αν η θέση είναι έγκυρη (δηλαδή αν δεν είναι τοίχος) """
        row = int(y / TILE_SIZE)
        column = int(x / TILE_SIZE)
        
        if MAP[row * MAP_SIZE + column] == '#':
            return False
        return True
