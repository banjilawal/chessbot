# src/chess/rank/model/concrete/king/king.py

"""
Module: chess.rank.model.concrete.king.king
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List, Optional

from chess.vector import Vector
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.coord import Coord
from chess.token import Token
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import KingSpanComputationFailedException, Rank, King


class King(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a King's current position.
    2.  Metadata about the King rank useful for optimizing the GameGraph.
    
    # PARENT:
        Rank

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """

    def __init__(
            self,
            id: int,
            name: str = Persona.KING.name,
            ransom: int = Persona.KING.ransom,
            team_quota: int = Persona.KING.quota,
            designation: str = Persona.KING.designation,
            quadrants: List[Quadrant] = List[Persona.KING.quadrants],
            vectors: Optional[List[Vector]] = List[Persona.KING.quadrants],
    ):
        super().__init__(
            id=id,
            name=name,
            ransom=ransom,
            team_quota=team_quota,
            designation=designation,
            quadrants=quadrants,
            vectors=vectors,
        )
    
    @LoggingLevelRouter.monitor
    def compute_span(self, token: Token,) -> ComputationResult[[Coord]]:
        """
        # Action
            1.  If the origin is not certified safe send an exception chain in the ComputationResult.
            2.  Add origin to each vector in King.vectors to get the spanning set. If any of the
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
            *   KingSpanComputationFailedException
        """
        method = "King.compute_span"
        #
        # # Handle the case that the token is both safe and actionable.
        # actionable_token_verification_result = token_service.verify_token_is_actionable(token=token)
        # if actionable_token_verification_result.is_failure:
        #     # Return the exception chain on failure.
        #     return ComputationResult.failure(
        #         KingSpanComputationFailedException(
        #             message=f"{method}: {KingSpanComputationFailedException.DEFAULT_MESSAGE}",
        #             ex=actionable_token_verification_result.exception
        #         )
        #     )

        # Iterate through the vectors, adding each to the king's position to get the King's spanning set.
        span: List[Coord] = []
        for vector in self.vectors:
            addition_result = self.coord_service.add_vector_to_coord(coord=token.current_position, vector=vector)
            
            # Handle the case that the computation does not produce a solution.
            if addition_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    KingSpanComputationFailedException(
                        message=f"{method}: {KingSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=addition_result.exception
                    )
                )
            # Otherwise add the coord to the span.
            if addition_result.payload not in span:
                span.append(addition_result.payload)
                
        # --- The King's span has been successfully computed. Return in the ComputationResult's payload. ---#
        return ComputationResult.success(span)