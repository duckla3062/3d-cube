"""
Lose screen handling.
"""

import config
import pygame
from ui import draw_text
from leaderboard import update_leaderboard
from config import DISPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_TRIES


def lose_screen(score: int, restart_callback, menu_callback):
    """
    Chooses a lose screen depends on whether the player still have chances to retry.
    """
    
    config.current_max_score = max(config.current_max_score, score)
    if config.current_tries < MAX_TRIES:
       lose_retry(score, restart_callback, menu_callback)
    else:
       lose_final(score, menu_callback)

def lose_retry(score: int, restart_callback, menu_callback):
    """
    Display the lose screen with options to restart or return to main menu.
    """
    
    screen = pygame.display.set_mode(DISPLAY)
    is_running = True

    while is_running:
        screen.fill((0, 0, 0))
        draw_text(screen, "You Lose!", 
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//4-50,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//4),
                   size=42, align="center")
        draw_text(screen, f"Your Current Score: {score}", 
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2-100,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2-50),
                   size=32, align="center")
        draw_text(screen, f"Your Best Score: {config.current_max_score}", 
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2-50,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2),
                   size=32, align="center")
        draw_text(screen, "Press SPACE to restart", 
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2+50),
                   size=28, align="center")
        draw_text(screen, "Press ESC to return to main menu", 
                  (SCREEN_WIDTH//2-250, SCREEN_HEIGHT//2+75,
                   SCREEN_WIDTH//2+250, SCREEN_HEIGHT//2+125),
                   size=28, align="center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    restart_callback(main_menu_callback=menu_callback)
                elif event.key == pygame.K_ESCAPE:
                    if config.rated:
                        update_leaderboard(config.current_max_score, config.rated_leaderboard_file)
                    else:
                        update_leaderboard(config.current_max_score, config.unrated_leaderboard_file)
                    menu_callback()

        pygame.display.flip()
    
def lose_final(score: int, menu_callback):
    """
    Display the lose screen only with options to return to main menu.

    Parameters:
        score (int): Final score achieved before losing.
    """

    if config.rated:
        update_leaderboard(config.current_max_score, config.rated_leaderboard_file)
    else:
        update_leaderboard(config.current_max_score, config.unrated_leaderboard_file)

    screen = pygame.display.set_mode(DISPLAY)
    is_running = True

    while is_running:
        screen.fill((0, 0, 0))
        draw_text(screen, "You Lose!", 
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//4-50,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//4),
                   size=42, align="center")
        draw_text(screen, f"Your Current Score: {score}", 
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2-100,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2-50),
                   size=32, align="center")
        draw_text(screen, f"Your Best Score: {config.current_max_score}", 
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2-50,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2),
                   size=32, align="center")
        draw_text(screen, "Press ESC to return to main menu", 
                  (SCREEN_WIDTH//2-250, SCREEN_HEIGHT//2,
                   SCREEN_WIDTH//2+250, SCREEN_HEIGHT//2+50),
                   size=28, align="center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_callback()

        pygame.display.flip()