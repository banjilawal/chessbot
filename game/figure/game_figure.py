from dataclasses import dataclass
from typing import Optional

from game.exception.exception import InvalidIdError, InvalidFigureLengthError, InvalidFigureHeightError, \
    NullSquareEntryError, OccupiedSquareEntryError, SquareOwnershipError, NoSquareToLeaveError, \
    FigureAreaBelowLimitError, SelfOccupiedSquareError
from game.board.board_square import GameBoardSquare

@dataclass
class GameFigure:
    MINIMUM_LENGTH = 1  # public static final int
    MINIMUM_HEIGHT = 1
    MINIMUM_AREA = 2
    _id: int
    _length: int
    _height: int
    color: str = None
    _square: Optional['GameBoardSquare'] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self._id < 1:
            raise InvalidIdError("figure id cannot be less than 1.")

        if self._length < GameFigure.MINIMUM_LENGTH:
            raise InvalidFigureLengthError("figure length cannot be less than 1.")

        if self._height < GameFigure.MINIMUM_HEIGHT:
            raise InvalidFigureHeightError("figure height cannot be less than 1.")

        if self._height * self._length < GameFigure.MINIMUM_AREA:
            raise FigureAreaBelowLimitError("The area occupied by the figure cannot be less than 2.")

    @property
    def id(self):
        return self._id

    @property
    def length(self):
        return self._length

    @property
    def height(self):
        return self._height

    @property
    def square(self) -> Optional['GameBoardSquare']:
        return self._square

    def area(self):
        return self._length * self._height

    def leave_square(self):
        if self._square is None:
            raise NoSquareToLeaveError("figure is not on a square.. No where to leave from.")
        if self._square.occupant is not self:
            raise SquareOwnershipError("square does not belong to this figure you cannot leave.")

        square = self._square

        self._square._occupant = None
        self._square = None

        square._occupant = None

    def enter_square(self, square: 'GameBoardSquare'):
        if square is None:
            raise NullSquareEntryError("Cannot enter square that does not exist.")

        if self._square is square and square.occupant is self:
            raise SelfOccupiedSquareError("figure is already on this square.")

        if self._square is not None:
            raise ValueError("you have left the old square.")

        if square.occupant is not None:
            raise OccupiedSquareEntryError("square already occupied by another figure you cannot enter.")

        self._square = square
        square._occupant = self

    def enter_square(self, square: 'GameBoardSquare'):
        if square is None:
            raise NullSquareEntryError("Cannot enter square that does not exist.")
        if self._square is square and square.occupant is self:
            raise SelfOccupiedSquareError("Cannot enter the square the figure already occupies")
        if self._square is not None:
            raise SquareNotVacatedError("You have not left the old square. You cannot enter a new one.")
        if square.occupant is not None:
            raise OccupiedSquareEntryError("square already occupied by another figure you cannot enter.")
        self._square = square
        square._occupant = self
