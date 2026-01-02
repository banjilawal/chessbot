# src/chess/token/service/data/unique/service.py

"""
Module: chess.token.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService, id_emitter
from chess.token import Token, TokenDataService


class UniqueTokenDataService(UniqueDataService[Token]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Wraps TokenDataService.
    3.  Guarantees each item on the stack is unique.

    # PROVIDES:
        *   TokenDataService

    # ATTRIBUTES:
        *   id (int):
        *   name (str):
        *   data_service (TokenDataService):
        
    # CONSTRUCTOR:
        *   __init__(id: int, designation: str, data_service: TeamDataService)
    
    # CLASS METHODS:
    None
    
    # INSTANCE METHODS:
        *   push_unique(item: Team) -> InsertionResult[Team]
    """
    DEFAULT_NAME = "UniqueTokenDataService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            data_service: TokenDataService = TokenDataService(),
    ):
        """
        # Action
        1.  Use id_emitter to automatically generate a unique id for each UniqueTokenDataService instance.
        2.  Automatic dependency injection by providing working default instances designation and TokenDataService instance.
        """
        super().__init__(id=id, name=name, data_service=data_service)
    
    @LoggingLevelRouter.monitor
    def push_unique_item(self, item: Token) -> InsertionResult[Token]:
        """
        # ACTION:
        1.  Use TeamDataService.service.validator to certify item.
        2.  If certification fails return the exception inside an InsertionResult.
        3.  Otherwise, push item onto the stack.
        4.  Send the successfully pushed data back in an InsertionResult.

        # PARAMETERS:
            *   item (Team)

        # RETURNS:
        InsertionResult[TTeam] containing either:
            - On success: Team in the payload.
            - On failure: Exception.

        # RAISES:
            *   TeamDataServiceException
        """
        method = "UniqueTokenDataService.push_unique"
        
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
                    AddingDuplicateTokenException(f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}")
                )
            # After the error chain is passed self._data_service returns the outcome of
            # pushing the item on to the stack.
            return self._data_service.push_item(item)
        
        # Finally return an InsertionResult containing any unhandled exception insided an
        # UniqueTokenDataServiceException
        except Exception as ex:
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    ex=ex, message=f"{method}: {UniqueTokenDataServiceException.DEFAULT_MESSAGE}"
                )
            )
