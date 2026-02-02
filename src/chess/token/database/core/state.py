from enum import Enum, auto


class TokenStackState(Enum):
    EMPTY = auto(),
    FILLED_READY_TO_DEPLOY = auto(),
    DEPLOYED_ON_BOARD = auto(),