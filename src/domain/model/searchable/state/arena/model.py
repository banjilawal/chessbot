# src/domain/model/searchable/state/arena/model.py

"""
Module: domain.model.searchable.state.arena.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from domain import ArenaPlayerColorBinder, Board, StateModel


class Arena(StateModel):
    _id: int
    _board: Board
    _arena_player_binder: ArenaPlayerColorBinder
    
    def __init__(self, id: int, arena_player_binder: ArenaPlayerColorBinder):
        self._id = id
        self._arena_player_binder = arena_player_binder
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def binder(self) ->ArenaPlayerColorBinder:
        return self._arena_player_binder

    @property
    def arena_has_board(self) -> bool:
        return self._arena_player_binder.board_exists
    
    @property
    def arena_is_full(self) -> bool:
        return self._arena_player_binder.has_both_slots_occupied
    
    @property
    def arena_is_empty(self) -> bool:
        return self._board is None and self._arena_player_binder is None
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    