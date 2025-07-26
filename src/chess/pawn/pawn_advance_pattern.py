class PawnAdvancePattern:
    """
    Refactored PawnAdvancePattern to handle the pawn's first move which can be two steps forward.
    PawnAdvancePattern has a different method siganture than patterns for king, quuen, bishop,
    and castle. It cannot be part of the GeometryPattern class hierarchy. Because its the one and
    only class that need to handle first advances differently and there's only 6 cases and interface
    is pointless.
    """

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
        else:
            return row_diff == 1

