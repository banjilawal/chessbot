from enum import Enum, auto


class OccupantCategory(Enum):
    NO_OCCUPANT = auto(),
    BLOCKING_OCCUPANT = auto(),
    TARGET = auto(),