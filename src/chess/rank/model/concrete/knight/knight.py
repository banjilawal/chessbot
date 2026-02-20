# src/chess/rank/model/concrete/knight/knight.py

"""
Module: chess.rank.model.concrete.knight.knight
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List, Optional

from chess.coord import Coord
from chess.vector import Vector
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.token.model import Token
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import KnightException, KnightSpanComputationFailedException, Rank, Knight

class Knight(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Knight's updated position.
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
    def compute_span(self, token: Token,) -> ComputationResult[[Coord]]:
        """
        # Action
            1.  Iterate through the Knight.vectors. Add each to occupant.current_position.
            2.  If the vector addition fails, return an exception chain in the ComputationResult. Else,
                add the resulting Coord to the span.
            3.  Put the completed span inside the ComputationResult and send to the caller.a
        # PARAMETERS:
            *   occupant (Token)
            *   coord_service (CoordService)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   KnightException
            *   KnightSpanComputationFailedException
        """
        method = "Knight.compute_span"
        
        span: List[Coord] = []
        # Iterate through the knight.vectors, adding each one to the origin to get the Knight's spanning set.
        for vector in self.vectors:
            addition_result = self.coord_service.add_vector_to_coord(coord=token.current_position, vector=vector)
            
            # Handle the case that the computation does not produce a solution.
            if addition_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    KnightException(
                        message=f"{method}: {KnightException.DEFAULT_MESSAGE}",
                        ex=KnightSpanComputationFailedException(
                            message=f"{method}: {KnightSpanComputationFailedException.DEFAULT_MESSAGE}",
                            ex=addition_result.exception
                        )
                    )
                )
            # On computation success add the coord to the span. It should not be present.
            if addition_result.payload not in span:
                span.append(addition_result.payload)
        # Put the completed Knight's span into a ComputationResult and send to the caller.
        return ComputationResult.success(span)
        