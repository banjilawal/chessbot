# src/chess/rank/rook.py

"""
Module: chess.brank.rook
Author: Banji Lawal
Created: 2025-07-28
version: 1.0.0
"""

from chess.coord import Coord
from chess.piece import Piece
from chess.rank import Rank, RankSpec
from chess.system import COLUMN_SIZE


class Rook(Rank):
    
    def __init__(self, spec: RankSpec = RankSpec.BISHOP):
        super().__init__(
            id=spec.id,
            name=spec.name,
            letter=spec.letter,
            ransom=spec.ransom,
            quadrants=spec.quadrants,
            quota=spec.quota
        )
    
    @classmethod
    def compute_span(cls, piece: Piece) -> [Coord]:
        origin = piece.current_position
        return [
            cls._compute_scan_helper(0, origin.column, 1, origin.row, origin.row, 0),
            cls._compute_scan_helper(origin.column, COLUMN_SIZE, 1, origin.row, origin.row, 0),
            cls._compute_scan_helper(origin.column, origin.column, 0, 0, origin.row, 1),
            cls._compute_scan_helper(origin.column, origin.column, 0, origin.row, COLUMN_SIZE, 1)
        ]
    
    @classmethod
    def _compute_scan_helper(
            cls,
            start_x: int,
            end_x: int,
            x_step: int,
            start_y: int,
            end_y: int,
            y_step: int
    ) -> [Coord]:
        """"""
        i = start_x
        j = start_y
        
        points = [Coord]
        while i < end_x and j < end_y:
            points.append(Coord(column=i, row=j))
            i += x_step
            j += y_step
        return points