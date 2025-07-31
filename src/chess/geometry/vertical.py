from chess.geometry.board.coordinate import Coordinate


class Vertical:
    """Y changes while X stays the same."""

    @staticmethod
    def is_vertical(origin: Coordinate, destination: Coordinate) -> bool:
        return origin.column == destination.column and origin.row != destination.row