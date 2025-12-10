# src/chess/arena/arena.py

"""
Module: chess.arena.arena
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""
from typing import List


from chess.team import Team
from chess.agent import Agent
from chess.board import BoardService

class Arena:
    _id: int
    _white_team: Team
    _black_team: Team
    _board: BoardService
    
    def __init__(self, id: int, board: BoardService, white_team: Team, black_team: Team,):
        self._id = id
        self._board = board
        self._white_team = white_team
        self._black_team = black_team

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> BoardService:
        return self._board
    
    @property
    def white_team(self) -> Team:
        return self._white_team
    
    @property
    def black_team(self) -> Team:
        return self._black_team
    
    @property
    def teams(self) -> List[Team]:
        return [self._white_team, self._black_team]
    
    @property
    def agent(self) -> List[Agent]:
        return [self._white_team.agent, self._black_team.agent]
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    
