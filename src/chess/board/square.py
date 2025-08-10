from typing import Optional, TYPE_CHECKING
from chess.geometry.coordinate.coordinate import Coordinate
from chess.board.occupation_status import OccupationStatus

if TYPE_CHECKING:
    from chess.token.chess_piece import ChessPiece

class Square:
    _id: int
    _name: str
    _status: 'OccupationStatus'
    _coordinate: Coordinate
    _occupant: Optional['ChessPiece']

    def __init__(self, square_id: int, name: str, coord: Coordinate):
        self._id = square_id
        self._name = name
        self._occupant = None
        self._coordinate = coord
        self._status = OccupationStatus.IS_VACANT

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
    def occupant(self) -> Optional['ChessPiece']:
        return self._occupant


    @property
    def status(self) -> 'OccupationStatus':
        return self._status


    # Removed occupy() and leave() methods. MapService will manage these.
    def set_occupant(self, piece: Optional['ChessPiece']):
        """
        Sets or clears the occupant of the square and updates its status.
        This method is intended to be called by MapService, not directly.
        """
        self._occupant = piece
        self._status = OccupationStatus.OCCUPIED_BY_SELF if piece else OccupationStatus.IS_VACANT


    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if not isinstance(other, Square): return False
        return self._id == other.id


    def __hash__(self): return hash(self._id)


    def __str__(self) -> str:
        if self._occupant:
            return f"Square ID: {self._id}, Name: {self._name}, Occupied by: {self._occupant.name} ({self._occupant.label})"
        return f"Square ID: {self._id}, Name: {self._name}, Status: {self._status.name}"


    def __repr__(self) -> str:
        occupant_repr = repr(self._occupant) if self._occupant else "None"
        return (f"Square(id={self._id}, name='{self._name}', "
                f"coordinate={repr(self._coordinate)}, "
                f"status={self._status.name}, occupant={occupant_repr})")
