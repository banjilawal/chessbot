# src/chess/team_name/service.py

"""
Module: chess.team_name.service
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""
from typing import Any, cast

from chess.agent import PlayerAgent
from chess.piece import Piece
from chess.system import BuildResult, GameColor, LoggingLevelRouter, SearchResult, ValidationResult
from chess.team import (
    PieceCollectionCategory, Team, TeamBuildFailedException, TeamBuilder, TeamSchema, TeamSearch,
    TeamValidator
)


class TeamService:
    _schema: TeamSchema
    _search: TeamSearch
    _builder: TeamBuilder
    _validator: TeamValidator
    _teams: [Team]
    
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
        self._teams = [Team]
        
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
    
    @LoggingLevelRouter.monitor
    def search_team(self, team: Team, collection: PieceCollectionCategory, search_context) -> SearchResult[[Piece]]:
        return self._search.search(team, collection, search_context)
        
    @LoggingLevelRouter
    def validate_team(self, candidate: Any) -> ValidationResult[Team]:
        return self._validator.validate(candidate)
    
    @LoggingLevelRouter.monitor
    def build_team(self, team_id: int, commander: PlayerAgent, color: GameColor) -> BuildResult[Team]:
        """"""
        method = "TeamService.build_team"
        try:
            schema = TeamSchema.schema_from_color(color)
            build_result = self._builder.build(id=team_id, commander=commander, schema=schema)
            
            if build_result.is_failure():
                return BuildResult.failure(build_result.exception)
            
            team = cast(Team, build_result.payload)
            if team not in self._teams:
                self._teams.append(team)
            
            return BuildResult.success(team)
            
        except Exception as ex:
            return BuildResult(
                TeamBuildFailedException(
                    f"{method}: {TeamBuildFailedException.DEFAULT_MESSAGE}",
                    ex
                )
            )
