from chess.common.geometry import Coordinate
from chess.motion.definition.definition import Definition


class KingDefinition(Definition):
    def __init__(self, definition_id: int, title: str):
        super().__init__(definition_id, title)

    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        return abs(origin.row - destination.row) == 1 and abs(origin.column - destination.column) == 1