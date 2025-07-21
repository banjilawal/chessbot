from dataclasses import field
from typing import Optional

from chess.figure.chess_piece import ChessPiece




    def __post_init__(self):
        object.__setattr__(self, 'mover_id_counter', self.id)
        object.__setattr__(self, 'top_left_coordinate', self.coordinate)
        object.__setattr__(self, 'occupant', self.occupant)