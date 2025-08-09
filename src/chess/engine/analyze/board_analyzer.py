from typing import List

from chess.board.board import ChessBoard
from chess.owner.model.cybernetic_owner import CyberneticOwner
from chess.engine.analyze.scout_report_analysis import ScoutReportAnalysis
from chess.engine.analyze.scout_report_analyzer import ScoutReportAnalyzer
from chess.engine.scout.scout_master import ScoutMaster


class BoardAnalyzer:

    @staticmethod
    def issue_analysis(owner: CyberneticOwner, chess_board: ChessBoard) -> List[ScoutReportAnalysis]:
        situation_map: List[ScoutReportAnalysis] = []
        for scout_report in ScoutMaster.send_scouts(owner, chess_board):
            neighbor_table = ScoutReportAnalyzer(scout_report).issue_analysis()
            if neighbor_table not in situation_map:
                situation_map.append(neighbor_table)
        return situation_map

