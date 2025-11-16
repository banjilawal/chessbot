# src/chess/rank/bishop.py

"""
Module: chess.rank.bishop
Author: Banji Lawal
Created: 2025-07-24
version: 1.0.0
"""


from chess.piece import Piece
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec
from chess.coord import Coord, CoordService
from chess.system import COLUMN_SIZE, LoggingLevelRouter, ROW_SIZE


class Bishop(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Bishop's current position.
    2.  Metadata about the Bishop rank useful for optimizing the GameGraph.

    # PROVIDES:
    Bishop

    # ATTRIBUTES:
    See super class
    """
    
    def __init__(
            self,
            id: int = RankSpec.BISHOP.id,
            name: str = RankSpec.BISHOP.name,
            ransom: int = RankSpec.BISHOP.ransom,
            team_quota: int = RankSpec.BISHOP.team_quota,
            designation: str = RankSpec.BISHOP.designation,
            quadrants: list[Quadrant] = RankSpec.BISHOP.quadrants,
            coord_service: CoordService = CoordService(),
    ):
        super().__init(
            id=id,
            name=name,
            ransom=ransom,
            quota=team_quota,
            letter=designation,
            quadrants=quadrants,
            coord_service=coord_service,
        )
    
    @LoggingLevelRouter.monitor
    def compute_span(self, piece: Piece) -> [[Coord]]:
        return self.compute_diagonal_span(piece)