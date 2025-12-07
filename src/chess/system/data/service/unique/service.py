# src/chess/system/data/service/stack/service.py

"""
Module: chess.system.data.entity_service.unique.entity_service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, EntityService, Context

T = TypeVar("T")

class UniqueDataService(ABC, Generic[T]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Assures DataService only stores unique data with no duplicates.
    2.  Interface for inserting data into the DataService.
    3.  Protects data from direct access.
    4.  Wrapper for DataService
    5.  Public facing API.

    # PROVIDES:
        *   EntityService
        *   DataService

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   data_service (DataService[D]):
    """
    _id: int
    _name: str
    _data_service: DataService[T]
    
    def __init__(self, id: int, name: str, data_service: DataService[T]):
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
    def current_item(self) -> Optional[T]:
        return self._data_service.current_item
    
    @property
    def is_empty(self) -> bool:
        return self._data_service.is_empty
    
    @property
    def service(self) -> EntityService[T]:
        """"""
        return self._data_service.entity_service
    
    @property
    def data_service(self) -> DataService[T]:
        return self._data_service
        
    
    @LoggingLevelRouter.monitor
    def search(self, context: Context) -> SearchResult[List[T]]:
        return self._data_service.search(context)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push_unique(self, item: T) -> InsertionResult[T]:
        """"""
        pass
        