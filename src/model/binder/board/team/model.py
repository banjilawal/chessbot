# src/model/state/binder/board/team/model/state.py

"""
Module: model.state.binder.board.team.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, List, Optional


from model.state.team import Team
from model import Board, Schema
from microservice import TeamService

class BoardTeamBinder:
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        
    Responsibility:
        1.  Performs integrity and consistency checks of the board's teams.
        2.  Simplifies management of a board's steams.
        
    Attributes:
        id: int
        board: Board
        table: Dict[str, Any]
        team_service: TeamService
        
    Provides:

    Super Class:
        Binder
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
        """
        Args:
            id: int
            board: Board
            table: Dict[str, Any]
            team_service: TeamService
        """
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
        if isinstance(other, BoardTeamBinder):
            return self.id == other.id
        
    def __hash__(self):
        return hash(self.id)

        
    