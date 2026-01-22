# src/chess/rank/model/concrete/bishop/bishop.py

"""
Module: chess.rank.model.concrete.bishop.bishop
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from _ast import List

from chess.rank import BishopSpanComputationFailedException, DiagonalSpan, Rank
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
            vectors=None
        )
        self._diagonal_span = diagonal_span
    
    @LoggingLevelRouter.monitor
    def compute_span(self, origin: Coord, coord_service: CoordService = CoordService()) -> ComputationResult[[[Coord]]]:
        """
        # Action
            1.  Pass the origin and coord_service to Bishop._diagonal_span. If diagonal span returns an origin
                validation failure or some other problem, wrap the exception chain then send in the ComputationResult.
            2.  Else, the computation was successful, the span is in the payload. Forward computation_result to the 
                caller. 
        # PARAMETERS:
            *   origin (Coord)
            *   coord_service (CoordService)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   BishopSpanComputationFailedException
        """
        method = "Bishop.compute_span"
        
        computation_result = self._diagonal_span.compute(origin=origin, points=[], coord_service=coord_service)
        # Handle the case that spanning set computation does not produce a solution.
        if computation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                BishopSpanComputationFailedException(
                    message=f"{method}: {BishopSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=computation_result.exception
                )
            )
        
        # --- The Bishop's span has been successfully computed. Return in the ComputationResult's payload. ---#
        return computation_result