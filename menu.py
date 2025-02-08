import pygame
import sys
import os  # Για να τρέξουμε το main.py
from settings import *

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 50)

# Χρώματα
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Επιλογές του μενού
menu_options = ["Start Game", "Controls", "Exit"]
selected_option = 0  # Δείχνει ποια επιλογή είναι ενεργή

def draw_menu():
    """Σχεδιάζει το main menu στην οθόνη"""
    win.fill((0, 0, 0))  # Μαύρο background
    title = font.render("Main Menu", True, WHITE)
    win.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

    for i, option in enumerate(menu_options):
        color = YELLOW if i == selected_option else WHITE
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
                if event.key == pygame.K_ESCAPE:  # ESC → Πίσω στο Menu
                    running = False

def main_menu():
    """Διαχειρίζεται το main menu"""
    global selected_option
    running = True
    while running:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Μετακίνηση πάνω στο μενού
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:  # Μετακίνηση κάτω στο μενού
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:  # Επιλογή κουμπιού
                    if selected_option == 0:  # Start Game
                        pygame.quit()  # Κλείνει το μενού
                        os.system("python main.py")  # Εκκινεί το παιχνίδι
                        sys.exit()
                    elif selected_option == 1:  # Controls
                        show_controls()
                    elif selected_option == 2:  # Exit
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main_menu()
