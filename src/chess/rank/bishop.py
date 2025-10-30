from typing import List

from chess.piece import Piece
from chess.coord import Coord
from chess.geometry import Path, Quadrant
from chess.rank import Rank, RankSpec
from chess.board.board import Board
from chess.system import COLUMN_SIZE, ROW_SIZE


class Bishop(Rank):
    
    def __init__(self, spec: RankSpec = RankSpec.BISHOP):
        super().__init__(
            id=spec.id,
            name=spec.name,
            letter=spec.letter,
            ransom=spec.ransom,
            quadrants=spec.quadrants,
            quota=spec.quota
        )
    
    @classmethod
    def compute_span(cls, origin: Coord) -> [[Coord]]:
        return [
            cls._compute_scan_helper(0, origin.column, 1, origin.row, 1),
            cls._compute_scan_helper(origin.column, COLUMN_SIZE, 1, 0, 1),
            cls._compute_scan_helper(origin.column, 0, -1, ROW_SIZE, -1),
            cls._compute_scan_helper(origin.column, COLUMN_SIZE, 1, ROW_SIZE, -1)
        ]
    
    @classmethod
    def _compute_scan_helper(cls, start_x: int, end_x: int, x_step: int, end_y: int, slope: int) -> [Coord]:
        """"""
        points = []
        i = start_x
        j = (2 * slope * i) + slope
        
        while i < end_x and j < end_y:
            points.append(Coord(i, j))
            i += x_step
            j = (2 * slope * i) + slope
        return points
    
    def walk(self, piece: Piece, destination: Coord, board: Board):
        """"""
        pass
        # method = "Bishop.walk"
        # try:
        #     if piece.current_position is None:
        #         raise PieceCoordNullException(f"{method}: {PieceCoordNullException.DEFAULT_MESSAGE}")
        #
        #     path = Path(piece.current_position, destination)
        #     if not path.is_diagonal():
        #         raise BishopWalkException(f"{method}: {BishopWalkException.DEFAULT_MESSAGE}")
        #
        #     square = board.find_square_by_coord(destination)
        #     request = OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
        #     OccupationFlow.enter(request=request, board=board)
        # except BishopWalkException as e:
        #     raise BishopException(f"{method}: {BishopException.DEFAULT_MESSAGE}") from e
