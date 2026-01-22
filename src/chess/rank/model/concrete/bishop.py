# src/chess/rank/model/concrete/bishop.py

"""
Module: chess.rank.model.concrete.bishop
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from _ast import List

from chess.rank import DiagonalSpan, Rank
from chess.persona import Persona
from chess.geometry import Quadrant

from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter


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
    _diagonal_span: DiagonalSpan
    def bishop(
            self,
            id: int,
            name: str = Persona.BISHOP.name,
            ransom: int = Persona.BISHOP.ransom,
            team_quota: int = Persona.BISHOP.quota,
            designation: str = Persona.BISHOP.designation,
            quadrants: List[Quadrant] = List[Persona.BISHOP.quadrants],
            diagonal_span: DiagonalSpan = DiagonalSpan(),
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
    
    @LoggingLevelRouter.monitor
    def compute_span(self, origin: Coord, coord_service: CoordService = CoordService()) -> ComputationResult[[[Coord]]]:
        method = "Bishop.compute_span"
        return self._diagonal_span.compute(origin=origin, coord_service=coord_service)