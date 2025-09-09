from typing import List, Optional

from chess.board.board import Board
from chess.config.rank import RankProfile
from chess.creator.emit import id_emitter
from chess.exception.rank import QueenRankException
from chess.exception.walk import QueenWalkException
from chess.flow.occupy import OccupationFlow
from chess.geometry.coord import Coord
from chess.geometry.path import Path, Line
from chess.geometry.quadrant import Quadrant
from chess.rank.base import Rank
from chess.system.send import OccupationRequest
from chess.token.model import Piece


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

class PromotedQueen(Queen):
    _old_rank: Optional[str]

    def __init__(
        self,
        name: str,
        letter: str,
        value:int,
        per_side: int,
        quadrants: List[Quadrant],
        old_rank: Optional[str] = None
    ):
        super().__init__(name=name, letter=letter, value=value, per_side=per_side, quadrants=quadrants)
        _old_rank: old_rank


    @property
    def old_rank(self) -> Optional[str]:
        return self._old_rank




