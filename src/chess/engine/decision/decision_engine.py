from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

from chess.board.board import ChessBoard
from chess.config.rank_config import RankConfig
from chess.engine.analyze import board_analyzer
from chess.engine.analyze.board_analysis import BoardAnalysis

from chess.geometry.coordinate.coordinate import Coordinate
from chess.owner.cybernetic_owner import CyberneticOwner

if TYPE_CHECKING:
    from chess.engine.analyze.board_analyzer import BoardAnalyzer


class DecisionEngine(ABC):
    _id: int
    _max_capture_value: int
    _board_analyzer: 'BoardAnalyzer'

    def __init__(self, engine_id:int, analyzer: 'BoardAnalyzer'):
        self._id = engine_id
        self._board_analyzer = analyzer
        self._max_capture_value = RankConfig.QUEEN.capture_value


    @property
    def id(self) -> int:
        return self._id


    @property
    def max_capture_value(self) -> int:
        return self._max_capture_value


    @property
    def board_analyzer(self) -> 'BoardAnalyzer':
        return self._board_analyzer




    @abstractmethod
    def decide_destination(self, cybernaut: CyberneticOwner, chess_board: ChessBoard) -> Optional[Coordinate]:
        pass

