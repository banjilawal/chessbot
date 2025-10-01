
from chess.piece import Piece
from chess.coord import Coord
from chess.geometry import Path
from chess.rank import Rank, RankSpec
from chess.board.board import Board
from chess.common.emitter import id_emitter



class Bishop(Rank):

    def __init__(self, spec: RankSpec=RankSpec.BISHOP):
        super().__init__(
            name=spec.name,
            letter=spec.letter,
            ransom=spec.ransom,
            quadrants=spec.quadrants,
            quota=spec.quota
        )


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "Bishop.walk"
        try:
            if piece.current_position is None:
                raise PieceCoordNullException(f"{method}: {PieceCoordNullException.DEFAULT_MESSAGE}")

            path = Path(piece.current_position, destination)
            if not path.is_diagonal():
                raise BishopWalkException(f"{method}: {BishopWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            request = OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            OccupationFlow.enter(request=request, board=board)
        except BishopWalkException as e:
            raise BishopException(f"{method}: {BishopException.DEFAULT_MESSAGE}") from e
