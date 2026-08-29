from enum import Enum, auto


class PathStackState(Enum):
    BEING_DEPLOYED = auto(),
    DEPLOYED_ON_BOARD = auto(),
    READY_FOR_DEPLOYMENT = auto(),
    NOT_READY_FORD_DEPLOYMENT = auto(),
