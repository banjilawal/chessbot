from typing import List

from chess.board.board import ChessBoard
from chess.owner.model import CyberneticOwner
from chess.engine.scout.scout import Scout
from chess.engine.scout.scout_report import ScoutReport


class ScoutMaster:

    @staticmethod
    def send_scouts(cybernetic_owner: CyberneticOwner, chess_board: ChessBoard) -> List[ScoutReport]:
        scout_reports: List[ScoutReport] = []

        for chess_piece in cybernetic_owner.team.free_pieces():
            report = Scout(chess_piece).survey(chess_board)
            if report not in scout_reports and report is not None:
                scout_reports.append(report)
        return scout_reports