from enum import Enum, auto


class TokenStackState(Enum):
    EMPTY = auto(),
    FILLED = auto(),
    DEPLOYED_ON_BOARD = auto(),