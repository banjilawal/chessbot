# src/chess/rank/model/concrete/queen/queen.py

"""
Module: chess.rank.model.concrete.queen.queen
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.rank.model.concrete.queen import QueenException
from chess.token import Token
from chess.coord import Coord
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import PerpendicularSpan, QueenSpanComputationFailedException, DiagonalSpan, Rank, Queen

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
            quadrants: List[Quadrant] = List[Persona.QUEEN.quadrants],
            perpendicular_span: PerpendicularSpan = PerpendicularSpan(),
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
        self._perpendicular_span = perpendicular_span
    
    @LoggingLevelRouter.monitor
    def compute_span(self, token: Token) -> ComputationResult[[Coord]]:
        """
        # Action
            1.  If Queen.diagonal_span fails send an exception chain in the Computation result. Else
                get the perpendicular span.
            2.  If Queen.perpendicular_span fails send an exception chain in the Computation result.
            3.  Make a set of unique points of the perpendicular spans and send it in the ComputationResult.
        # PARAMETERS:
            *   token (Token)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   RookException
            *   RookSpanComputationFailedException
        """
        method = "Queen.compute_span"
        
        # Compute the Queen's destinations that are perpendicular.
        perpendicular_result = self._perpendicular_span.compute(
            points=[],
            orgin=token.current_position,
            coord_service=self.coord_service,
        )
        # Handle the case that the perpendicular spanning set computation does not produce a solution.
        if perpendicular_result.is_failure:
            return ComputationResult.failure(
                QueenException(
                    f"{method}: {QueenException.DEFAULT_MESSAGE}",
                    ex=QueenSpanComputationFailedException(
                        f"{method}: {QueenException.DEFAULT_MESSAGE}",
                        ex=perpendicular_result.exception,
                    )
                )
            )
        # Compute the Queen's destinations that are diagonal.
        diagonal_result = self._diagonal_span.compute(
            points=[],
            orgin=token.current_position,
            coord_service=self.coord_service,
        )
        # Handle the case that the diagonal spanning set computation does not produce a solution.
        if diagonal_result.is_failure:
            return ComputationResult.failure(
                QueenException(
                    f"{method}: {QueenException.DEFAULT_MESSAGE}",
                    ex=QueenSpanComputationFailedException(
                        f"{method}: {QueenException.DEFAULT_MESSAGE}",
                        ex=diagonal_result.exception,
                    )
                )
            )
        # Put cast the set of unique points to a List then return to the caller in a ComputationResult.
        span = cast(List, list(set(diagonal_result.payload + perpendicular_result.payload)))
        return ComputationResult.success(span)
        
    