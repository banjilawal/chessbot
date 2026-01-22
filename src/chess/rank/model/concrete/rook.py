# src/chess/rank/model/concrete/rook.py

"""
Module: chess.rank.model.concrete.rook
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""
from typing import List

from chess.geometry import Quadrant
from chess.persona import Persona
from chess.rank import PerpendicularSpan, Rank
from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter





class Rook(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Rook's current position.
    2.  Metadata about the Rook rank useful for optimizing the GameGraph.

    # PROVIDES:
    Rook

    # ATTRIBUTES:
    See super class
    """
    _perpendicular_span: PerpendicularSpan
    
    def __init__(
            self,
            id: int,
            name: str = Persona.ROOK.name,
            designation: str = Persona.ROOK.designation,
            ransom: int = Persona.ROOK.ransom,
            team_quota: int = Persona.ROOK.quota,
            quadrants: List[Quadrant] = List[Persona.ROOK.quadrants],
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
        self._perpendicular_span = perpendicular_span
    
    def compute_span(
            self,
            origin: Coord,
            coord_service: CoordService = CoordService()
    ) -> ComputationResult[[Coord]]:
        """
        """
        method = "Rook.compute_span"
        return self._perpendicular_span.compute(orgin=origin, points=[], coord_service=coord_service)
