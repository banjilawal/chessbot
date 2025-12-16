# src/chess/arena/arena.py

"""
Module: chess.arena.arena
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from typing import List

from chess.agent import PlayerAgent
from chess.board import BoardService
from chess.team import Team, UniqueTeamDataService


class Arena:
    _id: int
    _white_team: Team
    _black_team: Team
    _board: BoardService
    _team_service: UniqueTeamDataService
    
    def __init__(self, id: int, board: BoardService, team_service: UniqueTeamDataService):
        self._id = id
        self._board = board
        self._team_service = team_service
        self._white_team = self._team_service.white_teams[0]
        self._black_team = self._team_service.black_teams[0]

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> BoardService:
        return self._board
    
    @property
    def white_team(self) -> Team:
        return self._team_service.white_teams[0]
    
    @property
    def black_team(self) -> Team:
        return self._team_service.black_teams[0]
    
    @property
    def team_service(self) -> UniqueTeamDataService:
        return self._team_service
    
    @property
    def agents(self) -> List[PlayerAgent]:
        return [self._white_team.player_agent, self._black_team.player_agent]
                
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    
