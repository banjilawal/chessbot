from dataclasses import field, dataclass

from typing import Optional

from chess.common.config import BOARD_DIMENSION
from chess.piece.chess_piece import Piece


@dataclass(frozen=True)
class Coordinate:
    row: int
    column: int

    def __post_init__(self):
        if self.row < 0:
            raise ValueError("Row cannot be negative")
        if self.column < 0:
            raise ValueError("Column cannot be negative")

    def shift(self, row_delta: int, column_delta: int) -> 'Coordinate':
        return Coordinate(row=self.row + row_delta, column=self.column + column_delta)

@dataclass
class ChessSquare:
    id: int
    coordinate: Coordinate
    occupant: Optional[Piece] = field(default=None)
