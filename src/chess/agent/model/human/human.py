# src/chess/model/human/human.py

"""
Module: chess.model.human.human
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import Agent
from chess.team import UniqueTeamDataService


class HumanAgent(Agent):
    
    def __init__(
            self,
            id: int,
            name: str,
            games: UniqueGameDataService = UniqueGameDataService(),
            team_assignments: UniqueTeamDataService = UniqueTeamDataService(),
    ):
        super().__init__(id=id, name=name, games=games, team_assignments=team_assignments)
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, HumanAgent):
                return True
        return False
    
    def __hash__(self):
        return hash(self.id)
