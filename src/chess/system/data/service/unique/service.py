# src/chess/system/data/service/stack/service.py

"""
Module: chess.system.data.service.unique.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from chess.system.data import DataService, InsertionResult
from chess.system import Context, LoggingLevelRouter, SearchResult, Service, UniqueDataServiceException

A = TypeVar("A")
C = TypeVar("C", binding=Context)

class UniqueDataService(ABC, Generic[A]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Assures DataService only stores unique data with no duplicates.
    2.  Interface for inserting data into the DataService.
    3.  Protects data from direct access.
    4.  Wrapper for DataService
    5.  Public facing API.

    # PROVIDES:
        *   DataService

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   data_service (DataService[D]):
    """
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
    def service(self) -> Service[A]:
        return self._data_service.service
    
    @property
    def context_service(self) -> Service[C]:
        return self._data_service.context_service
    
    def search(self, context: C) -> SearchResult[List[A]]:
        return self._data_service.search(context=context)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: A) -> InsertionResult[A]:
        pass