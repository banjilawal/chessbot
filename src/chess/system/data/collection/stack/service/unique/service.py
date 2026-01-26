# src/chess/system/data/collection/stack/service/unique/service.py

"""
Module: chess.system.data.collection.stack.service.unique.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import Generic, Optional, TypeVar

from chess.system import (
    AddingDuplicateDataException, DataService, InsertionResult, LoggingLevelRouter, UniqueDataServiceException
)

T = TypeVar("T")

class DatabaseService(ABC, Generic[T]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Assures DataService only stores unique data with no duplicates.
    2.  Interface for inserting data into the DataService.
    3.  Protects data from direct access.
    4.  Wrapper for DataService
    5.  Public facing API.
    
    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   member_service (DataService[D]):
        
    # INHERITED ATTRIBUTES:
    None
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
    def data_service(self) -> DataService[T]:
        return self._data_service
    
    @LoggingLevelRouter.monitor
    def push_unique_item(self, item: T) -> InsertionResult[T]:
        method = "UniqueAgentDataService.push_unique"
        try:
            validation = self.data_service.entity_service.entity_validator.validate(item)
            if validation.is_failure:
                return InsertionResult.failure(validation.exception)

            context_build = self._data_service.context_service.entity_builder.build(id=item.id)
            if context_build.is_failure:
                return InsertionResult.failure(context_build.exception)

            query_result = self._data_service.search(context=context_build.payload)
            if query_result.is_failure:
                return InsertionResult.failure(query_result.exception)

            if query_result.is_success:
                return InsertionResult.failure(
                    AddingDuplicateDataException(f"{method}: {AddingDuplicateDataException.DEFAULT_MESSAGE}")
                )
            return self._data_service.push_item(item)

        except Exception as ex:
            return InsertionResult.failure(
                UniqueDataServiceException(ex=ex, message=f"{method}: {UniqueDataServiceException.DEFAULT_MESSAGE}")
            )
        