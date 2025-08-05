from chess.geometry.coordinate.coordinate import Coordinate


class Horizontal:
    """X changes while Y stays the same."""

    @staticmethod
    def is_horizontal(origin: Coordinate, destination: Coordinate) -> bool:
        # Same row, column changes
        return origin.row == destination.row and origin.column != destination.column