from typing import List

from chess.board.board import Board
from chess.creator.emit import id_emitter
from chess.exception.rank import BishopException
from chess.exception.walk import BishopWalkException
from chess.flow.occupy import OccupationFlow
from chess.geometry.coord import Coordinate
from chess.geometry.path import Path, Line
from chess.rank.base import Rank
from chess.geometry.quadrant import Quadrant
from chess.request.occupy import OccupationRequest
from chess.token.model import Piece


class Bishop(Rank):

    def __init__(self, name: str, letter: str, value: int, per_team: int, territories: List[Quadrant]):
        super().__init__(name=name, letter=letter, value=value, territories=territories, per_team=per_team)


    def walk(self, piece: Piece, destination: Coordinate, board: Board):
        method = "Bishop.walk"

        try:
            if not Path(piece.current_position, destination).line == Line.BISHOP:
                raise BishopWalkException(f"{method}: {BishopWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coordinate(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(request_id=id_emitter.request_id, piece=piece, square=square)
            )
        except BishopWalkException as e:
            raise BishopException(f"{method}: {BishopException.DEFAULT_MESSAGE}") from e
