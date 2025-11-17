# src/chess/agent/agent/human.py

"""
Module: chess.agent.agent.human
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

class HumanPlayerAgent(PlayerAgent):

  def __init__(self, id: int,  name: str):
    super().__init__(id, name)

  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, HumanPlayerAgent):
        return True
    return False

  def __hash__(self):
    return hash(self.id)