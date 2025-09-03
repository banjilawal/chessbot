from typing import List

from chess.board.board import ChessBoard
from chess.exception.walk import KingWalkException
from chess.flow.occupy import OccupationFlow
from chess.geometry.coord import Coordinate
from chess.geometry.path import Line, Path
from chess.geometry.quadrant import Quadrant
from chess.rank.queen import PromotedQueen
from chess.request.occupy import OccupationRequest
from chess.token.model.base import Piece


class KingRank(PromotedQueen):

    def __init__(self, name: str, letter: str, value: int, per_team: int, territories: List[Quadrant]):
        super().__init__(name=name, letter=letter, value=value, territories=territories, per_team=per_team)


    def walk(self, piece: Piece, destination: Coordinate, board: ChessBoard):
        method = "KingRank.walk"

        if not Path(piece.current_position, destination).line == Line.KING:
            raise KingWalkException(f"{method}: {KingWalkException.DEFAULT_MESSAGE}")

        square = board.find_square_by_coordinate(destination)
        OccupationFlow.enter(
            board=board,
            request=OccupationRequest(request_id=id_emitter.request_id, piece=piece, square=square)
        )