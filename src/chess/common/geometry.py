from dataclasses import field
from typing import Optional

from chess.figure.chess_piece import ChessPiece


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
