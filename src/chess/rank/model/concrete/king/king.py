# src/chess/rank/model/concrete/king/king.py

"""
Module: chess.rank.model.concrete.king.king
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.coord import Coord, CoordService
from chess.geometry import Quadrant
from chess.persona import Persona
from chess.rank import Rank, King
from chess.system import ComputationResult, LoggingLevelRouter
from chess.vector import Vector


class King(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a King's current position.
    2.  Metadata about the King rank useful for optimizing the GameGraph.

    # PROVIDES:
    King

    # ATTRIBUTES:
    See super class
    """
    
    def __init__(
            self,
            id: int,
            name: str = Persona.KING.name,
            ransom: int = Persona.KING.ransom,
            team_quota: int = Persona.KING.quota,
            designation: str = Persona.KING.designation,
            quadrants: List[Quadrant] = List[Persona.KING.quadrants],
    ):
        super().__init__(
            id=id,
            name=name,
            ransom=ransom,
            team_quota=team_quota,
            designation=designation,
            quadrants=quadrants,
        )
    
    @LoggingLevelRouter.monitor
    def compute_span(
            self, 
            origin: Coord, 
            coord_service: CoordService = CoordService()
    ) -> ComputationResult[[Coord]]:
        """
        """
        method = "King.compute_span"
        # Handle the case that the coord is not certified safe.
        coord_validation_result = coord_service.validate_coord(coord=origin)
        if coord_validation_result.is_failure:
        
        
        span: [Coord] = []
        vectors = [
            Vector(1, 0), Vector(-1, 0), Vector(0, 1),  Vector(1, 1),  Vector(-1, 1), 
            Vector(-1, -1), Vector(1, -1)
        ]

        for vector in vectors:
            result = coord_service.add_vector_to_coord(coord=origin, vector=vector)
            if result.is_failure:
                return ComputationResult.failure(result.exception)
            if result.payload not in span:
                span.append(result.payload)
        return ComputationResult.success(span)