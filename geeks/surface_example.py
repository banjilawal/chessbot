import pygame
import sys

def main():
    pygame.init()

    # creating the display surface
    display_surface = pygame.display.set_mode((500, 500))


    pygame.Surface.set_colorkey([255, 255, 255])

    display_surface.blit( (100, 100))

    # updating the display
    pygame.display.flip()

if __name__ == "__main__":
    main()
