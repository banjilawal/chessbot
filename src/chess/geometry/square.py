from typing import Optional, TYPE_CHECKING

from chess.geometry.coordinate import Coordinate
from chess.geometry.occupation_status import OccupationStatus
from chess.piece.captivity_status import CaptivityStatus

if TYPE_CHECKING:
    from chess.piece.piece import Piece


class Square:
    _id: int
    _name: str
    _status: OccupationStatus
    _coordinate: Coordinate
    _occupant: Optional['Piece']

    def __init__(self, square_id: int, name: str, coord: Coordinate):
        if square_id < 0:
            raise ValueError("Square id cannot be negative.")
        if coord is None:
            raise ValueError("Coordinate cannot be None.")


        self._name = name
        self._id = square_id
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
    def occupant(self) -> Optional['Piece']:
        return self._occupant

    @property
    def status(self) -> OccupationStatus:
        return self._status


    @occupant.setter
    def occupant(self, piece: Optional['Piece']):
        print(f"{piece} wants to be my new occupant. Currently {self._occupant} is resident.")

        current_occupant = self._occupant

        if current_occupant is None:
            self._handle_occupation(self, OccupationStatus.IS_VACANT, piece)
        if piece.is_enemy(current_occupant):
            self._handle_occupation(self, OccupationStatus.HAS_ENEMY, piece)
        print(f"{self._coordinate} is occupied by friendly {current_occupant.label}")

        #
        #
        # if current_occupant is not None:
        #     print(f"Current occupant {current_occupant} has {current_occupant.current_position} as their address.")
        #     self._occupant = None
        #     print(f"my occupant is {self._occupant} now.")
        #
        # if piece is not None:
        #     self._occupant = piece;
        #     print(f"{self._occupant} is my new occupant.")
        #     # if self.coord not in piece.position_history:
        #     piece.add_position(self._coordinate)
        #
        # if piece is None:
        #     self._occupant = None


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


    def _handle_occupation(self, occupation_status: OccupationStatus, piece: 'Piece'):

        if occupation_status == OccupationStatus.BLOCKER:
            raise ValueError(f"{piece.label} is not allowed to occupy this blocked square.")

        if occupation_status == OccupationStatus.HAS_ENEMY:
            self._occupant.status = CaptivityStatus.PRISONER

        self._occupant = piece
        piece.add_position(self._coordinate)

