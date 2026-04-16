# src/model/arena/arena.py

"""
Module: model.arena.arena
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations


from model import ArenaPlayerBinder, Board


class Arena:
    _id: int
    _board: Board
    _arena_player_binder: ArenaPlayerBinder
    
    def __init__(self, id: int, board: Board, arena_player_binder: ArenaPlayerBinder):
        self._id = id
        self._board = board
        self._arena_player_binder = arena_player_binder
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def binder(self) ->ArenaPlayerBinder:
        return self._arena_player_binder
    
    @property
    def arena_is_full(self) -> bool:
        return self._arena_player_binder.is_full
    
    @property
    def arena_is_empty(self) -> bool:
        return self._board is None and self._arena_player_binder is None
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    