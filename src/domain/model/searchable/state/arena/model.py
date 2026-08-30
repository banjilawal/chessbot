# src/domain/model/searchable/state/arena/model.py

"""
Module: domain.model.searchable.state.arena.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from domain import ArenaPlayerColorBinder, Board, Game, StateModel


class Arena(StateModel):
    """
    Role:Data-Holder/Data Owner

    Responsibilities:
        1.  Player's interact with the Board through the Arena during Game lifeycle.

    Attributes:
        id: int
        board: Board
        player_binder: ArenaPlayerColorBinder

    Super Class:
        StateModel
    """
    _id: int
    _game: Game
    _board: Board
    _player_binder: ArenaPlayerColorBinder
    
    def __init__(
            self,
            id: int,
            game: Game,
            board: Board,
            player_binder: ArenaPlayerColorBinder,
    ):
        """
        Args:
            id: int
            game: Game
            board: Board
            player_binder: ArenaPlayerColorBinder
        """
        super().__init__(id=id)
        self._game = game
        self._board = board
        self._player_binder = player_binder
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def game(self) -> Game:
        return self._game
        
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def player_binder(self) ->ArenaPlayerColorBinder:
        return self._player_binder

    @property
    def arena_has_board(self) -> bool:
        return self._player_binder.board_exists
    
    @property
    def arena_is_full(self) -> bool:
        return self._player_binder.has_both_slots_occupied
    
    @property
    def arena_is_empty(self) -> bool:
        return self._board is None and self._player_binder is None
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    