from chess.board.board import Board
from chess.rank.profile import RankProfile
from chess.common.emit import id_emitter
from chess.exception.rank_exception import QueenRankException
from chess.exception.walk import QueenWalkException
from chess.flow.occupy import OccupationFlow
from chess.coord import Coord
from chess.geometry.path import Path, Line
from chess.geometry.quadrant import Quadrant
from chess.rank.rank import Rank
from chess.system.send import OccupationRequest
from chess.piece.piece import Piece


class Queen(Rank):

    def __init__(
        self,
        name:str=RankProfile.QUEEN.name,
        letter:str=RankProfile.QUEEN.letter,
        value:int=RankProfile.QUEEN.value,
        per_side:int=RankProfile.QUEEN.per_side,
        quadrants:[Quadrant]=RankProfile.QUEEN.quadrants
    ):
        super().__init__(name=name, letter=letter, value=value, quadrants=quadrants, per_side=per_side)


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "Queen.walk"

        try:
            if not Path(piece.current_position, destination).line == Line.QUEEN:
                raise QueenWalkException(f"{method}: {QueenWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            )
        except QueenWalkException as e:
            raise QueenRankException(f"{method}: {QueenRankException.DEFAULT_MESSAGE}") from e






