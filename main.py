import pygame
from control import Control
from flyobj import *
from config import *


def main():
    cfg = Config()

    # PyGame init
    pygame.init()
    screen = pygame.display.set_mode(cfg.getDisplay())
    pygame.display.set_caption("Solar System")

    # Space init
    bg = Surface(cfg.getDisplay())
    bg.fill(Color(cfg.getSpaceColor()))


    # Timer init
    timer = pygame.time.Clock()

    control = Control(timer, screen, bg, cfg)
    control.run()


if __name__ == "__main__":
    main()

