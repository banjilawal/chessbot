from typing import List, Optional

from chess.config.rank_config import RankConfig
from chess.engine.analyze.scout_report_analysis import ScoutReportAnalysis
from chess.engine.decision.decision_engine import DecisionEngine
from chess.geometry.coordinate.coordinate import Coordinate, CartesianDistance
from chess.rank.queen_rank import QueenRank
from chess.token.piece import ChessPiece


class GreedyEngine(DecisionEngine):

    @staticmethod
    def decide_destination(board_analysis: List[ScoutReportAnalysis]) -> Optional[Coordinate]:


    @staticmethod
    def _decision_helper(board_analysis: List[ScoutReportAnalysis]) -> Optional[Coordinate]:
        if len(board_analysis.ca) == 0:
            return None
        best_capture_report = GreedyEngine._select_best_capture_report(board_analysis)
        best_obstruction_report = GreedyEngine._select_best_obstruction_report(board_analysis)
        best_vacant_square_report = GreedyEngine._select_furthest_vacant_square_report(board_analysis)

        if best_capture_report is not None:
            return best_capture_report.chess_piece.coordinate_stack.current_coordinate()
        elif best_obstruction_report is not None:
            return best_obstruction_report.chess_piece.coordinate_stack.current_coordinate()
        elif best_vacant_square_report is not None:
            return best_vacant_square_report.chess_piece.coordinate_stack.current_coordinate()
        else:
            return None


    @staticmethod
    def _select_best_capture_report(
        board_analysis: List[ScoutReportAnalysis]
    ) -> Optional[ScoutReportAnalysis]:

        highest_capture_value = RankConfig.QUEEN.capture_value
        min_capture_value_range = RankConfig.QUEEN.capture_value

        best_report = None

        for analysis in board_analysis:
            current_capture_value_diff = highest_capture_value - analysis.enemies[0].rank.capture_value
            if current_capture_value_diff < min_capture_value_range:
                best_report = analysis
        return best_report


    @staticmethod
    def _select_furthest_vacant_square_report(
        board_analysis: List[ScoutReportAnalysis]
    ) -> Optional[ScoutReportAnalysis]:

        max_distance = 0
        best_report = None

        for analysis in board_analysis:

            square = analysis.vacant_squares[0]
            origin = analysis.chess_piece.coordinate_stack.current_coordinate()

            if CartesianDistance(origin, square.coordinate).distance > max_distance:
                best_report = analysis
        return best_report


    @staticmethod
    def _select_best_obstruction_report(
        board_analysis: List[ScoutReportAnalysis]
    ) -> Optional[ScoutReportAnalysis]:

        max_distance = 0
        best_report = None

        for analysis in board_analysis:
            coordinate = analysis.obstructions[0].blocked_coordinate
            origin = analysis.chess_piece.coordinate_stack.current_coordinate()

            if CartesianDistance(origin, coordinate).distance >max_distance:
                best_report = analysis
        return best_report









