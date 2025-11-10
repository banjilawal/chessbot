# src/chess/commander/bot.py

"""
Module: `chess.commander.bot`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides: Automated player that uses team_name `DecisionEngine` for picking optimal
  move during team_name turn.

Contains:
 * `Bot`
"""
from typing import cast

from chess.commander import Commander
from chess.engine import DecisionEngine
from chess.rank import Bishop


class Bot(Commander):
  """
  Automated player that uses team_name `DecisionEngine`

  Attributes: [
    * `_engine` (`DecisionEngine`): Selects the optimal during its turn.
    * All attributes fro the super class.
  move during team_name turn.
  """

  _engine: DecisionEngine

  def __init__(self, id: int, name: str,engine: DecisionEngine):
    super().__init__(id, name)
    self._engine = engine

  @property
  def engine(self) -> DecisionEngine:
    return self._engine


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, Bot):
        return True
    return False

  def __hash__(self):
    return hash(self.id)

  def __str__(self):
    return f"{super().__str__()} engine:{self._engine.__class__.__name__.title()}"