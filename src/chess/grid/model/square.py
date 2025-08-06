from typing import Optional, TYPE_CHECKING
from chess.geometry.coordinate.coordinate import Coordinate
from chess.grid.model.occupation_status import OccupationStatus
from chess.team.model.mobility_status import MobilityStatus

if TYPE_CHECKING:
    from chess.team.model.piece import ChessPiece


class Square:
    _id: int
    _name: str
    _status: OccupationStatus
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
    def occupant(self):
        return self._occupant

    @property
    def status(self) -> OccupationStatus:
        return self._status

    def occupy(self, piece: 'ChessPiece'):
        method = "Square.occupy"

        if self._occupant == piece:
            self._status = OccupationStatus.OCCUPIED_BY_SELF
            print(f"{piece.name} is already occupying {self._coordinate} nothing to do")

        if self._status == OccupationStatus.BLOCKED:
            print(f"Square is blocked by friendly {self._occupant.label}")

        if self._occupant is None:
            self._handle_occupation(OccupationStatus.IS_VACANT, piece)

        if piece.is_enemy(self._occupant):
            self._handle_occupation(OccupationStatus.HAS_ENEMY, piece)



    def leave(self, piece: 'ChessPiece'):
        method = "Square.leave"

        if self._occupant is None:
            print(f"{piece.name} cCannot leave a model already vacant")

        if self._occupant != piece:
           print(f"C{piece.name} is not the current occupant of {self._coordinate}")

        self._occupant = None
        self._status = OccupationStatus.IS_VACANT

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Square):
            return False
        return self._id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self) -> str:
        # if self._occupant is None:
        occupant_str = f"occupant:{self._occupant.name}" if self._occupant else "vacant"
        return f"Square[id:{self._id} name:{self.name} coordinate:{self._coordinate} {occupant_str}]"
        # return f"model {self._id} {self.name} is occupied by {self._occupant.name}"

    def __repr__(self) -> str:
        """
        Provides an unambiguous string representation, useful for debugging.
        This method is crucial for how objects appear when printed as part of a list.
        """
        occupant_repr = repr(self._occupant) if self._occupant else "None"
        return (f"Square(id={self._id}, name='{self._name}', "
                f"coordinate={repr(self._coordinate)}, "
                f"status={self._status.name}, occupant={occupant_repr})")

    def _handle_occupation(self, occupation_status: OccupationStatus, chess_piece: 'ChessPiece'):
        method = "Square._handle_occupation"

        if occupation_status == OccupationStatus.BLOCKED:
            print(f"{chess_piece.name} is not allowed to occupy this blocked model.")

        if occupation_status == OccupationStatus.HAS_ENEMY:
            self._occupant.status = MobilityStatus.PRISONER

        self._occupant = chess_piece
        chess_piece.coordinate_stack.push_coordinate(self._coordinate)
        self._status = occupation_status
        # print(
        #     f"{self._coordinate} is occupied by friendly {self._occupant.name} status:{self._status} "
        #     f"stack_size:{self._occupant.coordinate_stack.size()}"
        # )
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
    #     print(f"{self._coordinate} is occupied by friendly {current_occupant.name}")












