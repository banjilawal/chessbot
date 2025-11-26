# src/chess/piece/service/data/service_.py

"""
Module: chess.piece.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
from chess.piece import Piece, PieceContext, PieceDataServiceException, PieceSearch, PieceService, PieceContextService


class PieceDataService(DataService[Piece]):
    """"""
    DEFAULT_NAME = "PieceDataService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            items: List[Piece] = List[Piece],
            search: PieceSearch = PieceSearch(),
            service: PieceService = PieceService(),
            context_service: PieceContextService = PieceContextService(),
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
    def push(self, item: Piece) -> InsertionResult[Piece]:
        method = "PieceDataService.push"
        try:
            validation = self.service.validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            self.items.append(item)
            
            return InsertionResult.success(payload=item)
        except Exception as ex:
            return InsertionResult.failure(
                PieceDataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceDataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )


    @LoggingLevelRouter.monitor
    def search(self, context: PieceContext) -> SearchResult[List[Piece]]:
        method = "PieceDataService.search"
        return self.search.find(
            data_set=self.items,
            context=context,
            context_validator=self.context_service.validator
        )
