# src/chess/square/service/data/service.py

"""
Module: chess.square.service.data.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import List

from chess.system import DataService, LoggingLevelRouter, SearchResult, id_emitter
from chess.square import Square, SquareContext, SquareContextService, SquareSearch, SquareService


class SquareDataService(DataService[Square]):
    """"""
    DEFAULT_NAME = "SquareDataService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            items: List[Square] = List[Square],
            search: SquareSearch = SquareSearch(),
            service: SquareService = SquareService(),
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
    def search(self, context: SquareContext) -> SearchResult[List[Square]]:
        """"""
        method = "SquareDataService.search"
        return self._search.find(
            data_set=self.items,
            context=context,
            context_validator=self.context_service.validator
        )