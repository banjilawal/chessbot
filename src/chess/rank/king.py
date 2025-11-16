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
        
    @classmethod
    @LoggingLevelRouter.monitor
    def compute_span(cls, piece: Piece) -> [Coord]:
        
        origin = piece.current_position
        return [
            origin.add_vector(Vector(1, 0)),
            origin.add_vector(Vector(-1, 0)),
            origin.add_vector(Vector(0, 1)),
            origin.add_vector(Vector(1, 1)),
            origin.add_vector(Vector(-1, 1)),
            origin.add_vector(Vector(-1, -1)),
            origin.add_vector(Vector(1, -1))
        ]