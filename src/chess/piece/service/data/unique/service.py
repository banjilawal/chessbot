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
    None
        *   id (int):
        *   name (str):
        *   data_service (PieceDataService):
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
        method = "UniquePieceDataService.push_unique"
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
                    AddingDuplicatePieceException(
                        f"{method}: {AddingDuplicatePieceException.DEFAULT_MESSAGE}"
                    )
                )
            return self._data_service.push(item)
        except Exception as ex:
            return InsertionResult.failure(
                UniquePieceDataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{UniquePieceDataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
