# src/chess/rank/knight.py

"""
Module: chess.rank.knight
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""


from chess.piece import Piece
from chess.coord import Coord
from chess.system import LoggingLevelRouter
from chess.vector import Vector
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec



class Knight(Rank):
    """"""
    
    def __init__(
            self,
            id: int = RankSpec.KNIGHT.id,
            name: str = RankSpec.KNIGHT.name,
            letter: str = RankSpec.KNIGHT.letter,
            ransom: int = RankSpec.KNIGHT.ransom,
            quota: int = RankSpec.KNIGHT.quota,
            quadrants: list[Quadrant] = RankSpec.KNIGHT.quadrants
    ):
        super().__init(
            id=id,
            name=name,
            letter=letter,
            ransom=ransom,
            quadrants=quadrants,
            quota=quota
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
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