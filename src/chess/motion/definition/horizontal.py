from chess.common.geometry import Coordinate
from chess.motion.definition.definition import Definition
from chess.motion.definition.definition_category import DefinitionCategory


class HorizontalDefinition(Definition):
    """X changes while Y stays the same."""
    def __init__(self, definition_category: DefinitionCategory= DefinitionCategory.HORIZONTAL):
        super().__init__(self, id=definition_category.id, title=definition_category.value)


    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same row, column changes
        return origin.row == destination.row and origin.column != destination.column