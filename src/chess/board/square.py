from typing import Optional, TYPE_CHECKING

from assurance.exception.validation.piece import PieceValidationException
from assurance.validators.coord import CoordinateValidator
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from assurance.validators.piece import PieceValidator

if TYPE_CHECKING:
    from chess.geometry.coordinate.coord import Coordinate
    from chess.token.model import Piece

class Square:
    _id: int
    _name: str
    _coordinate: 'Coordinate'
    _occupant: Optional['Piece']

    """
    Square is a data-holding object that can store a ChessPiece. Ideally would have no public setters.
    That is difficult in Python. ChessBoard does not know directly about a ChessPiece.
    All fields are immutable.

    Attributes:
        _id (int): unique identifier for the square.
        _name (str): Name of square in Chess notation (e.g. "A1", "B2").
        _coordinate (Coordinate): Coordinate of the square on the ChessBoard.
        _occupant (ChessPiece): The ChessPiece occupying the square, if any.
    """

    def __init__(self, square_id: int, name: str, coordinate: 'Coordinate'):
        method = "Square.__init__()"

        """
        Creates a Square instance

        Args:
            square_id (int): id of the square, unique across the ChessBoard.
            name (str): name of the square in Chess notation (e.g. "A1", "B2").
            coordinate (Coordinate): coordinate of the square on the ChessBoard

        Raise:
            NameValidationException: If name is name fails any validators checks
            IdValidationException: If square_id fails any validators checks
            CoordinateValidationException: If coordinate fails any validators checks
        """


        id_validation = IdValidator.validate(square_id)
        if not id_validation.is_success():
            raise id_validation.exception

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise name_validation.exception

        coord_validation = CoordinateValidator.validate(coordinate)
        if not coord_validation.is_success():
            raise coord_validation.exception

        self._id = id_validation.payload
        self._name = name_validation.payload
        self._coordinate = coord_validation.payload

        self._occupant = None


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def coordinate(self) -> 'Coordinate':
        return self._coordinate


    @property
    def occupant(self) -> Optional['Piece']:
        return self._occupant


    @occupant.setter
    def occupant(self, piece: Optional['Piece']):
        method = f"Square.occupant"
        self._occupant = piece


    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if not isinstance(other, Square): return False

        return self._id == other.id


    def __hash__(self): return hash(self._id)


    def __str__(self) -> str:
        occupant_str = f"" if self._occupant is None else f" occupant:{self._occupant.name}"
        return (
            f"Square:{self._id}"
            f" Name:{self._name}"
            f"coordinate:{self._coordinate}"
            f"]"
        )