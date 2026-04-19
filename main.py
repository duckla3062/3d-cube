"""
Application entry: main menu, navigation to game and leaderboard.
"""

import config
import pygame
import os
from ui import draw_text
from leaderboard import show_leaderboard
from game import game_loop
from config import DISPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, GLOBAL_LEADERBOARD_FILE, LOCAL_LEADERBOARD_FILE, is_global
from input import input_index
from tutorial import show_tutorial

def main_menu() -> None:
    """
    Show the main menu and route to game or leaderboard.
    """

    global is_global, current_max_score, username
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption(WINDOW_TITLE)

    is_running = True
    while is_running:
        screen.fill((0, 0, 0))
        draw_text(screen, "3D Cube Stacking Game",
                  (SCREEN_WIDTH//2-250, SCREEN_HEIGHT//4-50,
                   SCREEN_WIDTH//2+250, SCREEN_HEIGHT//4),
                   size=42, align="center")
        draw_text(screen, "Press SPACE to start",
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2-50,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2),
                   size=32, align="center")
        draw_text(screen, "Press L to view leaderboard",
                  (SCREEN_WIDTH//2-250, SCREEN_HEIGHT//2,
                   SCREEN_WIDTH//2+250, SCREEN_HEIGHT//2+50),
                   size=28, align="center")
        draw_text(screen, "Press ESC to quit",
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2+75,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2+125),
                   size=28, align="center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_max_score = 0
                    input_index(menu_callback=main_menu)
                    if config.username == "":
                        config.username = "guest"
                    print(config.username)
                    game_loop(main_menu_callback=main_menu)
                elif event.key == pygame.K_l:
                    leaderboard_file = LOCAL_LEADERBOARD_FILE
                    leaderboard_title = "Local Leaderboard"
                    if is_global == True:
                        leaderboard_file = GLOBAL_LEADERBOARD_FILE
                        leaderboard_title = "Overall Leaderboard"
                    show_leaderboard(leaderboard_file, leaderboard_title)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()

                    quit()
 
        pygame.display.flip()


if __name__ == "__main__":
    if os.path.isfile(GLOBAL_LEADERBOARD_FILE):
        is_global = True
    main_menu()
