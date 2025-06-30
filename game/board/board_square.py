from dataclasses import dataclass
from itertools import count
from typing import Optional, List

import pygame

from game.common.game_constant import GameConstant
from game.exception.exception import InvalidIdError, NegativeRowError, NegativeColumnError, InvalidNumberOfRowsError, \
    InvalidNumberOfColumnsError
from game.occupy.game_figure import GameFigure


@dataclass
class GameBoardSquare:
    _id: int
    _row: int
    _column: int
    _occupant: Optional['GameFigure'] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self._id < GameConstant.MINIMUM_ID:
            raise InvalidIdError("GameBoardSquare id below minimum value.")
        if self._row < 0:
            raise NegativeRowError("GameBoardSquare cannot be on a negative row.")
        if self._column < 0:
            raise NegativeColumnError("GameBoardSquare cannot be on a negative column.")

    @property
    def occupant(self) -> Optional['GameFigure']:
        return self._occupant

    @property
    def occupied(self) -> bool:
        return self._occupant is not None

    def __repr__(self) -> str:
        status = f"Occupied by {self._occupant}" if self.occupied else "Empty"
        return f"Square({self._row}, {self._column}) - {status}"
