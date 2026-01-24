# src/chess/rank/model/concrete/queen.py

"""
Module: chess.rank.model.concrete.queen
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.coord import Coord
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.token.model import Token
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import (
    DiagonalSpan, KnightException, KnightSpanComputationFailedException, PerpendicularSpan, Rank,
    Knight
)



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
            id: int = Persona.QUEEN.id,
            name: str = Persona.QUEEN.name,
            ransom: int = Persona.QUEEN.ransom,
            team_quota: int = Persona.QUEEN.quota,
            designation: str = Persona.QUEEN.designation,
            quadrants: List[Quadrant] = Persona.QUEEN.quadrants,
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
    def compute_span(self, token: Token) -> ComputationResult[[Coord]]:
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
    