import pygame
import sys
from settings import *
from map import MAP
from player import Player
from raycasting import cast_rays, cast_floor, load_texture

def main():
    pygame.init()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player()

    # Φόρτωση των υφών μετά την αρχικοποίηση του Pygame
    load_texture()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        win.fill((0, 0, 0))
        
        # Απόδοση πατώματος και τοίχων
        cast_floor(win, player)
        cast_rays(win, player)
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
