from typing import List

from chess.engine.analyze.scout_report_analysis import ScoutReportAnalysis


class BoardAnalysis:
    _id: int
    _enemy_report_count: int
    _vacancy_report_count: int
    _obstruction_report_count: int
    _assessments: List[ScoutReportAnalysis]


    def __init__(self,
         analysis_id: int,
         enemy_report_count:int,
         vacancy_report_count:int,
         obstruction_report_count:int,
         assessments: List[ScoutReportAnalysis]
    ):
        self._id = analysis_id
        self._enemy_report_count = enemy_report_count
        self._vacancy_report_count = vacancy_report_count
        self._obstruction_report_count = obstruction_report_count
        self.assessments = assessments

    @property
    def id(self) -> int:
        return self._id

    @property
    def enemy_report_count(self) -> int:
        return self._enemy_report_count

    @property
    def vacancy_report_count(self) -> int:
        return self._vacancy_report_count

    @property
    def obstruction_report_count(self) -> int:
        return self._obstruction_report_count

    @property
    def assessments(self) -> List[ScoutReportAnalysis]:
        return self._assessments

