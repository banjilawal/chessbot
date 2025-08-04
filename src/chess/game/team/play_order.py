from enum import Enum, auto

from pygame.pixelcopy import surface_to_array


class PlayOrderr(Enum):
    FIRST = auto()
    SECOND = auto()