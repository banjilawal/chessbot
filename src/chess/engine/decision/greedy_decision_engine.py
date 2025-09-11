from typing import Optional

from chess.board.board import Board
from chess.engine.analyze.board_analysis import BoardAnalysis
from chess.engine.analyze.board_analyzer import BoardAnalyzer
from chess.engine.decision.decision_engine import DecisionEngine

from chess.coord import Coord
from chess.competitor.commander import CyberneticCommander


class GreedyDecisionEngine(DecisionEngine):
    _board_analysis: BoardAnalysis

    def __init__(self, engine_id: int, board_analyzer: BoardAnalyzer = BoardAnalyzer()):
        super().__init__(engine_id=engine_id, analyzer=board_analyzer)
        self._board_analysis = None


    def decide_destination(self, cybernaut: CyberneticCommander, chess_board: Board) -> Optional[Coord]:
        self._board_analysis = self.board_analyzer.issue_analysis(cybernaut, chess_board)
        return self._decision_helper()


    def _decision_helper(self) -> Optional[Coord]:

        if self._board_analysis.enemy_report_count > 0:
            return self._select_best_capture_report()
        elif self._board_analysis.vacancy_report_count > 0:
            return self._select_furthest_vacant_square_report()
        elif self._board_analysis.obstruction_report_count > 0:
            return self._select_best_obstruction_report()
        else:
            return None


    def _select_best_capture_report(self) -> Optional[Coord]:
        best_report = None
        min_capture_diff = self.max_capture_value

        for analysis in self._board_analysis.assessments:
            current_capture_value = analysis.enemies[0].rank.value

            if self._max_capture_value - current_capture_value < min_capture_diff:
                best_report = analysis

        if best_report is not None:
            return best_report.enemies[0].positions.current_coord()
        return best_report


    def _select_furthest_vacant_square_report(self) -> Optional[Coord]:

        max_distance = 0
        best_report = None

        for analysis in self._board_analysis.assessments:

            square = analysis.vacant_squares[0]
            origin = analysis.chess_piece.positions.current_coord()

            if Distance(origin, square.coord).magnitude > max_distance:
                best_report = analysis

        if best_report is not None:
            return best_report.vacant_squares[0].coord
        return best_report


    @staticmethod
    def _select_best_obstruction_report(self) -> Optional[Coord]:

        max_distance = 0
        best_report = None

        for analysis in self._board_analysis.assessments:
            coordinate = analysis.obstructions[0].blocked_coordinate
            origin = analysis.chess_piece.positions.current_coord

            if Distance(origin, coordinate).magnitude > max_distance:
                best_report = analysis

        if best_report is not None:
            return best_report.obstructions[0].blocked_coordinate
        return None









