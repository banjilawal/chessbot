from enum import Enum, auto

class MousePlacementStatus(Enum):
    PLACED = auto()
    BLOCKED = auto()
    RELEASED = auto()
    INVALID = auto()