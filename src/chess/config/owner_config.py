from enum import Enum
from typing import Optional

from chess.common.game_color import GameColor
from chess.engine.analyze.board_analyzer import BoardAnalyzer
from chess.engine.decision.decision_engine import DecisionEngine
from chess.engine.decision.greedy_decision_engine import GreedyDecisionEngine
from chess.game.player_order import PlayerOrder

class DecisionMode(Enum):
    def __new__(
            cls,
            decision_engine: Optional[DecisionEngine] = None,
            board_analyzer: Optional[BoardAnalyzer] = None
    ):
        obj = object.__new__(cls)
        obj._decision_engine = decision_engine
        obj._board_analyzer = board_analyzer
        return obj

    HUMAN = (None, None,)
    MACHINE = (GreedyDecisionEngine, BoardAnalyzer)

    @property
    def decision_engine(self) -> DecisionEngine:
        return self._decision_engine

    @property
    def board_analyzer(self) -> BoardAnalyzer:
        return self._board_analyzer


class OwnerConfig(Enum):
    def __new__( cls, decision_mode: DecisionMode):
        obj = object.__new__(cls)
        obj._decision_mode = decision_mode
        return obj

    HUMAN = DecisionMode.HUMAN
    CYBERNETIC = DecisionMode.MACHINE

    @property
    def decision_mode(self) -> DecisionMode:
        return self._decision_mode