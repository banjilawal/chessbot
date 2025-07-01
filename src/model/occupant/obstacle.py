from dataclasses import dataclass, field
from typing import Optional

from common.game_color import GameColor
from common.game_default import GameDefault
from model.cell.cell import Cell
from src.exception.exception import InvalidIdError, InvalidFigureLengthError, InvalidFigureHeightError, \
    NullSquareEntryError, OccupiedSquareEntryError, SquareOwnershipError, NoSquareToLeaveError, \
    FigureAreaBelowLimitError, SelfOccupiedSquareError

@dataclass
class Obstacle:
    MIN_LENGTH = 1
    MIN_HEIGHT = 1
    MIN_AREA = MIN_LENGTH * MIN_HEIGHT

    id: int
    length: int = field(default=GameDefault.OBSTACLE_LENGTH)
    height: int = field(default=GameDefault.OBSTACLE_HEIGHT)
    color: GameColor = field(default=GameDefault.OBSTACLE_COLOR)
    cells: tuple[tuple[Cell, ...], ...] = field(init=False, repr=False)

    def __post_init__(self):
        """Validate initialization parameters"""
        if self.id < 1:
            raise InvalidIdError("occupant id cannot be less than 1.")
        if self.length < Obstacle.MIN_LENGTH:
            raise InvalidFigureLengthError("occupant length cannot be less than 1.")
        if self.height < Obstacle.MIN_HEIGHT:
            raise InvalidFigureHeightError("occupant height cannot be less than 1.")
        if self.height * self.length < Obstacle.MIN_AREA:
            raise FigureAreaBelowLimitError("The area occupied by the occupant cannot be less than 2.")

        object.__setattr__(self, 'id', self.id)
        object.__setattr__(self, 'length', self.length)
        object.__setattr__(self, 'height', self.height)
        object.__setattr__(self, 'color', self.color)
        object.__setattr__(self, 'cells', tuple(self.length * [tuple() for _ in range(self.height)]))

        return self.cells

    def area(self):
        return self.length * self.height
    #
    # def leave_square(self):
    #     if self.square is None:
    #         raise NoSquareToLeaveError("occupant is not on a cell.. No where to leave from.")
    #     if self.square.occupant is not self:
    #         raise SquareOwnershipError("cell does not belong to this occupant you cannot leave.")
    #
    #     # cell = self.cell
    #
    #     self.square._occupant = None
    #     self.square = None
    #
    #
    #     # cell._occupant = None
    #
    # def enter_square(self, square: 'Cell'):
    #     if square is None:
    #         raise NullSquareEntryError("Cannot enter cell that does not exist.")
    #
    #     if self.square is square and square.occupant is self:
    #         raise SelfOccupiedSquareError("occupant is already on this cell.")
    #
    #     if self.square is not None:
    #         raise ValueError("you have left the old cell.")
    #
    #     if square.occupant is not None:
    #         raise OccupiedSquareEntryError("cell already occupied by another occupant you cannot enter.")
    #
    #     self.square = square
    #     square._occupant = self

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
