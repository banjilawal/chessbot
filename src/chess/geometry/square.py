from typing import Optional, TYPE_CHECKING

from chess.geometry.coordinate import Coordinate
from chess.geometry.occupation_status import OccupationStatus
from chess.piece.mobility_status import MobilityStatus
from chess.transaction.failure import Failure
from chess.transaction.status_code import StatusCode
from chess.transaction.transaction_result import TransactionResult

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

    def occupy(self, piece: 'Piece') -> TransactionResult:
        method = "Square.occupy"

        if self._occupant == piece:
            self.status = OccupationStatus.OCCUPIED_BY_SELF
            print(f"{piece.label} is already occupying {self._coordinate} nohing to do")
            return TransactionResult(method, StatusCode.SUCCESS)

        if self._status == OccupationStatus.BLOCKED:
            return TransactionResult(method, Failure(f"Square is blocked by friendly {self._occupant.label}"))

        if self._occupant is None:
            return self._handle_occupation(OccupationStatus.IS_VACANT, piece)

        if piece.is_enemy(self._occupant):
            return self._handle_occupation(OccupationStatus.HAS_ENEMY, piece)

        return TransactionResult(method, Failure(f"Occupation failed after mutation"))


    def leave(self, piece: 'Piece') -> TransactionResult:
        method = "Square.leave"

        if self._occupant is None:
            return TransactionResult(method, Failure(f"{piece.label} cCannot leave a square already vacant"))

        if self._occupant != piece:
            return TransactionResult(method, Failure(f"C{piece.lable} is not the current occupant of {self._coordinate}"))

        self._occupant = None
        self._status = OccupationStatus.IS_VACANT

        if self._occupant is None and piece.current_position() == self._coordinate:
            return TransactionResult(method, StatusCode.SUCCESS)
        else:
            return TransactionResult(method, Failure(f"Leave failed after mutation"))


    @occupant.setter
    def occupant(self, piece: Optional['Piece']):
        print(f"{piece} wants to be my new occupant. Currently {self._occupant} is resident.")

        current_occupant = self._occupant

        if current_occupant is None:
            self._handle_occupation(self, OccupationStatus.IS_VACANT, piece)
        if piece.is_enemy(current_occupant):
            self._handle_occupation(self, OccupationStatus.HAS_ENEMY, piece)
        print(f"{self._coordinate} is occupied by friendly {current_occupant.label}")



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
            self._occupant.status = MobilityStatus.PRISONER

        self._occupant = piece
        piece.add_position(self._coordinate)

