from typing import Optional, TYPE_CHECKING

from chess.geometry.coordinate import Coordinate

if TYPE_CHECKING:
    from chess.piece.piece import Piece


class Square:
    _id: int
    _name: str
    _coordinate: Coordinate
    _occupant: Optional['Piece']

    def __init__(self, square_id: int, name: str, coordinate: Coordinate):
        if square_id < 0:
            raise ValueError("Square id cannot be negative.")
        if coordinate is None:
            raise ValueError("Coordinate cannot be None.")

        self._id = square_id
        self._name = name
        self._coordinate = coordinate
        self._occupant = None


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def coordinate(self) -> Coordinate:
        return self._coordinate


    @property
    def occupant(self) -> Optional['Piece']:
        return self._occupant


    @occupant.setter
    def occupant(self, piece: Optional['Piece']):
        self._occupant = piece


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

    def __str__(self):
        return f"square {self._id} {self.name} occupant: {self._occupant}"