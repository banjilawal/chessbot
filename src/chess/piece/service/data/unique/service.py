# src/chess/piece/service/data/unique/service.py

"""
Module: chess.piece.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService, id_emitter
from chess.piece import Piece, AddingDuplicatePieceException, PieceDataService, UniquePieceDataServiceException


class UniquePieceDataService(UniqueDataService[Piece]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Wraps PieceDataService.
    3.  Guarantees each item on the stack is unique.

    # PROVIDES:
        *   PieceDataService

    # ATTRIBUTES:
        *   id (int):
        *   name (str):
        *   data_service (PieceDataService):
        
    # CONSTRUCTOR:
        *   __init__(id: int, name: str, data_service: TeamDataService)
    
    # CLASS METHODS:
    None
    
    # INSTANCE METHODS:
        *   push_unique(item: Team) -> InsertionResult[Team]
    """
    DEFAULT_NAME = "UniquePieceDataService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            data_service: PieceDataService = PieceDataService(),
    ):
        """
        # Action
        1.  Use id_emitter to automatically generate a unique id for each UniquePieceDataService instance.
        2.  Automatic dependency injection by providing working default instances name and PieceDataService instance.
        """
        super().__init__(id=id, name=name, data_service=data_service)
    
    @LoggingLevelRouter.monitor
    def push_unique(self, item: Piece) -> InsertionResult[Piece]:
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
            *   TeamDataServiceException
        """
        method = "UniquePieceDataService.push_unique"
        
        try:
            # Start the error detection process.
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
                    AddingDuplicatePieceException(f"{method}: {AddingDuplicatePieceException.DEFAULT_MESSAGE}")
                )
            # After the error chain is passed self._data_service returns the outcome of
            # pushing the item on to the stack.
            return self._data_service.push(item)
        
        # Finally return an InsertionResult containing any unhandled exceptions insided an
        # UniquePieceDataServiceException
        except Exception as ex:
            return InsertionResult.failure(
                UniquePieceDataServiceException(
                    ex=ex, message=f"{method}: {UniquePieceDataServiceException.DEFAULT_MESSAGE}"
                )
            )
