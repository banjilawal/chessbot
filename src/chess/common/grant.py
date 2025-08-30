from enum import Enum, auto


class Permission(Enum):
    GRANT_ATTACK = auto(),
    GRANT_PROMOTION = auto(),
    GRANT_OCCUPATION = auto(),
    MARK_OBSTRUCTION = auto()

