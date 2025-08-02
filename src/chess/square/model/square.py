from typing import Optional, TYPE_CHECKING

from chess.common.exceptions import NegativeIdException
from chess.geometry.board.board_exception import MissingCoordinateException
from chess.geometry.board.coordinate import Coordinate
from chess.square.model.occupation_status import OccupationStatus
from chess.piece.mobility_status import MobilityStatus
from chess.transaction.failure import Failure
from chess.transaction.status_code import StatusCode
from chess.transaction.old_transaction_result import OldTransactionResult
from chess.geometry.board.coordinate_validator import CoordinateValidator
from assurance.validation.id_validator import IdValidator

if TYPE_CHECKING:
    from chess.piece.piece import ChessPiece


class Square:
    _id: int
    _name: str
    _status: OccupationStatus
    _coordinate: Coordinate
    _occupant: Optional['ChessPiece']

    def __init__(self, square_id: int, name: str, coord: Coordinate):
        id_validation_result = IdValidator.test_id_positive(square_id)
        if id_validation_result.is_failure:
            raise NegativeIdException(NegativeIdException.default_message)

        coordinate_validation_result = CoordinateValidator.coordinate_exists(coord)
        if coordinate_validation_result.is_failure:
            raise MissingCoordinateException(MissingCoordinateException.default_message)

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
    def occupant(self) -> Optional['ChessPiece']:
        return self._occupant

    @property
    def status(self) -> OccupationStatus:
        return self._status

    def occupy(self, piece: 'ChessPiece') -> OldTransactionResult:
        method = "Square.occupy"

        if self._occupant == piece:
            self.status = OccupationStatus.OCCUPIED_BY_SELF
            print(f"{piece.label} is already occupying {self._coordinate} nohing to do")
            return OldTransactionResult(method, StatusCode.SUCCESS)

        if self._status == OccupationStatus.BLOCKED:
            return OldTransactionResult(method, Failure(f"Square is blocked by friendly {self._occupant.label}"))

        if self._occupant is None:
            return self._handle_occupation(OccupationStatus.IS_VACANT, piece)

        if piece.is_enemy(self._occupant):
            return self._handle_occupation(OccupationStatus.HAS_ENEMY, piece)

        return OldTransactionResult(method, Failure(f"Occupation failed after mutation"))


    def leave(self, piece: 'ChessPiece') -> OldTransactionResult:
        method = "Square.leave"

        if self._occupant is None:
            return OldTransactionResult(method, Failure(f"{piece.label} cCannot leave a model already vacant"))

        if self._occupant != piece:
            return OldTransactionResult(
                method,
                Failure(f"C{piece.lable} is not the current occupant of {self._coordinate}")
            )

        self._occupant = None
        self._status = OccupationStatus.IS_VACANT

        if self._occupant is None and piece.current_coordinate() == self._coordinate:
            return OldTransactionResult(method, StatusCode.SUCCESS)
        else:
            return OldTransactionResult(method, Failure(f"Leave failed after mutation"))

    #
    # @occupant.setter
    # def occupant(self, chess_piece: Optional['ChessPiece']):
    #     print(f"{chess_piece} wants to be my new occupant. Currently {self._occupant} is resident.")
    #
    #     current_occupant = self._occupant
    #
    #     if current_occupant is None:
    #         self._handle_occupation(self, OccupationStatus.IS_VACANT, chess_piece)
    #     if chess_piece.is_enemy(current_occupant):
    #         self._handle_occupation(self, OccupationStatus.HAS_ENEMY, chess_piece)
    #     print(f"{self._coordinate} is occupied by friendly {current_occupant.label}")



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
        return f"model {self._id} {self.name} occupant: {self._occupant}"


    def _handle_occupation(self, occupation_status: OccupationStatus, chess_piece: 'ChessPiece') -> OldTransactionResult:
        method = "Square._handle_occupation"

        if occupation_status == OccupationStatus.BLOCKER:
            OldTransactionResult(method, Failure(f"{chess_piece.label} is not allowed to occupy this blocked model."))

        if occupation_status == OccupationStatus.HAS_ENEMY:
            self._occupant.status = MobilityStatus.PRISONER

        self._occupant = chess_piece
        chess_piece.push_new_coordinate(self._coordinate)

        if self._coordinate == chess_piece.current_coordinate():
            return OldTransactionResult(method, StatusCode.SUCCESS)

        return OldTransactionResult(method, Failure(f"Occupation failed after mutation"))


