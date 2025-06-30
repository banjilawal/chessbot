from dataclasses import dataclass
from typing import Optional

from game.exception.exception import InvalidIdError, InvalidFigureLengthError, InvalidFigureHeightError, \
    NullSquareEntryError, OccupiedSquareEntryError, SquareOwnershipError, NoSquareToLeaveError, \
    FigureAreaBelowLimitError, SelfOccupiedSquareError

@dataclass
class GameFigure:
    MINIMUM_LENGTH = 1  # public static final int
    MINIMUM_HEIGHT = 1
    MINIMUM_AREA = 2
    id: int
    length: int
    height: int
    color: str = None
    square: Optional['GameBoardSquare'] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self.id < 1:
            raise InvalidIdError("occupy id cannot be less than 1.")

        if self.length < GameFigure.MINIMUM_LENGTH:
            raise InvalidFigureLengthError("occupy length cannot be less than 1.")

        if self.height < GameFigure.MINIMUM_HEIGHT:
            raise InvalidFigureHeightError("occupy height cannot be less than 1.")

        if self.height * self.length < GameFigure.MINIMUM_AREA:
            raise FigureAreaBelowLimitError("The area occupied by the occupy cannot be less than 2.")

    @property
    def id(self):
        return self.id

    @property
    def length(self):
        return self.length

    @property
    def height(self):
        return self.height

    @property
    def square(self) -> Optional['GameBoardSquare']:
        return self.square

    def area(self):
        return self.length * self.height

    def leave_square(self):
        if self.square is None:
            raise NoSquareToLeaveError("occupy is not on a square.. No where to leave from.")
        if self.square.occupant is not self:
            raise SquareOwnershipError("square does not belong to this occupy you cannot leave.")

        # square = self.square

        self.square._occupant = None
        self.square = None


        # square._occupant = None

    def enter_square(self, square: 'GameBoardSquare'):
        if square is None:
            raise NullSquareEntryError("Cannot enter square that does not exist.")

        if self.square is square and square.occupant is self:
            raise SelfOccupiedSquareError("occupy is already on this square.")

        if self.square is not None:
            raise ValueError("you have left the old square.")

        if square.occupant is not None:
            raise OccupiedSquareEntryError("square already occupied by another occupy you cannot enter.")

        self.square = square
        square._occupant = self

    # def enter_square(self, square: 'GameBoardSquare'):
    #     if square is None:
    #         raise NullSquareEntryError("Cannot enter square that does not exist.")
    #     if self.square is square and square.occupant is self:
    #         raise SelfOccupiedSquareError("Cannot enter the square the occupy already occupies")
    #     if self.square is not None:
    #         raise SquareNotVacatedError("You have not left the old square. You cannot enter a new one.")
    #     if square.occupant is not None:
    #         raise OccupiedSquareEntryError("square already occupied by another occupy you cannot enter.")
    #     self.square = square
    #     square._occupant = self
