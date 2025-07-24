from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern


class PawnAdvancePattern:
    @staticmethod
    def matches(
        origin: Coordinate,
        destination: Coordinate,
        position_history: list[Coordinate]
    ) -> bool:
        if len(position_history) == 0 or position_history is None:
            print("position_history is None or empty.")
            return False
        if origin.column != destination.column:
            return False

        row_diff = destination.row - origin.row

        if len(position_history) == 1:
            return row_diff in (1, 2)
        else
            return row_diff == 1

