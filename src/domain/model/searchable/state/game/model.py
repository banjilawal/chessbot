# src/domain/model/searchable/state/game/dossier/model/searchable/state.py

"""
Module: domain.model.searchable.state.game.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from typing import List

from domain import Arena, Player, StateModel


class Game(StateModel):
    """
    Role:Controller

    Responsibilities:
    Interface players use to change the Arena's state.

    Super Class:
    None

    # PROVIDES:
    Game

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   arena (Arena)
        *   white_player (Player)
        *   black_player (Player)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _arena: Arena
    _white_player: Player
    _black_player: Player
    
    def __init__(self, id: int, white_player: Player, black_player: Player, arena: Arena):
        super().__init__()
        self._id = id
        self._arena = arena
        self._white_player = white_player
        self._black_player = black_player

    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def white_player(self) -> Player:
        return self._white_player
    
    @property
    def black_player(self) -> Player:
        return self._black_player
    
    @property
    def players(self) -> List[Player]:
        return [self._white_player, self._black_player]
