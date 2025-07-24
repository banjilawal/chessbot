from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.definition_category import DefinitionCategory


class VerticalDefinition(GeometryPattern):
    """Y changes while X stays the same."""
    def __init__(self, definition_category: DefinitionCategory= DefinitionCategory.VERTICAL):
        if definition_category is None:
            raise TypeError("definition_category cannot be None")
        if not definition_category == DefinitionCategory.VERTICAL:
            raise ValueError("definition_category must be vertical")

        super().__init__(self, id=definition_category.id, title=definition_category.value)


    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same column, row changes
        return origin.column == destination.column and origin.row != destination.row