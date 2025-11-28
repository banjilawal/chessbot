# src/chess/team/service/data/unique/service.py

"""
Module: chess.team.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import AddingDuplicateTeamException, Team, TeamDataService, UniqueTeamDataServiceException
from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService, id_emitter


class UniqueTeamDataService(UniqueDataService[Team]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Wraps TeamDataService.
    3.  Guarantees each item on the stack is unique.

    # PROVIDES:
        *   TeamDataService

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   data_service (TeamDataService):
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
        method = "UniqueTeamDataService.push_unique"
        
        try:
            validation = self.service.validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            
            context_validation = self._data_service.context_service.builder.build(id=item.id)
            if context_validation.is_failure():
                return InsertionResult.failure(context_validation.exception)
            
            search_result = self._data_service.search(context=context_validation.payload)
            if search_result.is_failure():
                return InsertionResult.failure(search_result.exception)
            
            if search_result.is_success():
                return InsertionResult.failure(
                    AddingDuplicateTeamException(f"{method}: {AddingDuplicateTeamException.DEFAULT_MESSAGE}")
                )
            
            return self._data_service.push(item)
        
        except Exception as ex:
            return InsertionResult.failure(
                UniqueTeamDataServiceException(
                    ex=ex, message=f"{method}: {UniqueTeamDataServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    