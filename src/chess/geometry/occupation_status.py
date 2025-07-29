from enum import auto, Enum


class OccupationStatus(Enum):
    IS_BLOCKED = auto()
    HAS_ENEMY = auto()
    IS_VACANT = auto()