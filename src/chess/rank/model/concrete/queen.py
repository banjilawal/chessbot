# src/chess/rank/model/concrete/queen.py

"""
Module: chess.rank.model.concrete.queen
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from chess.piece import Piece

from chess.geometry import Quadrant
from chess.rank import DiagonalSpan, PerpendicularSpan, Rank, RankSpec
from chess.system import ComputationResult, LoggingLevelRouter
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
    _diagonal_span: DiagonalSpan
    _perpendicular_span: PerpendicularSpan
    
    def __init__(
            self,
            id: int = RankSpec.QUEEN.id,
            name: str = RankSpec.QUEEN.name,
            ransom: int = RankSpec.QUEEN.ransom,
            team_quota: int = RankSpec.QUEEN.quota,
            designation: str = RankSpec.QUEEN.designation,
            quadrants: list[Quadrant] = RankSpec.QUEEN.quadrants,
            diagonal_span: DiagonalSpan = DiagonalSpan(),
            perpendicular_span: PerpendicularSpan = PerpendicularSpan(),
    ):
        super().__init__(
            id=id,
            name=name,
            ransom=ransom,
            team_quota=team_quota,
            designation=designation,
            quadrants=quadrants,
        )
        self._diagonal_span = diagonal_span
        self._perpendicular_span = perpendicular_span
    
    @LoggingLevelRouter.monitor
    def compute_span(
            self,
            origin: Coord,
            coord_service: CoordService = CoordService()
    ) -> ComputationResult[[Coord]]:
        """
        """
        method = "Queen.compute_span"
        computation_result = self._perpendicular_span.compute(orgin=origin, points=[], coord_service=coord_service)
        if computation_result.is_failure:
            return ComputationResult.failure(computation_result.exception)
        span = computation_result.payload
        
        computation_result = self._diagonal_span.compute(orgin=origin, points=span, coord_service=coord_service)
        if computation_result.is_failure:
            return ComputationResult.failure(computation_result.exception)
        return ComputationResult.success(computation_result.payload)
    