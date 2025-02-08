import pygame
import sys
import os  # Για επιστροφή στο menu
from settings import *
from map import MAP
from player import Player
from raycasting import cast_rays, cast_floor, load_textures, render_sky

def main():
    pygame.init()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player()

    # Φορτώνουμε όλες τις υφές
    load_textures()

    # 🔊 Φόρτωση και αναπαραγωγή μουσικής gameplay
    pygame.mixer.init()
    pygame.mixer.music.load("gameplay_music.wav")  # Φορτώνει το αρχείο μουσικής
    pygame.mixer.music.set_volume(0.5)  # Ρυθμίζει την ένταση
    pygame.mixer.music.play(-1)  # Παίζει σε loop (-1 σημαίνει άπειρο loop)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC → Επιστροφή στο Menu
                    pygame.mixer.music.stop()  # Σταματάει τη μουσική του gameplay
                    pygame.quit()
                    os.system("python menu.py")  # Ξανατρέχει το menu
                    sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.handle_mouse_movement()

        win.fill((0, 0, 0))
        
        # Ζωγραφίζουμε τον ουρανό
        render_sky(win)
        # Αποδίδουμε το πάτωμα και τους τοίχους
        cast_floor(win, player)
        cast_rays(win, player)
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
