from enum import Enum, auto

from pygame.pixelcopy import surface_to_array


class PlayerOrder(Enum):
    FIRST = auto()
    SECOND = auto()