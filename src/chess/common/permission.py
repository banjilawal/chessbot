from enum import Enum, auto


class Permission(Enum):
    DENY_ATTACK_PERMISSION = auto(),
    DENY_PROMOTION_PERMISSION = auto(),
    DENY_OCCUPATION_PERMISSION = auto()

    GRANT_ATTACK_PERMISSION = auto(),
    GRANT_PROMOTION_PERMISSION = auto(),
    GRANT_OCCUPATION_PERMISSION = auto(),

