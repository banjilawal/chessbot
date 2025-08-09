from typing import List

from chess.board.board import ChessBoard
from chess.board.element.square import Square
from chess.creator.emit import id_emitter
from chess.geometry.coordinate.coordinate import Coordinate
from chess.token.piece import ChessPiece
from engine.scout.raw_scout_report import RawScoutReport


class Scout:
    _scout: ChessPiece

    def __init__(self, scout: ChessPiece):
        self._scout = scout

    @property
    def scout(self) -> ChessPiece:
        return self._scout


    def survey(self, chess_board: ChessBoard) -> RawScoutReport:
        squares: List[Square] = []
        origin = self._scout.coordinate_stack.current_coordinate()

        for territory in self._scout.rank.territories:
            for square in chess_board.iterator(origin, territory.delta):
                if not self._scout.rank.walk.is_walkable(self._scout, square.coordinate):
                    break
                if square.occupant is not None and square not in squares:
                    squares.append(square)
                    break
                squares.append(square)
        return RawScoutReport(
            scout_report_id=id_emitter.scout_report_id,
            scout=self._scout,
            squares=squares
        )


    def __str__(self) -> str:
        return f"Scout(scout:{self._scout.name})"

