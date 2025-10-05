# src/chess/commander/bot.py

"""
Module: `chess.commander.bot`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides: Automated player that uses a `DecisionEngine` for picking optimal
  move during a turn.

Contains:
 * `Bot`
"""



from chess.system import auto_id
from chess.commander import Commander
from chess.engine import DecisionEngine

@auto_id
class Bot(Commander):
  """
  Automated player that uses a `DecisionEngine`

  Attributes: [
    * `_engine` (`DecisionEngine`): Selects the optimal during its turn.
    * All attributes fro the super class.
  move during a turn.
  """

  _engine: DecisionEngine

  def __init__(self, name: str,engine: DecisionEngine):
    super().__init__(name)
    self._engine = engine

  @property
  def engine(self) -> DecisionEngine:
    return self._engine


  def __eq__(self, other):
    if not super().__eq__(other):
      return False

    if isinstance(other, Bot):
      return self._id == other.id
    return False

  def __str__(self):
    return f"{super().__str__()} engine:{self._engine.__class__.__name__.title()}"