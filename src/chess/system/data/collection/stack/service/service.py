# src/chess/system/data/collection/stack/service/service.py

"""
Module: chess.system.data.collection.stack.service.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import Generic, List, Optional, TypeVar

from chess.system import (
    Context, ContextService, DataServiceException, InsertionResult, LoggingLevelRouter, PoppingEmptyStackException,
    SearchResult, EntityService, DeletionResult
)


D = TypeVar("D")
C = TypeVar("C", bound=Context)

class DataService(ABC, Generic[D]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Scales Builder and Validator operations for collection of objects.
    2.  Provides map aware search.
    3.  Safe and reliable CRUD operations.
    4.  Public facing API.
    
    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int):
        *   name (str):
        *   items (List[D]):
        *   searcher (Searcher[D]):
        *   entity_service (EntityService[D]):
        *   context_service (ContextService);
        *   current_item (D):
        *   size (int)
    
    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _name: str
    _items: List[D]
    _entity_service: EntityService[D]
    _context_service: ContextService[C]

    def __init__(
            self,
            id: int,
            name: str,
            items: List[D],
            entity_service: EntityService[D],
            context_service: ContextService[C],
    ):
        self._id = id
        self._name = name
        self._items = items
        self._entity_service = entity_service
        self._context_service = context_service
        #
        # self._size = len(self._items)
        # self._current_item = self._items[-1] if self._items else None
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def size(self) -> int:
        return len(self._items)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def items(self) -> List[D]:
        return self._items
    
    @property
    def entity_service(self) -> EntityService[D]:
        return self._entity_service
    
    @property
    def context_service(self) -> ContextService[C]:
        return self._context_service
    
    @property
    def current_item(self) -> Optional[D]:
        return self._items[-1] if self._items else None
    
    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    @LoggingLevelRouter.monitor
    def push_item(self, item: D) -> InsertionResult[D]:
        """"""
        method = "DataService.push"
        try:
            validation = self._entity_service.entity_validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            self.items.append(item)
            return InsertionResult.success(payload=item)
        except Exception as ex:
            return InsertionResult.failure(
                DataServiceException(ex=ex, message=f"{method}: {DataServiceException.DEFAULT_MESSAGE}")
            )
    
    @LoggingLevelRouter.monitor
    def search(self, context: C) -> SearchResult[List[D]]:
        """"""
        method = "DataService.search"
        return self._context_service.entity_finder.find(
            dataset=self.items,
            context=context,
            context_validator=self._context_service.entity_validator,
        )
        # try:
        #     validation = self._context_service.entity_validator.validate(map)
        #     if validation.is_failure():
        #         return SearchResult.failure(validation.exception)
        #     return SearchResult.success(payload=validation.payload)
        # except Exception as ex:
        #     return SearchResult.failure(
        #         DataServiceException(ex=ex, message=f"{method}: {DataServiceException.DEFAULT_MESSAGE}")
        #     )
    
    @LoggingLevelRouter.monitor
    def undo_item_push(self) -> DeletionResult[D]:
        method = "DataService.undo_item_push"
        try:
            if self._items == 0:
                return DeletionResult.failure(
                    PoppingEmptyStackException(f"{method}: {PoppingEmptyStackException.DEFAULT_MESSAGE}")
                )
            item = self._items.pop()
            return DeletionResult.success(payload=item)
        except Exception as ex:
            return DeletionResult.failure(
                DataServiceException(ex=ex, message=f"{method}: {DataServiceException.DEFAULT_MESSAGE}")
            )
    
