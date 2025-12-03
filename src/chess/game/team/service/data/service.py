# src/chess/team/service/data/service.py

"""
Module: chess.team.service.data.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
from chess.team import Team, TeamContext, TeamContextService, TeamSearch, TeamIntegrityService, TeamInsertionFailedException

class TeamDataService(DataService[Team]):
    """
    # ROLE: Data Stack, Search IntegrityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Stack data structure for Team objects with no guarantee of uniqueness.
    3.  Implements search, insert, delete, and update operations on Team objects.
    4.  ContextService for building selecting different search attributes.
    5.  Including a TeamIntegrityService instance creates a microservice for clients.

    # PROVIDES:
        *   TeamIntegrityService
        *   ContextService
        *   Search
        *   TeamStack data structure

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   items (List[Team]):
        *   search (TeamSearch):
        *   service (TeamIntegrityService):
        *   context_service (TeamContextService):;
        *   current_item (Team):
        *   size (int):
        
    # CONSTRUCTOR:
        *   __init__(
                id: int, name: str, items: List[Team], search: TeamSearch,
                service: TeamIntegrityService, contextService: TeamContextService
            )
    
    # CLASS METHODS:
    None
    
    # INSTANCE METHODS:
        *   push(item: Team) -> InsertionResult[Team]
    """
    DEFAULT_NAME = "TeamDataService"
    
    def __init__(
            self,
            name=DEFAULT_NAME,
            id=id_emitter.service_id,
            items: List[Team] = List[Team],
            search: TeamSearch = TeamSearch(),
            service: TeamIntegrityService = TeamIntegrityService(),
            context_service: TeamContextService = TeamContextService(),
    ):
        """
        # Action
        1.  Use id_emitter to automatically generate a unique id for each TeamDataService instance.
        2.  Automatic dependency injection by providing working default instances of each attribute.
        """
        method = "TeamDataService.__init__"
        
        super().__init__(
            id=id,
            name=name,
            items=items,
            search=search,
            service=service,
            context_service=context_service
        )
    
    def push(self, item: Team) -> InsertionResult[Team]:
        """
        # ACTION:
        1.  Use TeamDataService.service.validator to certify item.
        2.  If certification fails return the exception inside an InsertionResult.
        3.  Otherwise, push item onto the stack.
        4.  Send the successfully pushed data back in an InsertionResult.

        # PARAMETERS:
            *   item (Team)

        # Returns:
        InsertionResult[TTeam] containing either:
            - On success: Team in the payload.
            - On failure: Exception.

        # Raises:
            *   TeamInsertionFailedException
        """
        method = "TeamDataService.push"
        
        try:
            # Start the error detection process.
            validation = self.service.item_validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            self.items.append(item)
            # After item is pushed onto the stack indicate success by sending it
            # back to the caller.
            return InsertionResult.success(payload=item)
        
        # Finally, if there is an unhandled exception Wrap a TeamInsertionFailedException around it
        # then return exception chain inside an InsertionResult.
        except Exception as ex:
            return InsertionResult.failure(
                TeamInsertionFailedException(
                    ex=ex, message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @LoggingLevelRouter.monitor
    def search(self, context: TeamContext) -> SearchResult[List[Team]]:
        """
        # ACTION:
        1.  Pass context argument to self.search.
        2.  Pass self.items and self.context_service.validator to self.search's renaming params.
        3.  The Search object will return any exceptions if it fails, success otherwise.
        4.  Because Search object does all the error using a try-catch is uneccesar

        2.  If certification fails return the exception inside an InsertionResult.
        3.  Otherwise, push item onto the stack.
        4.  Send the successfully pushed data back in an InsertionResult.

        # PARAMETERS:
            *   item (Team)

        # Returns:
        SearchResult[List[Team]] containing either:
            - On success: List[Team] in the payload.
            - On failure: Exception.

        # Raises:
        None
        """
        method = "TeamDataService.search"
        
        return self.search.find(
            data_set=self.items, context=context, context_validator=self.context_service.item_validator
        )