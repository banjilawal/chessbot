from chess.geometry.coordinate import Coordinate
from chess.motion.logic.reachable import Reachable
from chess.motion.logic.definition_category import DefinitionCategory


class Horizontal:
    """X changes while Y stays the same."""

    @staticmethod
    def is_horizontal(origin: Coordinate, destination: Coordinate) -> bool:
        # Same row, column changes
        return origin.row == destination.row and origin.column != destination.column