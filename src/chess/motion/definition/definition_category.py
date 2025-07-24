from enum import Enum


class DefinitionCategory(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    DIAGONAL = "diagonal"

    def id(self):
        if self == DefinitionCategory.HORIZONTAL:
            return 1
        elif self == DefinitionCategory.VERTICAL:
            return 2
        elif self == DefinitionCategory.DIAGONAL:
            return 3
        else:
            return 0