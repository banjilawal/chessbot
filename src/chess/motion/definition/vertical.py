from chess.common.geometry import Coordinate
from chess.motion.definition.definition import Definition
from chess.motion.definition.definition_category import DefinitionCategory


class VerticalDefinition(Definition):
    """Y changes while X stays the same."""
    def __init__(self, definition_category: DefinitionCategory= DefinitionCategory.VERTICAL):
        super().__init__(self, id=definition_category.id, title=definition_category.value)


    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same column, row changes
        return origin.column == destination.column and origin.row != destination.row