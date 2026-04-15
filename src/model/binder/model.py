from __future__ import annotations
from typing import Dict, List, Optional

from microservice import TeamService
from model import Board, Schema
from system import ComputationResult, GameColor, LoggingLevelRouter
from model.team import Team


class TeamBinder:
    """
    Role:Data-Holder Structure, Indexer

    # RESPONSIBILITY:
    1.  Binder table for simplifying and centralizing operations on opposing teams in a game.
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
    _id: int
    _board: Board
    _table: Dict[Schema, Team]
    _team_service: TeamService
    
    def __init__(
            self,
            id: int,
            board: Board,
            team_service: TeamService | None = None,
    ):
        self._id = id
        self.__table = {}
        self._board = board
        self._team_service = team_service or TeamService()
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def table(self) -> Dict[Schema, Team]:
        return self._table
    
    @property
    def team_service(self) -> TeamService:
        return self._team_service
        
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
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamBinder):
            return self.id == other.id
        
    def __hash__(self):
        return hash(self.id)

        
    