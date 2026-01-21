# src/chess/rank/model/concrete/queen.py

"""
Module: chess.rank.model.concrete.queen
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from chess.piece import Piece

from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec
from chess.system import LoggingLevelRouter
from chess.coord import Coord, CoordService




class Queen(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Queen's current position.
    2.  Metadata about the Queen rank.

    # PROVIDES:
    Queen

    # ATTRIBUTES:
    See super class
    """
    
    def __init__(
            self,
            id: int = RankSpec.QUEEN.id,
            name: str = RankSpec.QUEEN.name,
            ransom: int = RankSpec.QUEEN.ransom,
            team_quota: int = RankSpec.QUEEN.quota,
            designation: str = RankSpec.QUEEN.designation,
            quadrants: list[Quadrant] = RankSpec.QUEEN.quadrants,
            coord_service: CoordService = CoordService()
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
    def compute_span(self, piece: Piece) -> [Coord]:
        """
        # Action
        Call compute_diagonal_span and compute_perpendicular_span to get vertical,
        horizontal and diagonal points in the Queen's range.

        
        # PARAMETERS:
            *   piece (Token): Single-source-of-truth for the basis of the span.
        
        # RETURNS:
        List[Coord]
        
        RAISES:
        None
        """
        method = "Queen.compute_span"
        return [self.compute_diagonal_span(piece), self.compute_perpendicular_span(piece)]
