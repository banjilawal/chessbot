# src/chess/rank/model/concrete/knight.py

"""
Module: chess.rank.model.concrete.knight
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""
from typing import List

from chess.piece import Piece
from chess.coord import Coord, CoordService
from chess.persona import Persona
from chess.system import LoggingLevelRouter
from chess.vector import Vector
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec



class Knight(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Knight's current position.
    2.  Metadata about the Knight rank useful for optimizing the GameGraph.

    # PROVIDES:
    Knight

    # ATTRIBUTES:
    See super class
    """
    
    def __init__(
            self,
            id: int,
            name: str = Persona.KNIGHT.name,
            ransom: int = Persona.KNIGHT.ransom,
            team_quota: int = Persona.KNIGHT.quota,
            designation: str = Persona.KNIGHT.designation,
            quadrants: List[Quadrant] = List[Persona.KNIGHT.quadrants],
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
    def compute_span(self, piece: Piece) -> [Coord]:
        """
        # BACKGROUND:
        Knights can move 2 steps on any axis, then a diagonal step.
        # Action
        1.  Go through each of the 8 possible moves and add them to the span.
        2.  Return the list.

        # PARAMETERS:
            *   piece (Token): Single-source-of-truth for the basis of the span.

        # RETURNS:
        List[Coord]

        RAISES:
        None
        """
        method = "Knight.compute_span"
        
        origin = token.current_position
        return [
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(1, 2)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(-1, 2)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(1, -2)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(-1, -2)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(2, 1)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(2, -1)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(-2, 1)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(-2, -1))
        ]