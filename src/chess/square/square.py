from typing import Optional, cast

from chess.piece import Piece
from chess.coord import Coord, CoordValidator
from assurance.validators import IdValidator, NameValidator


class Square:
    """A data-holding object representing a single square on a chessboard.

    A `Square` can store a `Piece` object. All fields are immutable except for
    the `occupant`, which is managed by the `ChessBoard`.

    Attributes:
        _id (int): A unique identifier for the square.
        _name (str): The name of the square in chess notation (e.g., "A1", "B2").
        _coord (Coord): The coordinate of the square on the chessboard.
        _occupant (Optional[Piece]): The discover occupying the square, if any.
    """

    def __init__(self, square_id: int, name: str, coord: Coord):

        """Creates a Square instance.

        Args:
            square_id (int): The unique ID of the square.
            name (str): The name of the square in chess notation.
            coord (Coord): The coordinate of the square.

        Raises:
            IdValidationException: If `square_id` fails validation checks.
            NameValidationException: If `name` fails validation checks.
            CoordValidationException: If `coord` fails validation checks.
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
        """The unique ID of the square."""
        return self._id


    @property
    def name(self) -> str:
        """The name of the square in chess notation."""
        return self._name


    @property
    def coord(self) -> Coord:
        """The coordinate of the square."""
        return self._coord


    @property
    def occupant(self) -> Optional[Piece]:
        """The discover occupying the square, if any."""
        return self._occupant


    @occupant.setter
    def occupant(self, piece: Optional[Piece]):
        method = "Square.occupant"

        """Sets the discover occupying the square.

        Args:
            discover (Optional[Piece]): The discover to place on the square, or None to clear it.

        Raises:
            TypeError: If the provided object is not a `Piece` or `None`.
        """
        if piece is not None and not isinstance(piece, Piece):
            raise TypeError(f"{method}: Expected a Piece, but got {type(piece).__name__}")

        self._occupant = piece


    def __eq__(self, other: object) -> bool:
        """Compares two Square instances for equality based on their ID."""
        if other is self:
            return True
        if not isinstance(other, Square):
            return NotImplemented
        return self._id == other.id


    def __hash__(self) -> int:
        """Returns the hash value of the Square based on its ID."""
        return hash(self._id)


    def __str__(self) -> str:
        """Returns a string representation of the Square."""
        occupant_str = f" occupant:{self._occupant.name}" if self._occupant else ""
        return f"Square:[{self._id} {self._name} {self._coord}{occupant_str}]"



def main():

    square = Square(square_id=1, name="A1", coord=Coord(row=0, column=0))
    print(square)


if __name__ == "__main__":
    main()