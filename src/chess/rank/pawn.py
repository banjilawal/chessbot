from typing import List

from chess.board.board import ChessBoard
from chess.creator.emit import id_emitter
from chess.exception.rank import PawnRankException
from chess.exception.walk import PawnWalkException
from chess.flow.occupy import OccupationFlow
from chess.geometry.coord import Coordinate
from chess.geometry.path import Path, Line
from chess.geometry.quadrant import Quadrant
from chess.rank.queen import PromotedQueen
from chess.request.occupy import OccupationRequest
from chess.token.model.base import Piece


class PawnRank(PromotedQueen):

    def __init__(self, name: str, letter: str, value: int, per_team: int, territories: List[Quadrant]):
        super().__init__(name=name, letter=letter, value=value, territories=territories, per_team=per_team)


    def walk(self, piece: Piece, destination: Coordinate, board: ChessBoard):
        method = "PawnRank.walk"

        try:
            if not (
                self._is_opening(piece, destination) or
                self._is_advance(piece, destination) or
                self._is_attack(piece, destination)
            ):
                raise PawnWalkException(f"{method}: {PawnWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coordinate(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(request_id=id_emitter.request_id, piece=piece, square=square)
            )
        except PawnWalkException as e:
            raise PawnRankException(f"{method}: {PawnRankException.DEFAULT_MESSAGE}") from e



    def _is_opening(self, piece: Piece, destination: Coordinate):
        return piece.positions.size() == 1 and Path(piece.current_position, destination).line == Line.PAWN_OPENING


    def _is_advance(self, piece: Piece, destination: Coordinate):
        return piece.positions.size() >= 1 and Path(piece.current_position, destination).line == Line.PAWN_ADVANCE


    def _is_attack(self, piece: Piece, destination: Coordinate):
        return piece.positions.size() >= 1 and Path(piece.current_position, destination).line == Line.PAWN_ATTACK

