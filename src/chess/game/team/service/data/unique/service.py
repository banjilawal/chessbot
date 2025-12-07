# src/chess/team/entity_service/data/unique/entity_service.py

"""
Module: chess.team.entity_service.data.unique.entity_service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import (
    AddingDuplicateTeamException, Team, TeamDataService, TeamInsertionFailedException,
    UniqueTeamDataServiceException
)
from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService, id_emitter


class UniqueTeamDataService(UniqueDataService[Team]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Wraps TeamDataService.
    3.  Guarantees each item on the stack is unique.

    # PROVIDES:
        *   TeamDataService

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   data_service (TeamDataService)
        
    # CONSTRUCTOR:
        *   __init__(id: int, name: str, data_service: TeamDataService)
    
    # CLASS METHODS:
    None
    
    # INSTANCE METHODS:
        *   push_unique(item: Team) -> InsertionResult[Team]
    """
    DEFAULT_NAME = "UniqueTeamDataService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id, 
            data_service: TeamDataService = TeamDataService(),
    ):
        """
        # Action
        1.  Use id_emitter to automatically generate a unique id for each UniqueTeamDataService instance.
        2.  Automatic dependency injection by providing working default instances name and TeamDataService instance.
        """
        super().__init__(id=id, name=name,data_service=data_service )
    
    @LoggingLevelRouter.monitor
    def push_unique(self, item: Team) -> InsertionResult[Team]:
        """
        # ACTION:
        1.  Use self.entity_service.validator to verify the item is safe.
        2.  There is no direct access to the internal list so use self.data_service.searcher to find item.
        3.  If item already exists return an exception in an InsertionResult.
        4.  Otherwise, push the item onto the stack and send the item.
        5.  After the push send the item back to the caller indicating success.

        # PARAMETERS:
            *   item (Team)

        # Returns:
        InsertionResult[Team] containing either:
            - On success: Team in the payload.
            - On failure: Exception.

        # Raises:
            *   AddingDuplicateTeamException
            *   UniqueTeamDataServiceException
        """
        method = "UniqueTeamDataService.push_unique"
        
        try:
            # Start the error detection process.
            validation = self.data.item_validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            
            context_validation = self._data_service.context_service.item_builder.build(id=item.id)
            if context_validation.is_failure():
                return InsertionResult.failure(context_validation.exception)
            
            search_result = self._data_service.search(context=context_validation.payload)
            if search_result.is_failure():
                return InsertionResult.failure(search_result.exception)
            
            if search_result.is_success():
                return InsertionResult.failure(
                    AddingDuplicateTeamException(f"{method}: {AddingDuplicateTeamException.DEFAULT_MESSAGE}")
                )
            # After the error has been passed self._data_service returns the outcome of
            # pushing the item on to the stack.
            return self._data_service.push_item(item)
        
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return InsertionResult.failure(
                TeamInsertionFailedException(
                    ex=ex, message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    