# src/chess/system/data/service/stack/unique/service.py

"""
Module: chess.system.data.service.stack.unique.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""
from abc import abstractmethod
from typing import TypeVar

from chess.system import DataResult, DataService, LoggingLevelRouter, StackService, UniqueStackServiceException

T = TypeVar("T")


class UniqueStackService(StackService[T]):
    
    def __init__(id: int, name: str, data_service: DataService[T]):
        super().__init__(id=id, name=name, data_service=data_service)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: T) -> DataResult[T]:
        pass
        # method = "UniqueDataStackService."
        # try:
        #     search_result = self.search()
        # except Exception as ex:
        #     return DataResult.failure(
        #         UniqueStackServiceException(
        #             ex=ex,
        #             message=(
        #                 f"{method}: "
        #                 f"{UniqueStackServiceException.DEFAULT_MESSAGE}"
        #             )
        #         )
        #     )