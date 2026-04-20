"""
Showing a tutorial screen for user.
"""

import pygame
from ui import draw_text
from config import DISPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_TRIES


def show_tutorial(menu_callback) -> None:

    screen = pygame.display.set_mode(DISPLAY)
    is_running = True
    verify_text = ""

    while is_running:
        screen.fill((0, 0, 0))
        draw_text(screen, "Stack the cubes as tall as you can.", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2-175,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2-125),
                   size=42, align="center")
        draw_text(screen, f"Green cubes are normal cubes,", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2-100,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2-50),
                   size=28, align="center")
        draw_text(screen, "Red cubes occasionally change their speed,", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2-50,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2),
                   size=28, align="center")
        draw_text(screen, "Purple cubes occasionally teleports when moving.", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2+50),
                   size=28, align="center")
        draw_text(screen, "Press space if you understand the rules.", 
                  (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2+75,
                   SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2+125),
                   size=28, align="center")
        draw_text(screen, f"You have {MAX_TRIES} tries in total.", 
                  (SCREEN_WIDTH//2-500, SCREEN_HEIGHT//2+125,
                   SCREEN_WIDTH//2+500, SCREEN_HEIGHT//2+175),
                   size=28, align="center")
        draw_text(screen, f"If you finish reading the tutorial, type the text shown in the bottom right corner and press enter.", 
                  (SCREEN_WIDTH//2-500, SCREEN_HEIGHT//2+175,
                   SCREEN_WIDTH//2+500, SCREEN_HEIGHT//2+200),
                   size=14, align="center")
        draw_text(screen, f"{verify_text}", 
                  (SCREEN_WIDTH//2-500, SCREEN_HEIGHT//2+200,
                   SCREEN_WIDTH//2+500, SCREEN_HEIGHT//2+225),
                   size=14, align="center")
        draw_text(screen, f"cpc", 
                  (SCREEN_WIDTH-50, SCREEN_HEIGHT-20,
                   SCREEN_WIDTH, SCREEN_HEIGHT),
                   size=14, align="center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if verify_text == "cpc":
                        start_game_text = ["3", "2", "1", "START!"]
                        for round_text in start_game_text:
                            screen.fill((0, 0, 0))
                            draw_text(screen, round_text, 
                                    (SCREEN_WIDTH//2-400, SCREEN_HEIGHT//2-50,
                                    SCREEN_WIDTH//2+400, SCREEN_HEIGHT//2+50),
                                    size=84, align="center")
                            pygame.display.flip()
                            pygame.time.wait(1000)
                        return
                elif event.key == pygame.K_ESCAPE:
                    menu_callback()
                elif event.key == pygame.K_BACKSPACE:
                    if verify_text != "":
                        verify_text = verify_text[:-1]
                else:
                    press_char = event.unicode
                    if press_char.isprintable() and len(press_char) == 1:
                        verify_text += press_char
        
        pygame.display.flip()

    return