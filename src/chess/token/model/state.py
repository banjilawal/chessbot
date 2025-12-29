from enum import Enum, auto


class TokenState(Enum):
    ACTIVE_KING = auto(),
    KING_IN_CHECK = auto(),
    CHECKMATED_KING = auto(),
    ACTIVE_COMBATANT = auto(),
    CAPTURED_COMBATANT = auto(),
    PROMOTED_PAWN = auto(),
    NOT_OPENED = auto(),
