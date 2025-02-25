import pygame
import sys
import os  # Για να τρέξουμε το main.py
from settings import *

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 50)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Aναπαραγωγή μουσικής
pygame.mixer.init()
if not pygame.mixer.music.get_busy():
    pygame.mixer.music.load("menu_music.wav") 
    pygame.mixer.music.set_volume(0.5) 
    pygame.mixer.music.play(-1)  

# Menu
menu_options = ["Start Game", "Controls", "How to Play", "Exit"]
selected_option = 0  # Δείχνει ποια επιλογή είναι ενεργή

# Wallpaper
background_image = pygame.image.load("maze.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_menu():
    """Σχεδιάζει το start menu στην οθόνη"""
    win.blit(background_image, (0, 0)) 
    title = font.render("Escape", True, WHITE)
    win.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

    for i, option in enumerate(menu_options):
        color = RED if i == selected_option else WHITE
        text = font.render(option, True, color)
        win.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 250 + i * 60))

    pygame.display.flip()

def show_controls():
    """Σχεδιάζει το controls menu"""
    running = True
    while running:
        win.fill((0, 0, 0))
        title = font.render("Controls", True, WHITE)
        win.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        controls_text = [
            "WASD - Move",
            "Mouse - Look Around",
            "E - Interact",
            "ESC - Back to Menu"
        ]

        for i, text in enumerate(controls_text):
            text_surface = font.render(text, True, WHITE)
            win.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 200 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

def show_how_to_play():
    """Σχεδιάζει το how to play menu"""
    running = True
    while running:
        win.fill((0, 0, 0))
        title = font.render("How to Play", True, WHITE)
        win.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        how_to_play_text = [
            "You entered through a magic portal,",
            "find the exit portal to escape the maze."
        ]

        for i, text in enumerate(how_to_play_text):
            text_surface = font.render(text, True, WHITE)
            win.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 200 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

def main_menu():
    """Διαχειρίζεται το start menu"""
    global selected_option
    running = True
    while running:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN: 
                    if selected_option == 0: 
                        pygame.mixer.music.stop() 
                        pygame.quit()  
                        os.system("python main.py") 
                        sys.exit()
                    elif selected_option == 1: 
                        show_controls()
                    elif selected_option == 2: 
                        show_how_to_play()
                    elif selected_option == 3:  
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main_menu()
