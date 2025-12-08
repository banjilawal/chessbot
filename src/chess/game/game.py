# src/chess/game/game.py

"""
Module: chess.game.game
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import List

from chess.board import BoardService
from chess.agent import Agent, UniqueAgentDataService


class Game:
    _id: int
    _board: BoardService
    _white_player: Agent
    _black_player: Agent
    
    def __init__(self, id: int, white_player: Agent, black_player: Agent, board: BoardService = BoardService()):
        self._id = id
        self._board = board
        self._white_player = white_player
        self._black_player = black_player
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> BoardService:
        return self._board
    
    @property
    def white_player(self) -> Agent:
        return self._white_player
    
    @property
    def black_player(self) -> Agent:
        return self._black_player
    
    @property
    def players(self) -> List[Agent]:
        return [self._white_player, self._black_player]
        
