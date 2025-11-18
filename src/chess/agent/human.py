# src/chess/agent/agent/human.py

"""
Module: chess.agent.agent.human
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.agent import Agent, TeamStackService


class HumanAgent(Agent):

  def __init__(self, id: int,  name: str, team_stack_service: TeamStackService = TeamStackService()):
    super().__init__(id=id, name=name, team_stack_service=team_stack_service)

  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, HumanAgent):
        return True
    return False

  def __hash__(self):
    return hash(self.id)