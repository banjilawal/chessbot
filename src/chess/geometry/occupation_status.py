from enum import auto, Enum


class OccupationStatus(Enum):
    BLOCKED = auto()
    HAS_ENEMY = auto()
    IS_VACANT = auto()