# src/chess/rank/model/concrete/knight/knight.py

"""
Module: chess.rank.model.concrete.knight.knight
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List, Optional

from chess.token import TokenService
from chess.token.model import Token
from chess.vector import Vector
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.coord import Coord, CoordService
from chess.system import ChessException, ComputationResult, LoggingLevelRouter
from chess.rank import KnightSpanComputationFailedException, Rank, Knight


class Knight(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Knight's current position.
    2.  Metadata about the Knight rank useful for optimizing the GameGraph.

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
            name: str = Persona.KNIGHT.name,
            ransom: int = Persona.KNIGHT.ransom,
            team_quota: int = Persona.KNIGHT.quota,
            designation: str = Persona.KNIGHT.designation,
            quadrants: List[Quadrant] = List[Persona.KNIGHT.quadrants],
            vectors: Optional[List[Vector]] = List[Persona.KNIGHT.quadrants],
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
    def compute_span(
            self,
            token: Token,
            token_service: TokenService = TokenService(),
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[[[Coord]]]:
        """
        # Action
            1.  If the origin is not certified safe send an exception chain in the ComputationResult.
            2.  Add origin to each vector in Knight.vectors to get the spanning set. If any of the
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
            *   KnightSpanComputationFailedException
        """
        method = "Knight.compute_span"
        
        # # Handle the case that the coord is not certified safe.
        # coord_validation = coord_service.validator.validate(candidate=origin)
        # if coord_validation.is_failure:
        #     # On failure return the exception chain
        #     return ComputationResult.failure(
        #         KnightSpanComputationFailedException(
        #             message=f"{method}: {KnightSpanComputationFailedException.DEFAULT_MESSAGE}",
        #             ex=coord_validation.exception
        #         )
        #     )
        if not token.is_active:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                KnightSpanComputationFailedException(
                    message=f"{method}: {KnightSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ChessException()
                )
            )
        
        # Iterate through the vectors, adding each one to the origin to get the Knight's spanning set.
        span: List[Coord] = []
        for vector in self.vectors:
            # Handle the case that the computation does not produce a solution.
            result = coord_service.add_vector_to_coord(coord=token.current_position, vector=vector)
            # Return the exception chain on failure.
            if result.is_failure:
                return ComputationResult.failure(result.exception)
            # Otherwise add the coord to the span.
            if result.payload not in span:
                span.append(result.payload)
        
        # --- The Knight's span has been successfully computed. Return in the ComputationResult's payload. ---#
        return ComputationResult.success(span)
        