# src/chess/arena/arena.py

"""
Module: chess.arena.arena
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""


from chess.board import Board
from chess.team import Team


class Arena:
    _id: int
    _board: Board
    _white_team: Team
    _black_team: Team

    def __init__(self, id: int, white_team: Team, black_team: Team):
        self._id = id
        self._white_team = white_team
        self._black_team = black_team
        self._board = None

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def white_team(self) -> Team:
        return self._white_team
    
    @property
    def black_team(self) -> Team:
        return self._black_team
    
    @property
    def arena_is_full(self) -> bool:
        return self._white_team is not None and self._black_team is not None
    
    @property
    def arena_is_empty(self) -> bool:
        return self._white_team is None and self._black_team is None
    
    @property
    def white_team_is_assigned(self) -> bool:
        return self._white_team is not None
    
    @property
    def black_team_is_assigned(self) -> bool:
        return self._black_team is not None
    
    @board.setter
    def board(self, board: Board):
        self._board = board
    
    @white_team.setter
    def white_team(self, team: Team):
        self._white_team = team
    
    @black_team.setter
    def black_team(self, team: Team):
        self._black_team = team
                
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self.id)
    
