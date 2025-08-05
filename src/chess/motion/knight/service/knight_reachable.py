from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.reachable import Reachable


class KnightReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        row_diff = abs(origin.row - destination.row)
        col_diff = abs(origin.column - destination.column)

        # A KnightMotionController's move is always (2,1) or (1,2) in terms of row/column difference
        return (row_diff == 2 and col_diff == 1) or \
            (row_diff == 1 and col_diff == 2)