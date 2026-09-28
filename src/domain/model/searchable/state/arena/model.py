# src/domain/model/searchable/state/arena/model.py

"""
Module: domain.model.searchable.state.arena.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from domain import ArenaState, PlayerColorBinder, Board, Game, StateModel


class Arena(StateModel):
    """
    Role:Data-Holder/Data Owner

    Responsibilities:
        1.  Player's interact with the Board through the Arena during Game lifeycle.

    Attributes:
        id: int
        board: Board
        player_binder: PlayerColorBinder

    Super Class:
        StateModel
    """
    _id: int
    _game: Game
    _board: Board
    _player_binder: PlayerColorBinder
    _state: ArenaState
    
    def __init__(
            self,
            id: int,
            game: Game,
            board: Board,
            player_binder: PlayerColorBinder,
    ):
        """
        Args:
            id: int
            game: Game
            board: Board
            player_binder: PlayerColorBinder
        """
        super().__init__(id=id)
        self._game = game
        self._board = board
        self._player_binder = player_binder
        self._arena_state = ArenaState.NO_TOKEN_OPENED
    
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
    def player_binder(self) ->PlayerColorBinder:
        return self._player_binder
    
    @property
    def arena_is_empty(self) -> bool:
        return self._board is None and self._player_binder is None
    
    @property
    def no_token_has_opened(self) -> bool:
        return (
                self._board.move_counter == 0 and
                self._state == ArenaState.NO_TOKEN_OPENED
        )
    
    @property
    def opening_move_launched(self) -> bool:
        return (
            self._board.move_counter > 0 and
            self._state == ArenaState.OPENING_MOVE_LAUNCHED
        )
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    