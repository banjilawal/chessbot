from typing import List, Optional

from chess.board.board import Board
from chess.creator.emit import id_emitter
from chess.exception.rank import QueenRankException
from chess.exception.walk import QueenWalkException
from chess.flow.occupy import OccupationFlow
from chess.geometry.coord import Coordinate
from chess.geometry.path import Path, Line
from chess.geometry.quadrant import Quadrant
from chess.rank.base import Rank
from chess.request.occupy import OccupationRequest
from chess.token.model import Piece


class Queen(Rank):

    def __init__(self, name: str, letter: str, value: int, per_team: int, territories: List[Quadrant]):
        super().__init__(name=name, letter=letter, value=value, territories=territories, per_team=per_team)


    def walk(self, piece: Piece, destination: Coordinate, board: Board):
        method = "Queen.walk"

        try:
            if not Path(piece.current_position, destination).line == Line.QUEEN:
                raise QueenWalkException(f"{method}: {QueenWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coordinate(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(request_id=id_emitter.request_id, piece=piece, square=square)
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
        per_team: int,
        territories: List[Quadrant],
        old_rank: Optional[str] = None
    ):
        super().__init__(name=name, letter=letter, value=value, per_team=per_team, territories=territories)
        _old_rank: old_rank


    @property
    def old_rank(self) -> Optional[str]:
        return self._old_rank




