"""
Showing a tutorial screen for user.
"""

import config
import pygame
from ui import draw_text
from config import DISPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_TRIES


def input_index(menu_callback) -> None:

    screen = pygame.display.set_mode(DISPLAY)
    is_running = True
    config.username = ""
    
    while is_running:
        screen.fill((0, 0, 0))
        draw_text(screen, "Input your index number.", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//4-50,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//4),
                   size=42, align="center")
        draw_text(screen, "e.g. If your index number is sms27072, input '27072'.", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2-50,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2),
                   size=28, align="center")
        draw_text(screen, "Unrecognizable index number will not be counted for prize.", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2+50),
                   size=28, align="center")
        draw_text(screen, "Press Enter after inputting your index number.", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2+50,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2+100),
                   size=28, align="center")
        draw_text(screen, f"Your Username: {config.username}", 
                  (0, SCREEN_HEIGHT//2+125,
                   SCREEN_WIDTH, SCREEN_HEIGHT//2+175),
                   size=28, align="center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    menu_callback()
                elif event.key == pygame.K_BACKSPACE:
                    if config.username != "":
                        config.username = config.username[:-1]
                else:
                    press_char = event.unicode
                    if press_char.isprintable() and len(press_char) == 1:
                        config.username += press_char
        
        pygame.display.flip()

    return