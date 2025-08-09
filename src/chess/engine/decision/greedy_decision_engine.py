from typing import List, Optional

from chess.config.rank_config import RankConfig
from chess.engine.analyze.board_analysis import BoardAnalysis
from chess.engine.decision.decision_engine import DecisionEngine
from chess.geometry.coordinate.coordinate import Coordinate, CartesianDistance


class GreedyDecisionEngine(DecisionEngine):


    def __init__(self, board_analysis: BoardAnalysis):
        super().__init__(board_analysis)


    def decide_destination(self) -> Optional[Coordinate]:
        return self._decision_helper()


    def _decision_helper(self) -> Optional[Coordinate]:

        if self._board_analysis.enemy_report_count > 0:
            return self._select_best_capture_report()
        elif self._board_analysis.vacancy_report_count > 0:
            return self._select_furthest_vacant_square_report()
        elif self._board_analysis.obstruction_report_count > 0:
            return self._select_best_obstruction_report()
        else:
            return None


    def _select_best_capture_report(self) -> Optional[Coordinate]:
        best_report = None
        min_capture_diff = self._max_capture_value

        for analysis in self._board_analysis:
            current_capture_value = analysis.enemies[0].rank.capture_value

            if self._max_capture_value - current_capture_value < min_capture_diff:
                best_report = analysis

        if best_report is not None:
            return best_report.enemies[0].coordinate_stack.current_coordinate()
        return best_report


    def _select_furthest_vacant_square_report(self) -> Optional[Coordinate]:

        max_distance = 0
        best_report = None

        for analysis in self._board_analysis:

            square = analysis.vacant_squares[0]
            origin = analysis.chess_piece.coordinate_stack.current_coordinate()

            if CartesianDistance(origin, square.coordinate).distance > max_distance:
                best_report = analysis

        if best_report is not None:
            return best_report.vacant_squares[0].coordinate
        return best_report


    @staticmethod
    def _select_best_obstruction_report(self) -> Optional[Coordinate]:

        max_distance = 0
        best_report = None

        for analysis in self._board_analysis:
            coordinate = analysis.obstructions[0].blocked_coordinate
            origin = analysis.chess_piece.coordinate_stack.current_coordinate()

            if CartesianDistance(origin, coordinate).distance > max_distance:
                best_report = analysis

        if best_report is not None:
            return best_report.obstructions[0].blocked_coordinate
        return None









