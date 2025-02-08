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

        # Κλείδωμα ποντικιού στην οθόνη
        self.mouse_locked = True
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

    def move(self, keys):
        new_x = self.x
        new_y = self.y
        
        # Περιστροφή με A/D ή με το ποντίκι
        if keys[pygame.K_a]:  # A -> αριστερά
            self.angle -= 0.05
        if keys[pygame.K_d]:  # D -> δεξιά
            self.angle += 0.05

        # Κίνηση μπροστά/πίσω
        if keys[pygame.K_w]:  # W -> μπροστά
            new_x = self.x + -math.sin(self.angle) * self.speed
            new_y = self.y + +math.cos(self.angle) * self.speed
        if keys[pygame.K_s]:  # S -> πίσω
            new_x = self.x + +math.sin(self.angle) * self.speed
            new_y = self.y + -math.cos(self.angle) * self.speed
        
        # Έλεγχος αν η νέα θέση είναι τοίχος
        if self.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def is_valid_position(self, x, y):
        """ Ελέγχει αν η θέση είναι έγκυρη (δηλαδή αν δεν είναι τοίχος) """
        row = int(y / TILE_SIZE)
        column = int(x / TILE_SIZE)
        
        return MAP[row * MAP_SIZE + column] != '#'

    def handle_mouse_movement(self):
        """Χειρίζεται την κίνηση του ποντικιού για περιστροφή της κάμερας"""
        keys = pygame.key.get_pressed()

        # Αν πατηθεί ESC, ξεκλειδώνει το ποντίκι και το εμφανίζει
        if keys[pygame.K_ESCAPE]:
            self.mouse_locked = False
            pygame.mouse.set_visible(True)
            pygame.event.set_grab(False)
            return  # Σταματάει την εκτέλεση της συνάρτησης

        # Αν πατηθεί ENTER, ξανακλειδώνει το ποντίκι
        if keys[pygame.K_RETURN]:
            self.mouse_locked = True
            pygame.mouse.set_visible(False)
            pygame.event.set_grab(True)

        # Μην κινείς το ποντίκι αν είναι ξεκλείδωτο
        if not self.mouse_locked:
            return

        # Αν είναι κλειδωμένο, συνεχίζει να ενημερώνει τη γωνία
        mouse_x, _ = pygame.mouse.get_pos()
        center_x = SCREEN_WIDTH // 2

        # Υπολογισμός διαφοράς θέσης ποντικιού
        delta_x = mouse_x - center_x
        self.angle += delta_x * 0.002  # Ευαισθησία ποντικιού

        # Επαναφορά του ποντικιού στο κέντρο της οθόνης
        pygame.mouse.set_pos([center_x, SCREEN_HEIGHT // 2])
