"""
Leaderboard file I/O and display screen.
"""

import config
import pygame
from typing import List
from ui import draw_text
from config import DISPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_DISPLAY_SCORES


def read_leaderboard(filename: str) -> List[int]:
    """
    Read leaderboard scores from file.

    Parameters:
        filename (str): Path to leaderboard file.

    Returns:
        List[int]: List of scores (descending order assumed or enforced later).
    """
    scores = []
    try:
        with open(filename, "r") as f:
            count = int(f.readline().strip())
            for _ in range(count):
                line = f.readline()
                line = line.split()
                # print(line)
                rscore = int(line[0])
                rname = str(line[1])
                if not line:
                    break
                scores.append([rscore, rname])
    except FileNotFoundError:
        # Initialize an empty file
        with open(filename, "w") as f:
            f.write("0\n")
    return scores


def write_leaderboard(scores: List[int], filename: str) -> None:
    """
    Write leaderboard scores to file.

    Parameters:
        scores (List[int]): Scores to write (will be truncated/padded).
        filename (str): Path to leaderboard file.
    """
    with open(filename, "w") as f:
        f.write((str(min(len(scores), MAX_DISPLAY_SCORES)) + "\n"))
        for i in range(min(len(scores), MAX_DISPLAY_SCORES)):
            s = scores[i] if i < len(scores) else [0, "none"]
            f.write(str(s[0]) + ' ' + str(s[1]) + "\n")


def update_leaderboard(new_score: int, filename: str) -> None:
    """
    Add a new score to leaderboard and persist it.

    Parameters:
        new_score (int): Player score to add.
        filename (str): Path to leaderboard file.
    """
    scores = read_leaderboard(filename)
    found = False
    for i in range(len(scores)):
        if scores[i][1] == config.username:
            scores[i][0] = max(scores[i][0], new_score)
            found = True
    if found == False:
        scores.append([new_score, config.username])
    scores = sorted(scores, reverse=True)
    write_leaderboard(scores, filename)


def show_leaderboard(filename: str, title: str) -> None:
    """
    Display the local leaderboard screen.
    """
    screen = pygame.display.set_mode(DISPLAY)
    is_running = True

    while is_running:
        screen.fill((0, 0, 0))
        draw_text(screen, title,
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//4-50,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//4),
                  size=32, align="center")
        draw_text(screen, "Press ESC to return",
                  (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//4,
                   SCREEN_WIDTH//2+200, SCREEN_HEIGHT//4+50),
                  size=28, align="center")

        scores = read_leaderboard(filename)
        # print(scores)
        for i, s in enumerate(sorted(scores, reverse=True)[:5], start=1):
            draw_text(screen, f"{i}. {s[0]}: {s[1]}",
                      (SCREEN_WIDTH//2-200, SCREEN_HEIGHT//4+i*50+50,
                       SCREEN_WIDTH//2+200, SCREEN_HEIGHT//4+i*50+100),
                      size=32, align="center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                elif event.key == pygame.K_TAB:
                    if filename == config.rated_leaderboard_file:
                        filename = config.unrated_leaderboard_file
                        title = title[:-11]
                        title += " (Others)"
                    else:
                        filename = config.rated_leaderboard_file
                        title = title[:-9]
                        title += " (Students)"

        pygame.display.flip()
