from chess.motion.logic.reachable import Reachable
from chess.motion.logic.definition_category import DefinitionCategory


class VerticalPatern(Reachable):
    """Y changes while X stays the same."""

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return origin.column == destination.column and origin.row != destination.row