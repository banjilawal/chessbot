from enum import Enum


class DefinitionCategory(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    DIAGONAL = "diagonal"
    PAWN = "pawn"
    KNIGHT = "knight"
    KING = "king"
    QUEEN = "queen"
    PAWN_CAPTURE_ENEMY = "pawn capture enemy"

    def id(self):
        if self == DefinitionCategory.HORIZONTAL:
            return 1
        elif self == DefinitionCategory.VERTICAL:
            return 2
        elif self == DefinitionCategory.DIAGONAL:
            return 3
        elif self == DefinitionCategory.PAWN:
            return 4
        elif self == DefinitionCategory.KNIGHT:
            return 5
        elif self == DefinitionCategory.KING:
            return 6
        elif self == DefinitionCategory.QUEEN:
            return 7
        elif self == DefinitionCategory.PAWN_CAPTURE_ENEMY:
            return 8
        else:
            return 0