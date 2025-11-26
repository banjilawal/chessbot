# src/chess/team/context/exception.py

"""
Module: chess.team.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.agent import Agent
from chess.rank import Rank
from chess.system import Context, GameColor
from chess.team import TeamSchema


class TeamContext(Context):
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
    return {
      "id": self.int,
      "name": self.name,
      "agent": self._agent,
      "color": self._color,
      "schema": self._schema
    }
