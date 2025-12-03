# src/chess/rank/model/knight/knight.py

"""
Module: chess.rank.model.knight.knight
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""


from chess.piece import Piece
from chess.coord import Coord, CoordIntegrityService
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
            id: int = RankSpec.KNIGHT.id,
            name: str = RankSpec.KNIGHT.name,
            ransom: int = RankSpec.KNIGHT.ransom,
            team_quota: int = RankSpec.KNIGHT.team_quota,
            designation: str = RankSpec.KNIGHT.designation,
            quadrants: list[Quadrant] = RankSpec.KNIGHT.quadrants,
            coord_service: CoordIntegrityService=CoordIntegrityService()
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
    def compute_span(self, piece: Piece) -> [Coord]:
        """
        # BACKGROUND:
        Knights can move 2 steps on any axis, then a diagonal step.
        # Action
        1.  Go through each of the 8 possible moves and add them to the span.
        2.  Return the list.

        # PARAMETERS:
            *   piece (Piece): Single-source-of-truth for the basis of the span.

        # Returns:
        List[Coord]

        RAISES:
        None
        """
        method = "Knight.compute_span"
        
        origin = piece.current_position
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