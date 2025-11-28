# src/chess/team/context/context.py

"""
Module: chess.team.context.context
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.agent import Agent
from chess.team import TeamSchema
from chess.system import Context, GameColor

class TeamContext(Context):
  """
  # ROLE: Option Selection,

  # RESPONSIBILITIES:
  1.  Selecting which Team attribute will be used for running TeamSearch.
  2.  Extend Context super class' features.


  # PROVIDES:
  1. TeamSearch filtering key-value pair.

  # ATTRIBUTES:
      *   agent (Optional[Agent])
      *   color (Optional[GameColor])
  """
  _agent: Optional[Agent] = None
  _color: Optional[GameColor] = None,
  _schema: Optional[TeamSchema] = None

  def __init__(
      self,
      id: Optional[int] = None,
      name: Optional[str] = None,
      agent: Optional[Agent] = None,
      color: Optional[GameColor] = None,
      schema: Optional[TeamSchema] = None,
  ):
    """
    # Action:
    1.  Construct TeamContext objects
    """
    method = "TeamContext.__init__"
    super().__init__(id=id, name=name)
    self._agent = agent
    self._color = color
    self._schema = schema
    
  @property
  def agent(self) -> Optional[Agent]:
    return self._agent
  
  @property
  def color(self) -> Optional[GameColor]:
    return self._color
  
  @property
  def schema(self) -> Optional[TeamSchema]:
    return self._schema
  
  def to_dict(self) -> dict:
    """
    # ACTION:
    1.  Convert a Context into a dictionary.
    2.  Subclasses must implement this method.

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
      "agent": self._agent,
      "color": self._color,
      "schema": self._schema
    }
