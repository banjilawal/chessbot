from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.horizontal import HorizontalDefinition


class QueenDefinition(GeometryPattern):
    def __init__(self, definition_id: int, title: str):
        super().__init__(definition_id, title)

    def line_fits_definition(self, origin: Coordinate, destination: Coordinate) -> bool:
        horizontal_def = HorizontalDefinition(definition_id=1, title="horizontal")
        vertical_def = GeometryPattern(definition_id=2, title="vertical")

        return (horizontal_def.line_fits_definition(origin, destination)
                or vertical_def.line_fits_definition(origin, destination))