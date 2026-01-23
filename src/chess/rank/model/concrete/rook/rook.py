# src/chess/rank/model/concrete/rook/rook.py

"""
Module: chess.rank.model.concrete.rook.rook
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""
from collections.abc import coroutine
from typing import List, Optional

from chess.persona import Persona
from chess.geometry import Quadrant
from chess.coord import Coord, CoordService
from chess.system import ChessException, ComputationResult, LoggingLevelRouter
from chess.rank import RookSpanComputationFailedException, PerpendicularSpan, Rank, Rook
from chess.token import Token, TokenService


class Rook(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Rook's current position.
    2.  Metadata about the Rook rank useful for optimizing the GameGraph.

    # PARENT:
        Rank

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        * perpendicular_span (PerpendicularSpan)

    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _perpendicular_span: PerpendicularSpan
    
    def __init__(
            self,
            id: int,
            name: str = Persona.ROOK.name,
            ransom: int = Persona.ROOK.ransom,
            team_quota: int = Persona.ROOK.quota,
            designation: str = Persona.ROOK.designation,
            quadrants: List[Quadrant] = List[Persona.ROOK.quadrants],
            perpendicular_span: PerpendicularSpan = PerpendicularSpan(),
            coord_service: CoordService = CoordService(),
    ):
        super().__init__(
            id=id,
            name=name,
            ransom=ransom,
            team_quota=team_quota,
            designation=designation,
            quadrants=quadrants,
            vectors=None,
            coord_service=coroutine
        )
        self._perpendicular_span = perpendicular_span
    
    @LoggingLevelRouter.monitor
    def compute_span(self, token: Token) -> ComputationResult[[Coord]]:
        """
        # Action
            1.  If the origin is not certified safe send an exception chain in the ComputationResult.
            2.  Add origin to each vector in Rook.vectors to get the spanning set. If any of the
                additions fails send an exception chain in the ComputationResult.
            3.  Send the set of points to the caller in the ComputationReslt's payload.
        # PARAMETERS:
            *   origin (Coord)
            *   coord_service (CoordService)

        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   RookSpanComputationFailedException
        """
        method = "Rook.compute_span"
        
        # # Handle the case that the token is both safe and actionable.
        # actionable_token_verification_result = token_service.verify_token_is_actionable(token=token)
        # if actionable_token_verification_result.is_failure:
        #     # Return the exception chain on failure.
        #     return ComputationResult.failure(
        #         RookSpanComputationFailedException(
        #             message=f"{method}: {RookSpanComputationFailedException.DEFAULT_MESSAGE}",
        #             ex=actionable_token_verification_result.exception
        #         )
        #     )
        # --- Compute the Rook's possible destinations. ---#
        computation_result = self._perpendicular_span.compute(
            points=[],
            origin=token.current_position,
            coord_service=self.coord_service
        )
        # Handle the case that spanning set computation does not produce a solution.
        if computation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RookSpanComputationFailedException(
                    message=f"{method}: {RookSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=computation_result.exception
                )
            )
        
        # --- The Rook's span has been successfully computed. Return in the ComputationResult's payload. ---#
        return computation_result
