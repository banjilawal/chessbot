# src/chess/arena/arena.py

"""
Module: chess.arena.arena
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from typing import List

from chess.agent import PlayerAgent
from chess.board import Board, BoardService
from chess.schema import Schema
from chess.schema.map.lookup import SchemaLookup
from chess.system import SearchResult
from chess.team import Team, UniqueTeamDataService


class Arena:
    _id: int
    _board: Board
    _white_team: Team
    _black_team: Team

    
    def __init__(self, id: int, board: Board, white_team: Team = None, black_team: Team = None):
        self._id = id
        self._board = board
        self._white_team = self._white_team
        self._black_team = self._black_team

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> BoardService:
        return self._board
    
    @property
    def white_team(self) -> Team:
        return self._white_team
    
    @property
    def black_team(self) -> Team:
        return self._black_team
    
    @set.white_team
    def white_team(self, team: Team):
        self._white_team = team
    
    @set.black_team
    def white_team(self, team: Team):
        self._black_team = team
        
    def team_from_schema(
            self,
            schema: Schema,
            schema_service: SchemaLookup = SchemaLookup()
    ) -> SearchResult[Team]:
        """"""
        method = "Arena.team_from_schema"
        try:
            validation = schema_service.schema_validator.validate(schema)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            if self._white_team is not None and schema == self._white_team.schema:
                return SearchResult.success(payload=[self._white_team])
            if self._black_team is not None and schema == self._black_team.schema:
                return SearchResult.success(payload=[self._black_team])
            return SearchResult.empty()
        except Exception as e:
            return SearchResult.failure(e)
    
    @property
    def agents(self) -> List[PlayerAgent]:
        return [self._white_team.player_agent, self._black_team.player_agent]
                
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self.id)
    
