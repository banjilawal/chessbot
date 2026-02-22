from enum import Enum, auto


class TokenStackState(Enum):
    EMPTY = auto(),
    PARTIALLY_FULL = auto(),
    DEPLOYED_ON_BOARD = auto(),
    FILLED_READY_TO_DEPLOY = auto(),
