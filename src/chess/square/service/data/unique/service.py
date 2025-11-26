# src/chess/square/service/data/service.py

"""
Module: chess.square.service.data.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import List

from chess.square.service.data.unique.exception import UniqueSquareDataServiceException
from chess.system import InsertionResult, LoggingLevelRouter, UniqueDataService, ValidationResult, id_emitter
from chess.square import AddingDuplicateSquareException, Square, SquareDataService, SquareDataServiceException



class UniqueSquareDataService(UniqueDataService[Square]):
    """"""
    
    DEFAULT_NAME = "UniqueSquareDataService"
    _id: int
    _data_service: SquareDataService
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            data_service: SquareDataService = SquareDataService(),
    ):
        super().__init__(id=id, name=name, data_service=data_service)
    
    @LoggingLevelRouter.monitor
    def push_unique(self, item: Square) -> InsertionResult[Square]:
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
        
        
    

        
