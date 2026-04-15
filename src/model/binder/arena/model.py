from __future__ import annotations
from typing import Dict, List, Optional

from microservice import PlayerService
from model import Arena, Schema
from system import ComputationResult, GameColor, LoggingLevelRouter
from model.player import Player


class ArenaPlayerBinder:
    """
    Role:Data-Holder Structure, Indexer

    # RESPONSIBILITY:
    1.  Binder table for simplifying and centralizing operations on opposing players in a game.
    2.  Single unified entry point for player operations on the arena.

    Super Class:
    None

    Provides:

    # LOCAL ATTRIBUTES:
        *   white_player (Player)
        *   black_player (Player)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _arena: Arena
    _table: Dict[Schema, Player]
    _player_service: PlayerService
    
    def __init__(
            self,
            id: int,
            arena: Arena,
            player_service: PlayerService | None = None,
    ):
        self._id = id
        self.__table = {}
        self._arena = arena
        self._player_service = player_service or PlayerService()
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def table(self) -> Dict[Schema, Player]:
        return self._table
    
    @property
    def player_service(self) -> PlayerService:
        return self._player_service
        
    @property
    def is_empty(self) -> bool:
        return len(self.__table) == 0
    
    @property
    def is_full(self) -> bool:
        return not len(self.__table) == 2
    
    @property
    def white_slot_is_occupied(self) -> bool:
        return self._table[Schema.WHITE] is not None
    
    @property
    def black_slot_is_occupied(self) -> bool:
        return self.__table[Schema.BLACK] is not None
        
    @property
    def white_player(self) -> Optional[Player]:
        return self._table[Schema.WHITE]
    
    @property
    def black_player(self) -> Optional[Player]:
        return self._table[Schema.BLACK]
    
    @property
    def schemas(self) -> List[Schema]:
        keys: List[Schema] = []
        for key in self._table.keys():
            keys.append(key)
        return keys
    
    @property
    def players(self) -> List[Player]:
        players: List[Player] = []
        for key in self.__table.keys():
            players.append(self.__table[key])
        return players
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaPlayerBinder):
            return self.id == other.id
        
    def __hash__(self):
        return hash(self.id)

        
    