from typing import List

from chess.board.element.square import Square
from chess.geometry.coordinate.coordinate import CartesianDistance
from chess.token.obstruction import Obstruction
from chess.token.piece import ChessPiece

from engine.scout.raw_scout_report import RawScoutReport



class ScoutReportSorter:
    _scout_report: RawScoutReport

    def __init__(self, scout_report: RawScoutReport):
        self._scout_report = scout_report

    @property
    def scout(self) -> RawScoutReport:
        return self._scout_report

    def sort_vacant_squares(self) -> List[Square]:
        empty_squares: List[Square] = []
        origin = self._scout_report.scout.coordinate_stack.current_coordinate()
        for square in self._scout_report.squares:
            if square.occupant is None and square not in empty_squares:
                empty_squares.append(square)
            else:
                continue
        empty_squares.sort(
            reverse=True,
            key=lambda vacant_square: CartesianDistance(origin, vacant_square.coordinate).distance,
        )
        return empty_squares


    def sort_obstructions(self) -> List[Obstruction]:
        obstructions: List[Obstruction] = []
        origin = self._scout_report.scout.coordinate_stack.current_coordinate()
        for square in self._scout_report.squares:
            occupant = square.occupant
            if occupant is not None and not self._scout_report.scout.is_enemy(occupant):
                obstruction = Obstruction(occupant)
                if obstruction not in obstructions:
                    obstructions.append(obstruction)
            else:
                continue
        obstructions.sort(
            reverse=True,
            key=lambda blocker: CartesianDistance(origin, blocker.coordinate).distance
        )
        return obstructions


    def sort_enemies(self):
        enemies: List[ChessPiece] = []
        for square in self._scout_report.squares:
            occupant = square.occupant
            if (
                occupant is not None and self._scout_report.scout.is_enemy(occupant) and
                occupant not in enemies
            ):
                enemies.append(occupant)
            else:
                continue
        return enemies.sort(key=lambda chess_piece: chess_piece.rank.capture_value, reverse=True)



