# src/chess/rank/model/concrete/bishop/bishop.py

"""
Module: chess.rank.model.concrete.bishop.bishop
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List, Optional

from chess.token import Token
from chess.coord import Coord
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import BishopSpanComputationFailedException, DiagonalSpan, Rank, Bishop

class Bishop(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Bishop's current position.
    2.  Metadata about the Bishop rank useful for optimizing the GameGraph.

    # PARENT:
        Rank

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        * diagonal_span (DiagonalSpan)

    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _diagonal_span: DiagonalSpan
    
    def __init__(
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
    def compute_span(self, token: Token,) -> ComputationResult[[Coord]]:
        """
        # Action
            1.  Pass the occupant's current position to Rook._perpendicular_span to get the set of possible destinations.
            2.  If perpendicular_span fails send the exception chain in the ComputationResult. Else, return
                the span in the ComputationResult's payload.
        # PARAMETERS:
            *   occupant (Token)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   RookException
            *   RookSpanComputationFailedException
        """
        method = "Bishop.compute_span"
        
        # --- Compute the Bishop's possible destinations. ---#
        computation_result = self._diagonal_span.compute(
            points=[],
            origin=token.current_position,
            coord_service=self.coord_service
        )
        # Handle the case that spanning set computation does not produce a solution.
        if computation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                BishopSpanComputationFailedException(
                    message=f"{method}: {BishopSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=computation_result.exception
                )
            )
        # Put the completed Bishop's span into a ComputationResult and send to the caller.
        return computation_result