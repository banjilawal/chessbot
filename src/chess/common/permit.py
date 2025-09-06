from enum import Enum, auto


class Event(Enum):
    ATTACK = auto(),
    PROMOTION = auto(),
    OCCUPATION = auto(),
    RECORD_ENCOUNTER = auto()

