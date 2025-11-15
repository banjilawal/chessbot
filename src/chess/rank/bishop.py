# src/chess/rank/bishop.py

"""
Module: chess.rank.bishop
Author: Banji Lawal
Created: 2025-07-24
version: 1.0.0
"""


from chess.piece import Piece
from chess.coord import Coord
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec
from chess.system import COLUMN_SIZE, ROW_SIZE


class Bishop(Rank):
    
    def __init__(
            self,
            id: int = RankSpec.BISHOP.id,
            name: str = RankSpec.BISHOP.name,
            letter: str = RankSpec.BISHOP.letter,
            ransom: int = RankSpec.BISHOP.ransom,
            quota: int = RankSpec.BISHOP.quota,
            quadrants: list[Quadrant] = RankSpec.BISHOP.quadrants
    ):
        super().__init(
            id=id,
            name=name,
            letter=letter,
            ransom=ransom,
            quadrants=quadrants,
            quota=quota
        )
    
    @classmethod
    def compute_span(cls, piece: Piece) -> [[Coord]]:
        origin = piece.current_position
        return [
            cls.slope_points(0, origin.column, 1, origin.row, 1),
            cls.slope_points(origin.column, COLUMN_SIZE, 1, 0, 1),
            cls.slope_points(origin.column, 0, -1, ROW_SIZE, -1),
            cls.slope_points(origin.column, COLUMN_SIZE, 1, ROW_SIZE, -1)
        ]
    
    @classmethod
    def slope_points(cls, start_x: int, end_x: int, x_step: int, end_y: int, slope: int) -> [Coord]:
        """"""
        points = []
        i = start_x
        j = (2 * slope * i) + slope
        
        while i < end_x and j < end_y:
            points.append(Coord(column=i, row=j))
            i += x_step
            j = (2 * slope * i) + slope
        return points
