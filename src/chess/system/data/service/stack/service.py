# src/chess/system/data/service/stack/service.py

"""
Module: chess.system.data.service.stack.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import Generic, List, Optional, TypeVar

from chess.system import (
    Context, DataResult, DataService, StackServiceException, LoggingLevelRouter, RemovingNullException,
    SearchResult, Service
)

A = TypeVar("A")
C = TypeVar("C", binding=Context)

class StackService(ABC, Generic[A]):
    """"""
    _id: int
    _name: str
    _data_service: DataService[A]
    
    def __init__(self, id: int, name: str, data_service: DataService[A]):
        self._id = id
        self._name =  name
        self._data_service = data_service
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def size(self) -> int:
        return self._data_service.size
    
    @property
    def current_item(self) -> Optional[A]:
        return self._data_service.current_item
    
    @property
    def service(self) -> Service[C]:
        return self._data_service.service
    
    @property
    def context_service(self) -> Service[C]:
        return self._data_service.context_service
    
    @property
    def search(self, context: C) -> SearchResult[List[A]]:
        return self._data_service.query(context=context)
    
    @LoggingLevelRouter.monitor
    def push(self, item: A):
        self._data_service.items.append(item)
        
    @LoggingLevelRouter.monitor
    def pop(self) -> DataResult[A]:
        method = "StackService.pop"
        try:
            if self._data_service.is_empty():
                return DataResult.failure(
                    RemovingNullException(
                        f"{method}: "
                        f"{RemovingNullException.DEFAULT_MESSAGE}"
                    )
                )
        except Exception as ex:
            DataResult.failure(
                StackServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{StackServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
    