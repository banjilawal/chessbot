# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""
from typing import Any

from chess.commander import Commander
from chess.piece import Piece
from chess.system import BuildResult, GameColor, SearchResult, ValidationResult
from chess.team import PieceCollection, Team, TeamBuilder, TeamSchema, TeamSearch, TeamValidator


class TeamService:
    _schema: TeamSchema
    _search: TeamSearch
    _builder: TeamBuilder
    _validator: TeamValidator
    
    def __init__(
            self,
            search: TeamSearch,
            schema: TeamSchema,
            builder: TeamBuilder,
            validator: TeamValidator
    ):
        self._schema = schema
        self._search = search
        self._builder = builder
        self._validator = validator
        
    @property
    def schema(self) -> TeamSchema:
        return self._schema
    
    @property
    def search(self) -> TeamSearch:
        return self._search
    
    @property
    def builder(self) -> TeamBuilder:
        return self._builder
    
    @property
    def validator(self) -> TeamValidator:
        return self._validator
    
    
    def search_team(self, team: Team, collection: PieceCollection, search_context) -> SearchResult[[Piece]]:
        return self._search.search(team, collection, search_context)
        
    
    def validate_team(self, candidate: Any) -> ValidationResult[Team]:
        return self._validator.validate(candidate)
    
    def build_team(self, team_id: int, commander: Commander, color: GameColor) -> BuildResult[Team]:
        schema = TeamSchema.schema_from_color(color)
        return self._builder.build(id=team_id, commander=commander, schema=schema)
