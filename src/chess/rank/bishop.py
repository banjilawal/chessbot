# src/chess/rank/bishop.py

"""
Module: chess.rank.bishop
Author: Banji Lawal
Created: 2025-07-24
version: 1.0.0
"""

from chess.piece import Piece
from chess.coord import Coord
from chess.rank import Rank, RankSpec
from chess.system import COLUMN_SIZE, ROW_SIZE


class Bishop(Rank):
    
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
    def compute_span(cls, piece: Piece) -> [[Coord]]:
        origin = piece.current_position
        return [
            cls._compute_scan_helper(0, origin.column, 1, origin.row, 1),
            cls._compute_scan_helper(origin.column, COLUMN_SIZE, 1, 0, 1),
            cls._compute_scan_helper(origin.column, 0, -1, ROW_SIZE, -1),
            cls._compute_scan_helper(origin.column, COLUMN_SIZE, 1, ROW_SIZE, -1)
        ]
    
    @classmethod
    def _compute_scan_helper(cls, start_x: int, end_x: int, x_step: int, end_y: int, slope: int) -> [Coord]:
        """"""
        points = []
        i = start_x
        j = (2 * slope * i) + slope
        
        while i < end_x and j < end_y:
            points.append(Coord(column=i, row=j))
            i += x_step
            j = (2 * slope * i) + slope
        return points
