from enum import Enum, auto


class Event(Enum):
    ATTACK = auto(),
    PROMOTION = auto(),
    OCCUPATION = auto(),
    MARK_OBSTRUCTION = auto()

