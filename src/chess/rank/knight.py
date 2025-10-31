# src/chess/rank/knight.py

"""
Module: chess.rank.knight
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from chess.coord import Coord
from chess.piece import Piece
from chess.rank import Rank, RankSpec
from chess.vector import Vector


class Knight(Rank):
    """"""
    
    def __init__(self, spec: RankSpec = RankSpec.KNIGHT):
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
        origin = piece.current_position
        return [
            origin.add_vector(Vector(1, 2)),
            origin.add_vector(Vector(-1, 2)),
            origin.add_vector(Vector(1, -2)),
            origin.add_vector(Vector(-1, -2)),
            origin.add_vector(Vector(2, 1)),
            origin.add_vector(Vector(2, -1)),
            origin.add_vector(Vector(-2, 1)),
            origin.add_vector(Vector(-2, -1))
        ]