from enum import Enum, auto


class ActivityState(Enum):
    ACTIVE_KING = auto(),
    KING_IN_CHECK = auto(),
    CHECKMATED_KING = auto(),
    ACTIVE_COMBATANT = auto(),
    CAPTURED_COMBATANT = auto(),
    BLOCKED_COMBATANT = auto(),
    PROMOTED_PAWN = auto(),
    NOT_OPENED = auto(),
    FORMATION__ASSIGNED =  auto(),
    FORMATION_ENACTED = auto(),
    PLACED_ON_BOARD = auto()
    REMOVED_FROM_BOARD = auto()
    REGISTERED_HOSTAGE = auto(),
