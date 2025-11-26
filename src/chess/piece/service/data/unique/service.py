# src/chess/piece/service/data/unique/service.py

"""
Module: chess.piece.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService
from chess.piece import Piece, AddingDuplicatePieceException, UniquePieceDataServiceException

class UniquePieceDataService(UniqueDataService[Piece]):
    
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
