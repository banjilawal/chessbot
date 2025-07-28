from chess.geometry.coordinate import Coordinate
from chess.motion.logic.reachable import Reachable


class Diagonal(Reachable):
    """
    A Diagonal is a rule that defines a diagonal motion. Diagonal motion is:
    forward Xj, Yj <= Xi, Yi = Xi-1, Yi+1
    backward Xj, Yj>=Xi, Yi = Xi+1, Yi+1
    """

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        # Row and column difference equal (non-zero)
        return (origin != destination and
            abs(origin.row - destination.row) == abs(destination.column - origin.column))


