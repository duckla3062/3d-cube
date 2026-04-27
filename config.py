"""
Global configuration constants for window, assets, gameplay, and camera.
"""

import pygame


# # Window
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
DISPLAY = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "3D Cube Stacking"

# Assets
FONT_PATH = "assets/font_pixel.ttf"

# Gameplay
INITIAL_CUBE_POS = (-1.0, -1.0, -1.0)
INITIAL_CUBE_SIZE = (2.0, 2.0, 2.0)
SPAWN_RADIUS = 10.0            # distance from target for new cube spawn
STACK_HEIGHT_STEP = 2.0        # vertical step when spawning a new cube
ARRIVAL_FRAMES = 100.0         # frames to reach target (controls speed)
MAX_DISPLAY_SCORES = 10        # number of scores stored
MAX_TRIES = 3                  # number of tries per round

# Camera
INITIAL_AZIMUTH = 45.0         # degrees
INITIAL_ELEVATION = 30.0       # degrees
INITIAL_RADIUS = 10.0          # distance from focus
ELEVATION_MIN = -89.9
ELEVATION_MAX = 89.9
MOUSE_SENSITIVITY = 0.3
ZOOM_STEP = 0.5
CAMERA_Y_OFFSET = 1.0          # small lift above the cube center

# import Timing
FRAME_DELAY_MS = 10

# Users
USER_INCLUDE = [23103, 24094, 24111, 25080, 26022, 26023, 26026, 26034, 26048, 26051, 26070, 26085, 26087, 26098, 26100, 26106, 26117, 26124, 26131, 26133, 26140, 26142]
USER_EXCLUDE = []
USER_YEAR_MAX = [119, 149, 126, 151, 124]

# Variable assets
textures = {
    "normal": None,
    "var_a": None,
    "var_pos": None
}
is_global = True
username = ""
current_tries = 0
current_max_score = 0
rated_leaderboard_file = "H:/open-day/rated.txt"
unrated_leaderboard_file = "H:/open-day/unrated.txt"
rated = False

def init_config():
    # Window initialize
    pygame.init()
    # display_info = pygame.display.Info()
    # SCREEN_WIDTH, SCREEN_HEIGHT = display_info.current_w, display_info.current_h
    # DISPLAY = (SCREEN_WIDTH, SCREEN_HEIGHT)
    # print(SCREEN_WIDTH, SCREEN_HEIGHT)