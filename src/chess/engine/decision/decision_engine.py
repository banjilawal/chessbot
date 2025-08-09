from abc import ABC, abstractmethod
from typing import List, Optional

from chess.engine.analyze.board_analysis import BoardAnalysis
from chess.engine.analyze.scout_report_analysis import ScoutReportAnalysis
from chess.geometry.coordinate.coordinate import Coordinate


class DecisionEngine(ABC):
    _board_analysis: BoardAnalysis

    def __init__(self, board_analysis: BoardAnalysis):
        self._board_analysis = board_analysis


    @abstractmethod
    def decide_destination() -> Optional[Coordinate]:
        pass

