# src/chess/rank/rook.py

"""
Module: chess.rank.rook
Author: Banji Lawal
Created: 2025-07-28
version: 1.0.0
"""


from chess.piece import Piece
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec
from chess.coord import Coord, CoordService
from chess.system import COLUMN_SIZE, LoggingLevelRouter





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
    def __init__(
            self,
            id: int = RankSpec.ROOK.id,
            name: str = RankSpec.ROOK.name,
            designation: str = RankSpec.ROOK.designation,
            ransom: int = RankSpec.ROOK.ransom,
            team_quota: int = RankSpec.ROOK.team_quota,
            quadrants: list[Quadrant] = RankSpec.ROOK.quadrants,
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
    def compute_span(self, piece: Piece) -> [Coord]:
        """
        # Action
        1.  Call compute_perpendicular_span. to get the horizontal and vertical points
            in the Rook's range.

        # PARAMETERS:
            *   piece (Piece): Single-source-of-truth for the basis of the span.

        # Returns:
        List[Coord]

        RAISES:
        None
        """
        method = "Rook.compute_span"
        return self.compute_perpendicular_span(piece)