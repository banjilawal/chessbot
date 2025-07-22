from dataclasses import field, dataclass
from enum import Enum, auto
from typing import Optional

from chess.common.config import BOARD_DIMENSION
from chess.figure.chess_piece import ChessPiece


@dataclass(frozen=True)
class ChessSquareCoordinate:
    row: int
    column: int
class Coordinate:
    row: int
    column: int

    def __post_init__(self):
        if self.row < 0:
            raise ValueError("Row cannot be negative")
        if self.column < 0:
            raise ValueError("Column cannot be negative")

@dataclass
class ChessSquare:
    id: int
    coordinate: Coordinate
    occupant: Optional[ChessPiece] = field(default=None)
