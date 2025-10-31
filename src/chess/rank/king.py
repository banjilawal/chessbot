from chess.board.board import Board
from chess.coord import Coord
from chess.piece import Piece
from chess.rank import Bishop, Rank, RankSpec, Rook


class King(Rank):
    
    def __init__(self, spec: RankSpec = RankSpec.KING):
        super().__init__(
            id=spec.id,
            name=spec.name,
            letter=spec.letter,
            ransom=spec.ransom,
            quadrants=spec.quadrants,
            quota=spec.quota
        )
        
    @classmethod
    def compute_span(cls, origin: Coord) -> [Coord]:
        return [cls._diagonal_span_helper(origin), cls._horizontal_helper(origin)]
    
    @classmethod
    def _diagonal_span_helper(cls, origin: Coord) -> [[Coord]]:
        return [
            Bishop._compute_scan_helper(origin.column-1, origin.column, 1, origin.row, 1),
            Bishop._compute_scan_helper(origin.column, origin.column+1, 1, 0, 1),
            Bishop._compute_scan_helper(origin.column, origin.column-1, -1, origin.row+1, -1),
            Bishop._compute_scan_helper(origin.column, origin.column+1, 1, origin.row+1, -1)
        ]
        
    @classmethod
    def _horizontal_helper(cls, origin: Coord) -> [Coord]:
        return [
            Rook._compute_scan_helper(origin.column-1, origin.column, 1, origin.row, origin.row, 0),
            Rook._compute_scan_helper(origin.column, origin.column+1, 1, origin.row, origin.row, 0),
            Rook._compute_scan_helper(origin.column, origin.column, 0, origin.row-1, origin.row, 1),
            Rook._compute_scan_helper(origin.column, origin.column, 0, origin.row, origin.row+1, 1)
        ]
        
    @classmethod
    def walk(cls, piece: Piece, destination: Coord, board: Board):
        pass
        # method = "King.walk"
        #
        # try:
        #   if not Path(piece.current_position, destination).line == Line.KING:
        #     raise KingWalkException(f"{method}: {KingWalkException.DEFAULT_MESSAGE}")
        #
        #   square = board.find_square_by_coord(destination)
        #   OccupationFlow.enter(
        #     board=board,
        #     request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
        #   )
        # except KingWalkException as e:
        #   raise KingException(f"{method}: {KingException.DEFAULT_MESSAGE}") from e
