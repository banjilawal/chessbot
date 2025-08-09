from typing import List

from engine.scout.scout_report import ScoutReport
from engine.sorter.square_comparator import SquareComparator


class ScoutReportSorter:

    @staticmethod
    def receive_unsorted_reports(
            comparator: SquareComparator,
            reports: List[ScoutReport]
    ) -> List[ScoutReport]:
        pass


