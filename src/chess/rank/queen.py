# src/chess/rank/queen.py

"""
Module: chess.rank.queen
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""


from chess.piece import Piece
from chess.coord import Coord
from chess.geometry import Quadrant
from chess.system import LoggingLevelRouter
from chess.rank import Bishop, Rank, RankSpec, Rook



class Queen(Rank):
    """"""
    
    def __init__(
            self,
            id: int = RankSpec.QUEEN.id,
            name: str = RankSpec.QUEEN.name,
            designation: str = RankSpec.QUEEN.designation,
            ransom: int = RankSpec.QUEEN.ransom,
            team_quota: int = RankSpec.QUEEN.team_quota,
            quadrants: list[Quadrant] = RankSpec.QUEEN.quadrants
    ):
        super().__init(
            id=id,
            name=name,
            letter=designation,
            ransom=ransom,
            quadrants=quadrants,
            quota=team_quota
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute_span(cls, piece: Piece) -> [Coord]:
        """"""
        return [Bishop.compute_span(piece), Rook.compute_span(piece)]
