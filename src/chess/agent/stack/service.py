# src/chess/agent/stack/service.py

"""
Module: chess.agent.stack.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""
from typing import List

from chess.piece.stack.exception import DuplicatePushException, PopEmptyStackException
from chess.system import IdentityService, SearchResult
from chess.team import Team, TeamService
from chess.system.result import Result
from chess.agent import (
    PushingDuplicateTeamException, PushingNullException, TeamStack, TeamStackServiceException,
    TeamStackValidator
)


class TeamStackService:
    _pop_count: int
    _stack: TeamStack
    _validator: type[TeamStackValidator]
    _team_service: TeamService
    _identity_service: IdentityService
    
    def __init__(
            self,
            stack: TeamStack,
            validator: type[TeamStackValidator]=TeamStackValidator,
            team_service: TeamService=TeamService()
    ):
        self._stack = stack
        self._validator = validator
        self._team_service = team_service
        
        self._pop_count = 0
        
    def stack_size(self) -> int:
        return self._stack.size()
        
    def pop_count(self) -> int:
        return self._pop_count
        
    def push_team(self, team) -> Result[Team]:
        method = "TeamStackService.push_team"
        
        try:
            team_validation = self._team_service.validate_team(team)
            if team_validation.is_failure():
                return Result.failure(team_validation.exception)
            
            if team in self._stack.items:
                return Result.failure(
                    PushingDuplicateTeamException(
                        f"{method}: {PushingDuplicateTeamException.DEFAULT_MESSAGE}"
                    )
                )
            
        except Exception as ex:
            return Result.failure(
                TeamStackServiceException(
                    f"{method}: {TeamStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    def undo_push(self) -> Result[Team]:
        method = "TeamStackService.undo_push"
        
        try:
            if self._stack.is_empty():
                return Result.failure(
                    PopEmptyStackException(
                        f"{method}: {PopEmptyStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            if self._pop_count == 1:
                return Result.failure(
                
                )
            
            team = self._stack.items.pop()
            return Result.success(team)
        
        except Exception as ex:
            return Result.failure(
                TeamStackServiceException(
                    f"{method}: {TeamStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    def find_by_id(self, id: int) -> SearchResult[Team]:
        method = "TeamStackService.find_by_id"
        
        try:
            id_validation = self._identity_service.validate_id(id)
            if id_validation.is_failure():
                return SearchResult.failure(id_validation.exception)
            
            for team in self._stack.items:
                if team.id == id:
                    return SearchResult.success(team)
                
            return SearchResult.empty()
        
        except Exception as ex:
            return SearchResult.failure(
                TeamStackServiceException(
                    f"{method}: {TeamStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    def find_by_name(self, name: str) -> SearchResult[List[Team]]:
        method = "TeamStackService.find_by_name"
        
        try:
            name_validation = self._identity_service.validate_name(name)
            if name_validation.is_failure():
                return SearchResult.failure(name_validation.exception)
            
            matches = [team for team in self._stack if team.name.upper() == name.upper()]
            
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(matches)
        
        except Exception as ex:
            return SearchResult.failure(
                TeamStackServiceException(
                    f"{method}: {TeamStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )