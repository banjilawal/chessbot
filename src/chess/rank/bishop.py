from chess.board.board import Board
from chess.rank.profile import RankProfile
from chess.common.emitter import id_emitter


from chess.action.types import OccupationFlow

from chess.coord import Coord
from chess.geometry.path import Path
from chess.rank.rank import Rank
from chess.geometry.quadrant import Quadrant
from chess.action.send import OccupationRequest
from chess.piece.piece import Piece


class Bishop(Rank):

    def __init__(
        self,
        name:str=RankProfile.BISHOP.name,
        letter:str=RankProfile.BISHOP.letter,
        value:int=RankProfile.BISHOP.value,
        per_side:int=RankProfile.BISHOP.per_side,
        quadrants:[Quadrant]=RankProfile.BISHOP.quadrants
    ):
        super().__init__(name=name, letter=letter, value=value, quadrants=quadrants, per_side=per_side)


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
