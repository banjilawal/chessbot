# src/chess/rank_name/queen.py

"""
Module: chess.rank_name.queen
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from chess.coord import Coord
from chess.piece import Piece
from chess.rank import Bishop, Rank, RankSpec, Rook


class Queen(Rank):
    """"""
    
    def __init__(self, spec: RankSpec = RankSpec.QUEEN):
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
        """"""
        return [Bishop.compute_span(piece), Rook.compute_span(piece)]
