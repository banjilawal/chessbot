from typing import List

from chess.board.board import Board
from chess.config.rank import RankProfile
from chess.creator.emit import id_emitter
from chess.exception.rank import BishopException
from chess.exception.walk import BishopWalkException
from chess.flow.occupy import OccupationFlow

from chess.geometry.coord import Coord
from chess.geometry.path import Path, Line
from chess.rank.base import Rank
from chess.geometry.quadrant import Quadrant
from chess.request.occupy import OccupationRequest
from chess.token.model import Piece


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
            path = Path(piece.current_position, destination)
            if not path.is_diagonal():
                raise BishopWalkException(f"{method}: {BishopWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            )
        except BishopWalkException as e:
            raise BishopException(f"{method}: {BishopException.DEFAULT_MESSAGE}") from e
