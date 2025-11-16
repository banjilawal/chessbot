# src/chess/rank/rook.py

"""
Module: chess.rank.rook
Author: Banji Lawal
Created: 2025-07-28
version: 1.0.0
"""


from chess.piece import Piece
from chess.coord import Coord
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec
from chess.system import COLUMN_SIZE, LoggingLevelRouter





class Rook(Rank):
    
    def __init__(
            self,
            id: int = RankSpec.ROOK.id,
            name: str = RankSpec.ROOK.name,
            designation: str = RankSpec.ROOK.designation,
            ransom: int = RankSpec.ROOK.ransom,
            team_quota: int = RankSpec.ROOK.team_quota,
            quadrants: list[Quadrant] = RankSpec.ROOK.quadrants
    ):
        super().__init(
            id=id,
            name=name,
            letter=designation,
            ransom=ransom,
            quadrants=quadrants,
            quota=team_quota
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute_span(cls, piece: Piece) -> [Coord]:
        origin = piece.current_position
        return [
            cls.slope_points(0, origin.column, 1, origin.row, origin.row, 0),
            cls.slope_points(origin.column, COLUMN_SIZE, 1, origin.row, origin.row, 0),
            cls.slope_points(origin.column, origin.column, 0, 0, origin.row, 1),
            cls.slope_points(origin.column, origin.column, 0, origin.row, COLUMN_SIZE, 1)
        ]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def slope_points(
            cls,
            start_x: int,
            end_x: int,
            x_step: int,
            start_y: int,
            end_y: int,
            y_step: int
    ) -> [Coord]:
        """"""
        i = start_x
        j = start_y
        
        points = [Coord]
        while i < end_x and j < end_y:
            points.append(Coord(column=i, row=j))
            i += x_step
            j += y_step
        return points