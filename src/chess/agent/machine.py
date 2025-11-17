# src/chess/agent/agent/machine.py

"""
Module: chess.agent.machine
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
class MachinePlayerAgent(PlayerAgent):


  _engine: DecisionEngine

  def __init__(self, id: int, name: str,engine: DecisionEngine):
    super().__init__(id, name)
    self._engine = engine

  @property
  def engine(self) -> DecisionEngine:
    return self._engine


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, MachinePlayerAgent):
        return True
    return False

  def __hash__(self):
    return hash(self.id)

  def __str__(self):
    return f"{super().__str__()} engine:{self._engine.__class__.__name__.title()}"