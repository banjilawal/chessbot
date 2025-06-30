from dataclasses import dataclass
from typing import Optional

from game.exception.exception import InvalidIdError, InvalidFigureLengthError, InvalidFigureHeightError, \
    NullSquareEntryError, OccupiedSquareEntryError, SquareOwnershipError, NoSquareToLeaveError, \
    FigureAreaBelowLimitError, SelfOccupiedSquareError

@dataclass
class Obstacle:
    MINIMUM_LENGTH = 1  # public static final int
    MINIMUM_HEIGHT = 1
    MINIMUM_AREA = 2
    id: int
    length: int
    height: int
    color: str = None
    square: Optional['Cell'] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self.id < 1:
            raise InvalidIdError("occupant id cannot be less than 1.")

        if self.length < Obstacle.MINIMUM_LENGTH:
            raise InvalidFigureLengthError("occupant length cannot be less than 1.")

        if self.height < Obstacle.MINIMUM_HEIGHT:
            raise InvalidFigureHeightError("occupant height cannot be less than 1.")

        if self.height * self.length < Obstacle.MINIMUM_AREA:
            raise FigureAreaBelowLimitError("The area occupied by the occupant cannot be less than 2.")

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
    def square(self) -> Optional['Cell']:
        return self.square

    def area(self):
        return self.length * self.height

    def leave_square(self):
        if self.square is None:
            raise NoSquareToLeaveError("occupant is not on a cell.. No where to leave from.")
        if self.square.occupant is not self:
            raise SquareOwnershipError("cell does not belong to this occupant you cannot leave.")

        # cell = self.cell

        self.square._occupant = None
        self.square = None


        # cell._occupant = None

    def enter_square(self, square: 'Cell'):
        if square is None:
            raise NullSquareEntryError("Cannot enter cell that does not exist.")

        if self.square is square and square.occupant is self:
            raise SelfOccupiedSquareError("occupant is already on this cell.")

        if self.square is not None:
            raise ValueError("you have left the old cell.")

        if square.occupant is not None:
            raise OccupiedSquareEntryError("cell already occupied by another occupant you cannot enter.")

        self.square = square
        square._occupant = self

    # def enter_square(self, cell: 'Cell'):
    #     if cell is None:
    #         raise NullSquareEntryError("Cannot enter cell that does not exist.")
    #     if self.cell is cell and cell.occupant is self:
    #         raise SelfOccupiedSquareError("Cannot enter the cell the occupant already occupies")
    #     if self.cell is not None:
    #         raise SquareNotVacatedError("You have not left the old cell. You cannot enter a new one.")
    #     if cell.occupant is not None:
    #         raise OccupiedSquareEntryError("cell already occupied by another occupant you cannot enter.")
    #     self.cell = cell
    #     cell._occupant = self
