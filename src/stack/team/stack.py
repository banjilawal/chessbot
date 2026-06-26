# src/stack/team/stack.py

"""
Module: stack.team.stack
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from microservice import TeamService
from model import Team
from stack import StackService


class TeamStackService(StackService[Team]):
    """
    Role:Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing team objects and their lifecycles.
    3.  Ensure integrity of team data schema
    4.  Stack data structure for Team objects with no guarantee of uniqueness.
    
    Super Class:
        *   StackService

    Provides:

    
    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "TeamStack"
    
    _stack: List[Team]
    _microservice: TeamService
    _context_service: TeamQueryService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            microservice: TeamService = TeamService(),
            id: int = IdFactory.next_id(class_name="TeamStack"),
            context_microservice: TeamQueryService = TeamQueryService(),
    ):
        """
        Args:
            id: int
            name: str
            microservice: TeamService
        """
        method = "TokenStackService.__init__"
        super().__init__(id=id, name=name,)
        self._stack = []
        self._service = service
        self._context_service = context_service
        
    @property
    def size(self) -> int:
        return len(self._stack)
        
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def integrity_service(self) -> Teammicroservice:
        return self._service
    
    @property
    def context_service(self) -> TeamQuerymicroservice:
        return self.context_service
    
    @property
    def current_item(self) -> Team:
        return self._stack[-1] if self.is_empty else None
    
    @LoggingLevelRouter.monitor
    def push(self, item: Team) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   item (Team)
        # RETURNS:
            *   InsertionResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        Raises:
            *   TeamStackException
        """
        method = "TeamStack.push"
        
        # Handle the case that, the team is unsafe.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                TeamStackException(
                    msg=f"StackId:{self.id}, {method}: {TeamStackException.ERR_CODE}",
                    ex=PushingTeamFailedException(
                        msg=f"{method}: {PushingTeamFailedException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the team is already present in the schema.
        if item in self._stack:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                TeamStackException(
                    msg=f"StackId:{self.id}, {method}: {TeamStackException.ERR_CODE}",
                    ex=PushingTeamFailedException(
                        msg=f"{method}: {PushingTeamFailedException.ERR_CODE}",
                        ex=AddingDuplicateTeamException(
                            f"{method}: {AddingDuplicateTeamException.MSG}"
                        )
                    )
                )
            )
        # --- Team order is not required. Direct insertion into the schema is simpler that a push. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Team]:
        """
        # ACTION:
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_Teams_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_Teams_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        Raises:
            *   TeamStackException
        """
        method = "TeamStack.pop"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TeamStackException(
                    msg=f"StackId:{self.id}, {method}: {TeamStackException.ERR_CODE}",
                    ex=PoppingTeamStackFailedException(
                        msg=f"{method}: {PoppingTeamStackFailedException.ERR_CODE}",
                        ex=PoppingEmptyTeamStackException(
                            f"{method}: {PoppingEmptyTeamStackException.MSG}"
                        )
                    )
                )
            )
        team = self._stack.pop(-1)
        return DeletionResult.success(team)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_microservice: IdentityService = IdentityService()
    ) -> DeletionResult[Team]:
        """
        # ACTION:
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_Teams_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_Teams_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        Raises:
            *   TeamStackException
        """
        method = "TeamStack.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TeamStackException(
                    msg=f"StackId:{self.id}, {method}: {TeamStackException.ERR_CODE}",
                    ex=PoppingTeamStackFailedException(
                        msg=f"{method}: {PoppingTeamStackFailedException.ERR_CODE}",
                        ex=PoppingEmptyTeamStackException(
                            f"{method}: {PoppingEmptyTeamStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the idis not safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TeamStackException(
                    msg=f"StackId:{self.id}, {method}: {TeamStackException.ERR_CODE}",
                    ex=PoppingTeamStackFailedException(
                        msg=f"{method}: {PoppingTeamStackFailedException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for an item with target id. ---#
        for item in self._stack:
            if item.id == id:
                # Handle the case that, the match is the wrong type.
                if not isinstance(item, Team):
                    # Send the exception chain on failure.
                    return DeletionResult.failure(
                        TeamStackException(
                            msg=f"StackId:{self.id}, {method}: {TeamStackException.ERR_CODE}",
                            ex=PoppingTeamStackFailedException(
                                msg=f"{method}: {PoppingTeamStackFailedException.ERR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Team, got {type(item).__name__} "
                                    f"instead of a Team."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted item in the DeletionResult. ---#
                team = cast(Team, item)
                self._stack.remove(team)
                return DeletionResult.success(payload=team)
        
        # If none of the items had that id return an empty DeletionResult.
        return DeletionResult.nothing_to_delete()
    
    @LoggingLevelRouter.monitor
    def search(self, context: TeamContext) -> SearchResult[List[Team]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a TeamStackException 
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (TeamContext)
        # RETURN:
            *   SearchResult[List[Team] containing either:
                    - On failure: An exception.
                    - On success: List[Team] in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   TeamStackException
        """
        method = "TeamStack.context"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                TeamStackException(
                    msg=f"ServiceID:{self.id} {method}: {TeamStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
    
    @LoggingLevelRouter.monitor
    def query(self, context: TeamContext) -> SearchResult[List[Team]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a TeamStackException 
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (TeamContext)
        # RETURN:
            *   SearchResult[List[Team] containing either:
                    - On failure: An exception.
                    - On success: List[Team] in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   TeamStackException
        """
        method = "TeamStack.context"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                TeamStackException(
                    msg=f"ServiceID:{self.id} {method}: {TeamStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
    
