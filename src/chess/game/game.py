# src/chess/game/game.py

"""
Module: chess.game.game
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.board import BoardService
from chess.agent import UniqueAgentDataService


class Game:
    _id: int
    _board: BoardService
    _players: UniqueAgentDataService
    
    def __init__(self, id: int, board: BoardService, players: UniqueAgentDataService):
        self._id = id
        self._board = board
        self._players = players
        
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> BoardService:
        return self._board
    
    @property
    def players(self) -> UniqueAgentDataService:
        return self._players
        
