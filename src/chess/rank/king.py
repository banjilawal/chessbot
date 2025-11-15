# src/chess/rank/king.py

"""
Module: chess.rank.king
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""


from chess.piece import Piece
from chess.coord import Coord
from chess.geometry import Quadrant
from chess.rank import Rank, Bishop, RankSpec, Rook
from chess.system import LoggingLevelRouter


class King(Rank):
    
    def __init__(
            self,
            id: int=RankSpec.KING.id,
            name: str=RankSpec.KING.name,
            letter: str=RankSpec.KING.letter,
            ransom: int=RankSpec.KING.ransom,
            quota: int=RankSpec.KING.quota,
            quadrants: list[Quadrant]=RankSpec.KING.quadrants
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
    @LoggingLevelRouter.monitor
    def compute_span(cls, piece: Piece, bishop: Bishop=Bishop(), rook: Rook=Rook()) -> [Coord]:
        
        origin = piece.current_position
        return [
            cls._diagonal_span_helper(origin=origin, bishop=bishop),
            cls._horizontal_helper(origin=origin, rook=rook)
        ]
    
    @classmethod
    @LoggingLevelRouter
    def _diagonal_span_helper(cls, origin: Coord, bishop: Bishop=Bishop()) -> [[Coord]]:
        return [
            bishop.slope_points(
                start_x=origin.column - 1, end_x=origin.column, x_step=1, end_y=origin.row, slope=1
            ),
            Bishop.slope_points(
                start_x=origin.column, end_x=origin.column + 1, x_step=1, end_y=0, slope=1
            ),
            Bishop.slope_points(
                start_x=origin.column, end_x=origin.column - 1, x_step=-1, end_y=origin.row + 1, slope=-1
            ),
            Bishop.slope_points(
                start_x=origin.column, end_x=origin.column + 1, x_step=1, end_y=origin.row + 1, slope=-1
            )
        ]
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _horizontal_helper(cls, origin: Coord, rook: Rook=Rook()) -> [Coord]:
        return [
            rook.slope_points(
                start_x=origin.column - 1, end_x=origin.column, x_step=1,
                start_y=origin.row, end_y=origin.row, y_step=0
            ),
            rook.slope_points(
                start_x=origin.column, end_x=origin.column + 1, x_step=1,
                start_y=origin.row, end_y=origin.row, y_step=0
            ),
            rook.slope_points(
                start_x=origin.column, end_x=origin.column, x_step=0,
                start_y=origin.row - 1, end_y=origin.row, y_step=1
            ),
            rook.slope_points(
                start_x=origin.column, end_x=origin.column, x_step=0,
                start_y=origin.row, end_y=origin.row + 1, y_step=1
            )
        ]