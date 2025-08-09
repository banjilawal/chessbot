from chess.geometry.coordinate.coordinate import Coordinate
from chess.token.piece import ChessPiece


class Obstruction:
    _obstructor_id: int
    _blocked_coordinate:Coordinate

    def __init__(self, obstructor: ChessPiece):
        self._obstructor_id = obstructor.id
        self._blocked_coordinate = obstructor.coordinate_stack.current_coordinate()

    @property
    def obstructor_id(self) -> int:
        return self._obstructor_id

    @property
    def blocked_coordinate(self) -> Coordinate:
        return self._blocked_coordinate