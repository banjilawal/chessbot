# src/chess/rank_name/king.py

"""
Module: chess.rank_name.king
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from chess.coord import Coord
from chess.piece import Piece
from chess.rank import Bishop, Rank, RankSpec, Rook


class King(Rank):
    
    def __init__(self, spec: RankSpec = RankSpec.KING):
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
        return [cls._diagonal_span_helper(origin), cls._horizontal_helper(origin)]
    
    @classmethod
    def _diagonal_span_helper(cls, origin: Coord) -> [[Coord]]:
        return [
            Bishop._compute_scan_helper(origin.column-1, origin.column, 1, origin.row, 1),
            Bishop._compute_scan_helper(origin.column, origin.column+1, 1, 0, 1),
            Bishop._compute_scan_helper(origin.column, origin.column-1, -1, origin.row+1, -1),
            Bishop._compute_scan_helper(origin.column, origin.column+1, 1, origin.row+1, -1)
        ]
        
    @classmethod
    def _horizontal_helper(cls, origin: Coord) -> [Coord]:
        return [
            Rook._compute_scan_helper(origin.column-1, origin.column, 1, origin.row, origin.row, 0),
            Rook._compute_scan_helper(origin.column, origin.column+1, 1, origin.row, origin.row, 0),
            Rook._compute_scan_helper(origin.column, origin.column, 0, origin.row-1, origin.row, 1),
            Rook._compute_scan_helper(origin.column, origin.column, 0, origin.row, origin.row+1, 1)
        ]