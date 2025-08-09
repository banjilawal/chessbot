from typing import List

from chess.creator.emit import id_emitter
from chess.geometry.coordinate.coordinate import Coordinate
from chess.board.square_iterator import SquareIterator
from chess.token.piece import ChessPiece
from engine.scout.scout_report import ScoutReport


class Scout:
    _scout: ChessPiece

    def __init__(self, scout: ChessPiece):
        self._scout = scout

    @property
    def scout(self) -> ChessPiece:
        return self._scout


    def survey(self) -> ScoutReport:
        locations: List[Coordinate] = []
        origin = self._scout.coordinate_stack.current_coordinate()

        for delta in self._scout.rank.delta:
            square_iterator = SquareIterator(origin, delta)

            for square in square_iterator:
                location = square.coordinate
                if not self._scout.rank.walk.is_walkable(self._scout, location):
                    break
                if square.occupant is not None:
                    locations.append(location)
        return ScoutReport(
            scout_report_id=id_emitter.scout_report_id,
            scout=self._scout,
            locations=locations
        )


    def __str__(self) -> str:
        return f"Scout(scout:{self._scout.name})"

