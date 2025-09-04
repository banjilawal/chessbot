from typing import List

from chess.board.board import Board
from chess.board.square import Square
from chess.creator.emit import id_emitter
from chess.token.model import Piece
from chess.engine.scout.scout_report import ScoutReport


class Scout:
    _scout: Piece

    def __init__(self, scout: Piece):
        self._scout = scout

    @property
    def scout(self) -> Piece:
        return self._scout


    def survey(self, chess_board: Board) -> ScoutReport:
        squares: List[Square] = []
        origin = self._scout.positions.current_coord()

        for territory in self._scout.rank.quadrants:
            for square in chess_board.iterator(origin, territory.delta):
                if not self._scout.rank.walk.is_walkable(self._scout, square.coord):
                    break
                if square.occupant is not None and square not in squares:
                    squares.append(square)
                    break
                squares.append(square)

        return ScoutReport(
            scout_report_id=id_emitter.scout_report_id,
            scout=self._scout,
            squares=squares
        )

