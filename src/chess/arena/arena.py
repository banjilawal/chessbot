# src/chess/arena/arena.py

"""
Module: chess.arena.arena
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""



from chess.team import Team
from chess.board import BoardService

class Arena:
    _id: int
    _white_team: Team
    _black_team: Team
    _board: BoardService
    
    def __init__(self, id: int, white_team: Team, black_team: Team, board: BoardService):
        self._id = id
        self._white_team = white_team
        self._black_team = black_team
        self._board = board
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def white_team(self) -> Team:
        return self._white_team
    
    @property
    def black_team(self) -> Team:
        return self._black_team
    
    @property
    def board(self) -> BoardService:
        return self._board
