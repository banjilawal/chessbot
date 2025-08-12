from typing import Optional, TYPE_CHECKING

from assurance.validation.coordinate_specification import CoordinateSpecification
from assurance.validation.id_specification import IdSpecification
from assurance.validation.validation_exception import IdValidationException, CoordinateValidationException

from chess.exception.null.null import NullNameException
from chess.geometry.coordinate.coordinate import Coordinate

if TYPE_CHECKING:
    from chess.token.chess_piece import ChessPiece

class Square:
    _id: int
    _name: str
    _coordinate: Coordinate
    _occupant: Optional['ChessPiece']

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

    def __init__(self, square_id: int, name: str, coordinate: Coordinate):
        method = "Square.__init__()"

        """
        Creates a Square instance

        Args:
            square_id (int): id of the square, unique across the ChessBoard.
            name (str): name of the square in Chess notation (e.g. "A1", "B2").
            coordinate (Coordinate): coordinate of the square on the ChessBoard

        Raise:
            NullNameException: If name is null
            IdValidationException: If id fails validation checks for non-null and positive.
            CoordinateValidationException: If coordinate is null, its row or colum are out of bounds
        """

        if name is None:
            raise NullNameException(NullNameException.default_message)

        if not IdSpecification.is_satisfied_by(id):
            raise IdValidationException(IdValidationException.default_message)

        if not CoordinateSpecification.is_satisfied_by(coordinate):
            raise CoordinateValidationException(CoordinateValidationException.default_message)

        self._id = square_id
        self._name = name
        self._occupant = None
        self._coordinate = coordinate

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


    @occupant.setter
    def occupant(self, chess_piece: Optional['ChessPiece']):
        method = f"Square.occupant"
        self._occupant = chess_piece


    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if not isinstance(other, Square): return False
        return self._id == other.id


    def __hash__(self): return hash(self._id)


    def __str__(self) -> str:
        if self._occupant is not None:
            return (
                f"Square ID: {self._id}"
                f", Name: {self._name}"
                f", Occupied by: {self._occupant.name}"
            )
        return (
            f"Square ID:{self._id} "
            f"Name:{self._name} "
            f"coordinate:{self._coordinate} "
        )


    def __repr__(self) -> str:
        occupant_repr = repr(self._occupant) if self._occupant else "None"
        return (f"Square(id={self._id}, name='{self._name}', "
                f"coordinate={repr(self._coordinate)}, "
                f"occupant={occupant_repr})")
