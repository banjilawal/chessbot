# src/chess/team/database/database.py

"""
Module: chess.team.database.database
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional, cast

from chess.schema import Schema
from chess.team import Team, TeamContext, TeamContextService, TeamDatabaseException, TeamService, TeamStack
from chess.system import (
    DeletionResult, InsertionResult, LoggingLevelRouter, SearchResult, Database, id_emitter
)


class TeamDatabase(Database[Team]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by TeamStack are unique.
    2.  Guarantee consistency of records in TeamStack.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "TeamDatabase"
    _stack_service: TeamStack
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            stack_service: TeamStack = TeamStack(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (TeamStack)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=stack_service)
        self._stack_service = stack_service

    @property
    def integrity_service(self) -> TeamService:
        return self._stack_service.integrity_service
    
    @property
    def context_service(self) -> TeamContextService:
        return self._stack_service.context_service
    
    @property
    def size(self) -> int:
        return self.data_service.size
    
    @property
    def is_empty(self) -> bool:
        return self.data_service.is_empty
    
    @property
    def current_team(self) -> Optional[Team]:
        return cast (Team, self.data_service.current_item)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[Team]:
        """
        # ACTION:
            1.  Get the result of calling _token_database_core.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   TeamDatabaseException
        """
        method = "TeamDatabase.remove_token"
        
        # --- Handoff the deletion responsibility to _token_database_core. ---#
        deletion_result = self._team_stack.delete_by_id(id=id, identity_service=identity_service)
        
        # Handle the case that the deletion was not completed.
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TeamDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {TeamDatabaseException.ERROR_CODE}",
                    ex=deletion_result.exception
                )
            )
        # --- For either a successful or null deletion result directly forward to the caller. ---#
        return deletion_result
    
    @LoggingLevelRouter.monitor
    def insert(self, team: Team) -> InsertionResult:
        """
        # ACTION:
            1.  If the item fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the item either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _token_database_core.insert_token fails send the wrapped exception in the
                InsertionResult. Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   team (Team)
        # RETURN:
            *   InsertionResult containing either:
                    - On failure: An exception.
                    - On success: bool in payload.
        # RAISES:
            *   TeamDatabaseException
        """
        method = "TeamDatabase.insert"
        
        # --- Use _token_database_core.insert_token because order does not matter for the occupant access. ---#
        insertion_result = self._team_stack.push(item=team)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TeamDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {TeamDatabaseException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: TeamContext) -> SearchResult[List[Team]]:
        """
        # ACTION:
            1.  Get the result of calling _token_database_core.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   TeamDatabaseException
        """
        method = "TokenDatabase.search"
        
        # --- Handoff the search responsibility to _token_database_core. ---#
        search_result = self._team_stack.context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TeamDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {TeamDatabaseException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
    
    @property
    @LoggingLevelRouter.monitor
    def white_teams(self) -> SearchResult[List[Team]]:
        """Convenience method which turns a common search into a dynamic property"""
        method = "TeamDatabase.white_teams"
        # Use color from the schema incase team color is changed from GameColor.BLACK
        result = self.data_service.search(context=TeamContext(color=Schema.WHITE.color))
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @property
    @LoggingLevelRouter.monitor
    def black_teams(self) -> SearchResult[List[Team]]:
        """Convenience method which turns a common search into a dynamic property"""
        method = "TeamDatabase.black_teams"
        # Use color from the schema incase team color is changed from GameColor.BLACK
        result = self.data_service.search(context=TeamContext(color=Schema.BLACK.color))
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def add_team(self, team: Team) -> InsertionResult[Team]:
        method = "TeamDatabase.add_team"
        result = self.push_unique_item(team)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the InsertionResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def undo_team_addition(self) -> DeletionResult[Team]:
        method = "TeamDatabase.undo_add_team"
        result = self.data_service.pop()
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the DeletionResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def search_teams(self, context: TeamContext) -> SearchResult[List[Team]]:
        method = "TeamDatabase.search_teams"
        result = self.data_service.search(context)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTeamStackServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTeamStackServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
