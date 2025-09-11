from enum import auto, Enum

class Line(Enum):
    VERTICAL = auto(),
    DIAGONAL = auto(),
    HORIZONTAL = auto(),
    KING = auto()
    KNIGHT = auto()
    BISHOP = auto ()
    CASTLE = auto()
    QUEEN = auto()
    PAWN_OPENING = auto()
    PAWN_ADVANCE = auto()
    PAWN_ATTACK = auto()
    CURVILINEAR = auto()