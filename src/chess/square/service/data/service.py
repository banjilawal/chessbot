# src/chess/square/service/data/service.py

"""
Module: chess.square.service.data.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import List

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
from chess.square import (
    Square, SquareContext, SquareContextService, SquareDataServiceException, SquareSearch,
    SquareCertifier
)


class SquareDataService(DataService[Square]):
    """"""
    DEFAULT_NAME = "SquareDataService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            items: List[Square] = List[Square],
            search: SquareSearch = SquareSearch(),
            service: SquareCertifier = SquareCertifier(),
            context_service: SquareContextService =  SquareContextService(),
    ):
        super().__init__(
            id=id,
            name=name,
            items=items,
            search=search,
            service=service,
            context_service=context_service,
        )
    
    @LoggingLevelRouter.monitor
    def push(self, item: Square) -> InsertionResult[Square]:
        method = "SquareDataService.push"
        try:
            validation = self.security_service.validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            self.items.append(item)
            
            return InsertionResult.success(payload=item)
        except Exception as ex:
            return InsertionResult.failure(
                SquareDataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{SquareDataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
 
        
    @LoggingLevelRouter.monitor
    def search(self, context: SquareContext) -> SearchResult[List[Square]]:
        """"""
        method = "SquareDataService.search"
        return self._search.find(
            data_set=self.items,
            context=context,
            context_validator=self.context_service.validator
        )