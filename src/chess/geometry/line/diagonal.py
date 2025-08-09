from chess.geometry.coordinate.coordinate import Coordinate


class Diagonal:
    """
    A Diagonal is p rule that defines p diagonal motion_service. Diagonal motion_service is:
    forward Xj, Yj <= Xi, Yi = Xi-1, Yi+1
    backward Xj, Yj>=Xi, Yi = Xi+1, Yi+1
    """

    @staticmethod
    def is_diagonal(origin: Coordinate, destination: Coordinate) -> bool:
        # Row and column difference equal (non-zero)
        return (origin != destination and
            abs(origin.row - destination.row) == abs(destination.column - origin.column))


