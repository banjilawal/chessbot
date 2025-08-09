from abc import ABC, abstractmethod
from typing import List, Optional

from chess.config.rank_config import RankConfig
from chess.engine.analyze.board_analysis import BoardAnalysis
from chess.engine.analyze.scout_report_analysis import ScoutReportAnalysis
from chess.geometry.coordinate.coordinate import Coordinate


class DecisionEngine(ABC):
    _board_analysis: BoardAnalysis
    _max_capture_value: int

    def __init__(self, board_analysis: BoardAnalysis):
        self._board_analysis = board_analysis
        self._max_capture_value = RankConfig.QUEEN.capture_value


    @property
    def board_analysis(self) -> BoardAnalysis:
        return self._board_analysis


    @property
    def max_capture_value(self) -> int:
        return self._max_capture_value


    @abstractmethod
    def decide_destination(self) -> Optional[Coordinate]:
        pass

