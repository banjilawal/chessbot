from chess.board import Board
from chess.coord import Coord
from chess.piece import Piece
from chess.rank import Bishop, Rank, RankSpec, Rook
from chess.system import ROW_SIZE


class Queen(Rank):
    
    def __init__(self, spec: RankSpec = RankSpec.QUEEN):
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
        return [Bishop.compute_span(origin), Rook.compute_span(origin)]
    
    def walk(self, piece: Piece, destination: Coord, board: Board):
        """"""
        pass
        # method = "Queen.walk"
        #
        # try:
        #   if not Path(piece.current_position, destination).line == Line.QUEEN:
        #     raise QueenWalkException(f"{method}: {QueenWalkException.DEFAULT_MESSAGE}")
        #
        #   square = board.find_square_by_coord(destination)
        #   OccupationFlow.enter(
        #     board=board,
        #     request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
        #   )
        # except QueenWalkException as e:
        #   raise QueenRankException(f"{method}: {QueenRankException.DEFAULT_MESSAGE}") from e
