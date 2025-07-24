from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.definition_category import DefinitionCategory


class DiagonalDefinition(GeometryPattern):
    """
    A DiagonalDefinition is a rule that defines a diagonal motion. Diagonal motion is:
    forward Xj, Yj <= Xi, Yi = Xi-1, Yi+1
    backward Xj, Yj>=Xi, Yi = Xi+1, Yi+1
    """

    def __init__(self, definition_id, title):
        super().__init__(self, id=definition_id, title=title)


    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Row and column difference equal (non-zero)
        return (origin != destination and
            abs(origin.row - destination.row) == abs(destination.column - origin.column))


