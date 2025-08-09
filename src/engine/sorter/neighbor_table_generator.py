from typing import List

from chess.board.element.square import Square
from chess.creator.emit import id_emitter
from chess.geometry.coordinate.coordinate import CartesianDistance
from chess.token.obstruction import Obstruction
from chess.token.piece import ChessPiece

from engine.scout.raw_scout_report import ScoutReport
from engine.sorter.neighbor_table import NeighborTable


class NeighborTableGenerator:
    _scout_report: ScoutReport

    def __init__(self, scout_report: ScoutReport):
        self._scout_report = scout_report

    @property
    def scout(self) -> ScoutReport:
        return self._scout_report

    def issue_neighbor_table(self) -> NeighborTable:
        return NeighborTable(
            neighbor_table_id=id_emitter.neighbor_table_id,
            chess_piece=self._scout_report.scout,
            enemies=self._sort_enemies(),
            obstructions=self._sort_obstructions(),
            vacant_squares=self._sort_vacant_squares()
        )

    def _sort_vacant_squares(self) -> List[Square]:
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


    def _sort_obstructions(self) -> List[Obstruction]:
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


    def _sort_enemies(self):
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



