# src/chess/square/service/data/service.py

"""
Module: chess.square.service.data.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import List, cast


from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService, id_emitter
from chess.square import (
    AddingDuplicateSquareException, Square, SquareDataService, SquareService, UniqueSquareDataServiceException
)


class UniqueSquareDataService(UniqueDataService[Square]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all items in managed by TokenDataService are unique.
    2.  Guarantee consistency of records in TokenDataService.

    # PARENT:
        *   UniqueDataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UniqueDataService class for inherited attributes.
    """
    SQUARE_NAME = "UniqueSquareDataService"
    _id: int
    data_service: SquareDataService
    
    def __init__(
            self,
            name: str = SQUARE_NAME,
            id: int = id_emitter.service_id,
            data_service: SquareDataService = SquareDataService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   data_service (TokenDataService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        
    @property
    def integrity_service(self) -> SquareService:
        return cast(SquareDataService, self.data_service).square_service
    
    @LoggingLevelRouter.monitor
    def push_unique_item(self, item: Square) -> InsertionResult[Square]:
        method = "UniqueSquareDataService.push"
        try:
            validation = self._data_service.validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            
            if item in self._data_service.items:
                return InsertionResult.failure(
                    AddingDuplicateSquareException(
                        f"{method}: "
                        f"{AddingDuplicateSquareException.DEFAULT_MESSAGE}"
                    )
                )
            self._data_service.items.append(item)
            return InsertionResult.success(item)
        except Exception as ex:
            return InsertionResult.failure(
                UniqueSquareDataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{UniqueSquareDataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        
    

        
