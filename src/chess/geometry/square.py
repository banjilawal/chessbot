from typing import Optional

from chess.common.piece import Piece
from chess.geometry.coordinate import Coordinate


class Square:
    _id: int
    _coordinate: Coordinate
    _occupant: Optional[Piece]

    def __init__(self, square_id: int, coordinate: Coordinate):
        if square_id < 0:
            raise ValueError("Square id cannot be negative.")
        if coordinate is None:
            raise ValueError("Coordinate cannot be None.")

        self._id = square_id
        self._coordinate = coordinate
        self._occupant = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def coordinate(self) -> Coordinate:
        return self._coordinate

    @property
    def occupant(self) -> Optional[Piece]:
        return self._occupant

    @occupant.setter
    def occupant(self, occupant: Optional[Piece]):
        self._occupant = occupant


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Square):
            return False
        return self.id == other.id and self.coordinate == other.coordinate


    def __hash__(self):
        return hash(self.id)