from dataclasses import dataclass
from typing import Optional

from game.common.game_constant import GameConstant
from game.exception.exception import InvalidIdError, NegativeRowError, NegativeColumnError
from game.model.occupy.game_figure import GameFigure


@dataclass
class GameBoardSquare:
    id: int
    row: int
    column: int
    occupant: Optional['GameFigure'] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self.id < GameConstant.MINIMUM_ID:
            raise InvalidIdError("GameBoardSquare id below minimum value.")
        if self.row < 0:
            raise NegativeRowError("GameBoardSquare cannot be on a negative row.")
        if self.column < 0:
            raise NegativeColumnError("GameBoardSquare cannot be on a negative column.")

    @property
    def occupant(self) -> Optional['GameFigure']:
        return self.occupant

    @property
    def occupied(self) -> bool:
        return self._occupant is not None

    def __repr__(self) -> str:
        status = f"Occupied by {self.occupant}" if self.occupied else "Empty"
        return f"Square({self.row}, {self.column}) - {status}"
