from typing import List

from chess.board.square import Square
from chess.creator.emit import id_emitter
from chess.geometry.coordinate.euclid import Distance
from chess.geometry.coordinate.coord import Coordinate
from chess.token.model.map import Record
from chess.token.model import Piece

from chess.engine.scout.scout_report import ScoutReport
from chess.engine.analyze.scout_report_analysis import ScoutReportAnalysis


class ScoutReportAnalyzer:
    _id: int
    _scout: Piece
    _scout_report: ScoutReport
    _scout_coordinate: Coordinate


    def __init__(self, analyzer_id: int, scout_report: ScoutReport):
        self.id = analyzer_id
        self._scout_report = scout_report

        self._scout = scout_report.scout
        self._scout_coordinate = scout_report.scout.positions.current_coordinate()



    @property
    def scout_report(self) -> ScoutReport:
        return self._scout_report

    def issue_analysis(self) -> ScoutReportAnalysis:
        return ScoutReportAnalysis(
            chess_piece=self._scout,
            enemies=self._sort_enemies(),
            obstructions=self._sort_obstructions(),
            vacant_squares=self._sort_vacant_squares(),
            analysis_id=id_emitter.scout_analysis_id
        )


    def _sort_vacant_squares(self) -> List[Square]:
        vacant_squares: List[Square] = []

        for square in self._scout_report.squares:
            if square is not None and square not in vacant_squares:
                vacant_squares.append(square)
            else:
                continue

        vacant_squares.sort(
            reverse=True,
            key=lambda vacancy: Distance(
                self._scout_coordinate,
                vacancy.coordinate
            ).magnitude
        )
        return vacant_squares


    def _sort_obstructions(self) -> List[Record]:
        obstructions: List[Record] = []

        for square in self._scout_report.squares:
            occupant = square.occupant

            if occupant is not None and not self._scout.is_enemy(occupant):
                obstruction = Record(occupant)
                if obstruction not in obstructions:
                    obstructions.append(obstruction)
            else:
                continue

        obstructions.sort(
            reverse=True,
            key=lambda blocker: Distance(
                self._scout_coordinate, blocker.coordinate
            ).magnitude
        )
        return obstructions


    def _sort_enemies(self) -> List[Piece]:
        enemies: List[Piece] = []

        for square in self._scout_report.squares:
            occupant = square.occupant
            if occupant is not None and self._scout.is_enemy(occupant) and occupant not in enemies:
                enemies.append(occupant)
            else:
                continue

        enemies.sort(
            reverse=True,
            key=lambda chess_piece: chess_piece.rank.capture_value
        )
        return enemies



