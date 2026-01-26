from enum import auto, Enum


class InsertionResultEnum(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    EMPTY = auto(),
    TIMED_OUT = auto(),