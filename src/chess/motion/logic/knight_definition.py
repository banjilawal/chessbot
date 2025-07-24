from chess.common.geometry import Coordinate
from chess.motion.logic.definition import Definition


class KnightDefinition(Definition):
    def __init__(self, definition_id: int, title: str):
        super().__init__(definition_id, title)

    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        return (abs(origin.row - destination.row) == 3 and
            abs(origin.column - destination.column) == 1)