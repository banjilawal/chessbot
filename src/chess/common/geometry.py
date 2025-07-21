from dataclasses import field, dataclass
from enum import Enum, auto
from typing import Optional

from chess.common.config import BOARD_DIMENSION
from chess.figure.chess_piece import ChessPiece

class HomeOrientation(Enum):
    NORTH = "North"
    SOUTH = "South"

    def first_home_row(self):
        if self == HomeOrientation.NORTH:
            return 0
        return BOARD_DIMENSION - 1

    def enemy_orientation(self):
        if self == HomeOrientation.NORTH:
            return HomeOrientation.SOUTH
        return HomeOrientation.NORTH

    def step_toward_enemy(self):
        if self == HomeOrientation.NORTH:
            return -1
        return 1


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
