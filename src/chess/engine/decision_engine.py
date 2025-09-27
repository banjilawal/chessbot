from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

from chess.board import Board
from chess.rank import RankSpec
from chess.coord import Coord



class DecisionEngine(ABC):
    _id: int
    _max_capture_value: int
    _board_analyzer: 'BoardAnalyzer'

    def __init__(self, engine_id:int, analyzer: 'BoardAnalyzer'):
        self._id = engine_id
        self._board_analyzer = analyzer
        self._max_capture_value = RankSpec.QUEEN.ransom


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
    def decide_destination(
            self,
            cybernaut: 'Bot',
            chess_board: Board
    ) -> Optional[Coord]:
        pass

