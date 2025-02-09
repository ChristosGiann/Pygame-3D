import pygame
import sys
import os  # Για επιστροφή στο menu
from settings import *
from map import MAP
from player import Player
from raycasting import cast_rays, cast_floor, load_textures, render_sky, check_gate_interaction

def play_gate_sound_if_in_range(player, gate_row, gate_col, interaction_range, gate_sound):
    """Παίζει ήχο αν ο παίκτης είναι εντός διπλάσιου εύρους της πύλης."""
    player_row = int(player.y / TILE_SIZE)
    player_col = int(player.x / TILE_SIZE)
    distance = ((player_row - gate_row) ** 2 + (player_col - gate_col) ** 2) ** 0.5

    # Αν ο παίκτης είναι εντός διπλάσιου range, παίζει ο ήχος
    if distance <= 2 * interaction_range:
        gate_sound.play()

def main():
    pygame.init()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player()

    # Φορτώνουμε όλες τα textures
    load_textures()

    # Αναπαραγωγή μουσικής
    pygame.mixer.init()
    pygame.mixer.music.load("gameplay_music.wav")  # Φορτώνει το αρχείο μουσικής
    pygame.mixer.music.set_volume(0.5)  # Ρυθμίζει την ένταση
    pygame.mixer.music.play(-1)  # Παίζει σε loop (-1 σημαίνει άπειρο loop)
    gate_sound = pygame.mixer.Sound("gate_sound.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    os.system("python menu.py")
                    sys.exit()
                if event.key == pygame.K_e and check_gate_interaction(player):
                    print("You escaped!")
                    pygame.mixer.music.stop()
                    pygame.quit()
                    os.system("python menu.py")
                    sys.exit()
                if event.key == pygame.K_v:  # V → Teleport μπροστά από την πύλη
                    player.x = 30 * TILE_SIZE + TILE_SIZE // 2  
                    player.y = 11 * TILE_SIZE + TILE_SIZE // 2 
        
        # Παίζει τον ήχο αν ο παίκτης είναι εντός διπλάσιου range
        play_gate_sound_if_in_range(player, gate_row=11, gate_col=30, interaction_range=1, gate_sound=gate_sound)

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.handle_mouse_movement()

        win.fill((0, 0, 0))
        
        #Φορτώνουμε περιβάλλον
        render_sky(win)
        cast_floor(win, player)
        cast_rays(win, player)
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
