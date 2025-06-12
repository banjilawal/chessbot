from typing import List, Union, Optional
from dataclasses import dataclass
from typing import Optional
from game.board.board_square import GameBoardSquare

@dataclass
class GameFigure:
    id: int
    width: int
    length: int
    color: str = None
    _square: Optional['GameBoardSquare'] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self.id < 1:
            raise ValueError("piece id cannot be less than 1.")
        if self.length < 1:
            raise ValueError("piece length cannot be less than 1.")
        if self.width < 1:
            raise ValueError("piece width cannot be less than 1.")

    @property
    def square(self) -> Optional['GameBoardSquare']:
        return self._sqaure

    def leave_square(self):
        if self._square is None:
            raise ValueError("piece is not on a square.")
        if self._square.occupant is not self:
            raise ValueError("piece is not on this square.")

        self._square.occupant = None
        self._square = None

        square = self._square
        square._occupant = None

    def enter_square(self, square: 'GameBoardSquare'):
        if self._square is not None:
            raise ValueError("piece is already on a square.")
        if square.occupant is not None:
            raise ValueError("square already occupied.")
        self._square = square
        square._occupant = self