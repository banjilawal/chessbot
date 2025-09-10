from typing import Optional, TYPE_CHECKING, cast

from chess.geometry.validator.coord_validator import CoordValidator
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from chess.creator.emit import id_emitter
from chess.geometry.coord import Coord

if TYPE_CHECKING:
    # from chess.geometry.coord import Coord
    from chess.piece.piece import Piece

class Square:
    _id:int
    _name:str
    _coord:Coord
    _occupant:Optional['Piece']

    """
    Square is a data-holding object that can store a ChessPiece. Ideally would have no public setters.
    That is difficult in Python. ChessBoard does not know directly about a ChessPiece.
    All fields are immutable.

    Attributes:
        _id (int):unique identifier for the square.
        _name (str):Name of square in Chess notation (e.g. "A1", "B2").
        _coord (Coord):Coord of the square on the ChessBoard.
        _occupant (ChessPiece):The ChessPiece occupying the square, if any.
    """

    def __init__(self, square_id:int, name:str, coord:Coord):
        method = "Square.__init__"

        """
        Creates a Square instance

        Args:
            square_id (int):id of the square, unique across the ChessBoard.
            name (str):name of the square in Chess notation (e.g. "A1", "B2").
            coord (Coord):coord of the square on the ChessBoard

        Raise:
            NameValidationException:If name is name fails any validators checks
            IdValidationException:If square_id fails any validators checks
            CoordValidationException:If coord fails any validators checks
        """


        id_validation = IdValidator.validate(square_id)
        if not id_validation.is_success():
            raise id_validation.exception

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise name_validation.exception

        coord_validation = CoordValidator.validate(coord)
        if not coord_validation.is_success():
            raise coord_validation.exception

        self._id = cast(int, id_validation.payload)
        self._name = cast(str, name_validation.payload)
        self._coord = cast(Coord, coord_validation.payload)

        self._occupant = None


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def coord(self) -> Coord:
        return self._coord


    @property
    def occupant(self) -> Optional['Piece']:
        return self._occupant


    @occupant.setter
    def occupant(self, piece:Optional['Piece']):
        method = f"Square.occupant"

        from chess.piece.piece import Piece
        if piece is not None and not isinstance(piece, Piece):
            raise TypeError(f"{method}:Expected a Piece, got {type(piece).__name__}")

        self._occupant = piece


    def __eq__(self, other):
        if other is self:return True
        if other is None:return False
        if not isinstance(other, Square):return False

        return self._id == other.id


    def __hash__(self):return hash(self._id)


    def __str__(self) -> str:
        occupant_str = f"" if self._occupant is None else f" occupant:{self._occupant.name}"
        return f"Square:[{self._id} {self._name} {self._coord}{occupant_str}]"



def main():

    square = Square(square_id=id_emitter.square_id, name="A1", coord=Coord(row=0, column=0))
    print(square)


if __name__ == "__main__":
    main()