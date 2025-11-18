# src/chess/engine/engine.py

"""
Module: `chess.engine.engine`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Provides:
Interface to implement pluggable optimization algorithms during team_name turn or the duration of the game.

Contains:
 * `DecisionEngine`


 NOTES:
   Reviewinng what is going to happen with graohing the board_validator and fin the best path there will just be one DecisionEngine
   actually it will be something like AlgorithmSelector tht will select the optimization algorthim for team_name MachinePlayerAgent.
"""



from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

from chess.board import Board
from chess.rank import RankSpec
from chess.coord import Coord



class DecisionEngine(ABC):
  """
  Interface implemented by selectors of optimization engines for `BotCommander`.

  Attributes:
  No attributes. Implementors declare their own.
  """
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
      cybernaut: 'MachinePlayerAgent',
      chess_board: Board
  ) -> Optional[Coord]:
    pass

