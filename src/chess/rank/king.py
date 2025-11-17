# src/chess/rank/king.py

"""
Module: chess.rank.king
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""


from chess.piece import Piece
from chess.coord import Coord, CoordService
from chess.geometry import Quadrant
from chess.rank import Rank, Bishop, RankSpec, Rook
from chess.system import LoggingLevelRouter
from chess.vector import Vector, VectorService


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
            id: int=RankSpec.KING.id,
            name: str=RankSpec.KING.name,
            ransom: int = RankSpec.KING.ransom,
            team_quota: int = RankSpec.KING.team_quota,
            designation: str=RankSpec.KING.designation,
            quadrants: list[Quadrant]=RankSpec.KING.quadrants,
            coord_service: CoordService=CoordService(),
            vector_service: VectorService=VectorService(),
    ):
        super().__init(
            id=id,
            name=name,
            ransom=ransom,
            quota=team_quota,
            letter=designation,
            quadrants=quadrants,
            coord_service=coord_service,
            vector_service=vector_service,
        )
        
    @LoggingLevelRouter.monitor
    def compute_span(self, piece: Piece) -> [Coord]:
        """
        # BACKGROUND:
        Kings move in a radius of one square.
        # Action
        1.  Get the points in a unit circle around the origin.
        2.  Return the list.

        # PARAMETERS:
            *   piece (Piece): Single-source-of-truth for the basis of the span.

        # Returns:
        List[Coord]

        RAISES:
        None
        """
        method = "King.compute_span"
        origin = piece.current_position
        return [
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(1, 0)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(-1, 0)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(0, 1)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(1, 1)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(-1, 1)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(-1, -1)),
            self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(1, -1))
        ]