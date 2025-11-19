# src/chess/teamStack/stack/service/service.py

"""
Module: chess.teamStack.stack.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from typing import List, Optional

from chess.piece.stack.exception import DuplicatePushException, PopEmptyStackException
from chess.system import IdentityService, LoggingLevelRouter, SearchResult, Service
from chess.team import Team, TeamService
from chess.system.result import Result
from chess.teamStack import (
    PushingDuplicateTeamException, PushingNullException, TeamStack, TeamStackServiceException,
    TeamStackValidator
)


class TeamStackService(Service[TeamStack]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for TeamStack, TeamStackValidator and TeamStackBuilder.
    2.  Protects TeamStack object from direct manipulation.
    3.  Extends behavior and functionality of TeamStack objects
    4.  Public facing API for TeamStack modules.

    # PROVIDES:
        *   TeamStackBuilder
        *   TeamStackValidator
        *   TeamStackService

    # ATTRIBUTES:
        *   pop_count (int):Assures teams from commited games are not removed from the stack
        *   is_empty (bool): Ensures teams from commited games are not removed from the stack
                                                        the application's safety contract.

        *   team_validator (type[TeamValidator]):   Ensures an existing Team will not raise an
                                                        exception when used by a client.

        *   scalar_service (type[ScalarService]):       Provides scalar product functionality.
    """
    SERVICE_NAME = "TeamService"
    
    SERVICE_NAME = "TeamStackService"
    
    _pop_count: int
    _is_empty: bool
    _stack: TeamStack
    _current_team: Team
    _team_service: TeamService
    _identity_service: IdentityService
    _team_stack_validator: type[TeamStackValidator]
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            stack: TeamStack = TeamStack(),
            team_service: TeamService = TeamService(),
            identity_service: IdentityService = IdentityService(),
            team_stack_validator: type[TeamStackValidator]=TeamStackValidator,
    ):
        self._stack = stack
        self._team_stack_validator = team_stack_validator
        self._team_service = team_service
        
        self._pop_count = 0
        self._is_empty = self._stack.is_empty()
        self._current_team = self._stack.current_team
        self._identity_service = identity_service
        
    @property
    def validator(self) -> type[TeamStackValidator]:
        return self._team_stack_validator
       
    @property
    def stack_size(self) -> int:
        return self._stack.size
    
    @property
    def is_empty(self) -> bool:
        return self._stack.is_empty()
    
    @property
    def current_team(self) -> Optional[Team]:
        return self._stack.current_team
        
    def pop_count(self) -> int:
        return self._pop_count
        
        
    @LoggingLevelRouter.monitor
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
        
        
    def find_tean(self, team) -> SearchResult[Team]:
        method = "TeamStackService.find_team"
        
        try:
            team_validation = self._team_service.validate_team(team)
            if team_validation.is_failure():
                return SearchResult.failure(team_validation.exception)
            
            for team in self._stack.items:
                if team == team:
                    return SearchResult.success(team)
                
            return SearchResult.empty()
        except Exception as ex:
            return SearchResult.failure(
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