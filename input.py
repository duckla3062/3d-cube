"""
Showing a tutorial screen for user.
"""

import config
import pygame
from ui import draw_text
from config import DISPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_TRIES, USER_INCLUDE, USER_EXCLUDE, USER_YEAR_MAX

def input_index(menu_callback) -> None:

    screen = pygame.display.set_mode(DISPLAY)
    is_running = True
    config.username = ""
    config.current_max_score = 0
    config.current_tries = 0
    
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
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
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

def is_student(username: str) -> bool:
    isnum = True
    for char in username:
        if char.isdigit() == False:
            isnum = False
            break
    if isnum == False:
        return False
    num = int(username)
    if num > 31999:
        return False
    elif num < 27000:
        for i in USER_INCLUDE:
            if i == num:
                return True
        return False
    else:
        q = num//1000-27
        r = num%1000
        if r > USER_YEAR_MAX[q]:
            return False
        for i in USER_EXCLUDE:
            if i == num:
                return False
        return True
    