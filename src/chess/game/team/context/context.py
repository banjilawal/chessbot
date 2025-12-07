# src/chess/team/context/context.py

"""
Module: chess.team.context.context
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.agent import Agent
from chess.game import Game
from chess.system import Context, GameColor

class TeamContext(Context):
  """
  # ROLE: Option Selection,

  # RESPONSIBILITIES:
  1.  Selecting which Team attribute will be used for running TeamFinder.
  2.  Extend Context super class' features.

  # PROVIDES:
  1. TeamFinder filtering key-value pair.

  # ATTRIBUTES:
      *   game (Optional[Game])
      *   agent (Optional[Agent])
      *   color (Optional[GameColor])
      
    # CONSTRUCTOR:
      *   __init__(
                id: Optional[int] = None,
                name: Optional[sstr] = None,
                game: Optional[Game] = None,
                agent: Optional[Agent] = None,
                color: Optional[GameColor] = None,
          )
      All flags must be turned set to null byy default. Only activated flags should have a not-null
      value.
    
    # CLASS METHODS:
    None
    
    # INSTANCE METHODS:
      *   to_dict() -> dict:
  """
  _game: Optional[Game] = None
  _agent: Optional[Agent] = None
  _color: Optional[GameColor] = None,

  def __init__(
      self,
      id: Optional[int] = None,
      name: Optional[str] = None,
      game: Optional[Game] = None,
      agent: Optional[Agent] = None,
      color: Optional[GameColor] = None,
      
  ):
    method = "TeamContext.__init__"
    super().__init__(id=id, name=name)
    self._game = game
    self._agent = agent
    self._color = color
    
  @property
  def agent(self) -> Optional[Agent]:
    return self._agent
  
  @property
  def game(self) -> Optional[Game]:
    return self._game
  
  @property
  def color(self) -> Optional[GameColor]:
    return self._color
  
  def to_dict(self) -> dict:
    """
    # ACTION:
    Convert a TeamContext attributes into a dictionary.

    # PARAMETERS:
    None

    # Returns:
        dict

    # RAISES:
    None
    """
    return {
      "id": self.int,
      "name": self.name,
      "game": self.game,
      "agent": self._agent,
      "color": self._color,
    }
