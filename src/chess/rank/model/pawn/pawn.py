# src/chess/rank/model/pawn/pawn.py

"""
Module: chess.rank.model.pawn.pawn
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""
from typing import List

from chess.coord import Coord, CoordService
from chess.pawn import PawnPiece
from chess.geometry import Quadrant
from chess.rank import PawnMovingException, Rank, RankSpec
from chess.system import LoggingLevelRouter, Result
from chess.vector import Vector


class Pawn(Rank):
    """
    # ROLE: Computation, Metadata
  
    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Pawn's current position.
    2.  Metadata about the Pawn rank.
  
    # PROVIDES:
    Queen
  
    # ATTRIBUTES:
    See super class
    """
    
    def __init__(
            self,
            id: int = RankSpec.PAWN.id,
            name: str = RankSpec.PAWN.name,
            ransom: int = RankSpec.PAWN.ransom,
            team_quota: int = RankSpec.PAWN.quota,
            designation: str = RankSpec.PAWN.designation,
            quadrants: list[Quadrant] = RankSpec.PAWN.quadrants,
            coord_service: CoordService = CoordService()
    ):
        super().__init(
            id=id,
            name=name,
            ransom=ransom,
            quota=team_quota,
            letter=designation,
            quadrants=quadrants,
            coord_service=coord_service,
        )
    
    @LoggingLevelRouter.monitor
    def compute_span(self, piece: PawnPiece) -> [Coord]:
        """
        # Action
        1.  If piece.positions.size() == 1, then we are in an opening move. Call _opening_span.
            Otherwise, call _developed_span.
        2.  Return the list.
    
        # PARAMETERS:
            *   piece (Token): Single-source-of-truth for the basis of the span.
    
        # RETURNS:
        List[Coord]
    
        RAISES:
        None
        """
        method = "Pawn.compute_span"
        
        origin = piece.current_position
        if piece.positions.size() == 1:
            return self._opening_span(origin)
        return self._developed_span(origin)
    
@LoggingLevelRouter.monitor
def _compute_developed_span(self, origin: Coord) -> [Coord]:
    """
    # BACKGROUND:
    Any opening moves develop by
        *   Advancing one square_name forward.
        *   Attacking one square_name forward then one diagonal square_name.

    # Action
    1.  Call  by adding a vector of (0,1) to the origin.
    2.  Get the set attackable positions by adding (-1,1), (1,1) to the origin.
    3.  Return the 3 points to the span.

    # PARAMETERS:
        *   origin (Coord):

    # RETURNS:
    List[Coord]

    RAISES:
    None
    """
    method = "Pawn._compute_developed_span"
    return [
        # Forward position
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=0, y=1)),
        # Queen-side attacking position
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=-1, y=1)),
        # King-side attacking position
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=1, y=1))
    ]

@LoggingLevelRouter
def _compute_opening_span(self, origin: Coord) -> [Coord]:
    """
    # BACKGROUND:
    Any opening moves develop by
        *   Advancing either one or two squares forward.
        *   Attacking either one or two squares forward then one diagonal square_name.

    # Action
    1.  Get the opening forward position by adding a vector of (0,2) to the origin.
    2.  Get the set opening attackable positions by adding (-1,2), (1,2) to the origin.
    3.  Call _developed_span to get the remaining opening destinations.
    4.  Return the 6 points to the span.

    # PARAMETERS:
        *   origin (Coord):

    # RETURNS:
    List[Coord]

    RAISES:
    None
    """
    method = "Pawn._compute_opening_span"
    return [
        # Get destination of 2 step advance.
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=0, y=2)),
        # Get 2 step queen-side attack destination.
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=-1, y=2)),
        # Get 2 step king-side attack destination.
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=1, y=2)),
        # Add points in developed move.
        self._compute_developed_span(origin),
    ]
