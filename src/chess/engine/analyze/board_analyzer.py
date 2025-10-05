from typing import List

from chess.board.board import Board
from chess.system.emitter import id_emitter
from chess.engine.analyze.board_analysis import BoardAnalysis
from chess.competitor.commander import CyberneticCommander
from chess.engine.analyze.scout_report_analysis import ScoutReportAnalysis
from chess.engine.analyze.scout_report_analyzer import ScoutReportAnalyzer
from chess.engine.scout.master import ScoutMaster


class BoardAnalyzer:

  @staticmethod
  def issue_analysis(owner: CyberneticCommander, chess_board: Board) -> BoardAnalysis:
    enemy_reports_count = 0
    vacancy_reports_count = 0
    obstruction_reports_count = 0

    assessments: List[ScoutReportAnalysis] = []
    for scout_report in ScoutMaster.send_scouts(owner, chess_board):
      analysis = ScoutReportAnalyzer(scout_report).issue_analysis()

      enemy_reports_count += analysis.enemy_count
      vacancy_reports_count += analysis.vacancy_count
      obstruction_reports_count += analysis.obstruction_count

      if analysis not in assessments:
        assessments.append(analysis)
    return BoardAnalysis(
      analsis_id=id_emitter.board_analysis_id,
      enemy_report_count=enemy_reports_count,
      vacancy_report_count=vacancy_reports_count,
      obstruction_report_count=obstruction_reports_count,
      assessments=assessments
    )

