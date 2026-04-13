from __future__ import annotations
from typing import Dict, List, Optional

from model import Board, Schema
from system import ComputationResult, GameColor, LoggingLevelRouter
from model.team import Team


class TeamTable:
    """
    Role:Data-Holder Structure, Indexer

    # RESPONSIBILITY:
    1.  Hash table for simplifying and centralizing operations on opposing teams in a game.
    2.  Single unified entry point for team operations on the board.

    Super Class:
    None

    Provides:

    # LOCAL ATTRIBUTES:
        *   white_team (Team)
        *   blake_team (Team)

    # INHERITED ATTRIBUTES:
    None
    """
    _board: Board
    _table: Dict[Schema, Team]
    
    def __init__(self, board: Board,):
        self.__table = {}
        self._board = board
        
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
    def board(self) -> Board:
        return self._board
    
    @property
    def table(self) -> Dict[Schema, Team]:
        return self._table
        
    @property
    def white_team(self) -> Optional[Team]:
        return self._table[Schema.WHITE]
    
    @property
    def black_team(self) -> Optional[Team]:
        return self._table[Schema.BLACK]
    
    @property
    def schemas(self) -> List[Schema]:
        keys: List[Schema] = []
        for key in self._table.keys():
            keys.append(key)
        return keys
    
    @property
    def teams(self) -> List[Team]:
        teams: List[Team] = []
        
        for key in self.__table.keys():
            teams.append(self.__table[key])
        return teams
    
    @LoggingLevelRouter.monitor
    def slot_is_occupied(self, team: Team) -> ComputationResult[bool]:
        return ComputationResult.success(self.table[team.schema.color] is None)

        
    