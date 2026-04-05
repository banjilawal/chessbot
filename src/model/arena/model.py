# src/model/arena/model.py

"""
Module: model.arena.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model.board import Board
from model.player import Player


class Arena:
    _id: int
    _board: Board
    _white_player: Player
    _black_player: Player

    def __init__(self, id: int, white_player: Player, black_player: Player):
        self._id = id
        self._white_player = white_player
        self._black_player = black_player
        self._board = None

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def white_player(self) -> Player:
        return self._white_player
    
    @property
    def black_player(self) -> Player:
        return self._black_player
    
    @property
    def arena_is_full(self) -> bool:
        return self._white_player is not None and self._black_player is not None
    
    @property
    def arena_is_empty(self) -> bool:
        return self._white_player is None and self._black_player is None
    
    @property
    def white_player_is_assigned(self) -> bool:
        return self._white_player is not None
    
    @property
    def black_player_is_assigned(self) -> bool:
        return self._black_player is not None
    
    @board.setter
    def board(self, board: Board):
        self._board = board
    
    @white_player.setter
    def white_player(self, player: Player):
        self._white_player = player
    
    @black_player.setter
    def black_player(self, player: Player):
        self._black_player = player
                
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self.id)
    
