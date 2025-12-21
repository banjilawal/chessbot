# src/chess/system/result/stack/stack.py

"""
Module: chess.system.result.stack.stack
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC
from typing import Generic, List, Optional, TypeVar

from chess.system import (
    Context, DeletionResult, InsertionResult, LoggingLevelRouter, PoppingEmptyStackException,
    Result, SearchResult
)

T = TypeVar("T", bound=Result)



class ResultStack(ABC, Generic[T]):
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
        *   errors():   --> List[Result[Exception]]
        *   payloads():     --> List[Result[T]]
        *   last_result():  --> Optional[Result[T]]
        *   undo_result_push(): --> DeletionResult[T]
        *   push_result(result: Result[T]): --> InsertionResult[T]

    # LOCAL ATTRIBUTES:
        *   size (int)
        *   is_empty (bool)
        *   items (List[T])
        *   current_result (T)

    # INHERITED ATTRIBUTES:
    None
    """
    _items: List[T]
    
    def __init__(
            self,
            items: List[T] = [],
    ):
        self._items = items

    @property
    def size(self) -> int:
        return len(self._items)
    
    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0

    @property
    def items(self) -> List[T]:
        return self._items
    
    @property
    def last_result(self) -> Optional[T]:
        return self._items[-1] if self._items else None
    
    
    @LoggingLevelRouter.monitor
    def push_result(self, result: Result[T]) -> InsertionResult[T]:
        """"""
        method = "ResultStack.push_result"
        try:
            if result is None:
                return InsertionResult.failure(
                    NullResultException(f"{method}: {NullResultException.DEFAULT_MESSAGE}")
                )
            if not isinstance(result, Result[T]):
                return InsertionResult.failure(
                    TypeError(f"{method}: Expected Result, got {type(result).__name__} instead.")
                )
            if result in self.items:
                return InsertionResult.failure(
                    AddingResultDataSetException(f"{method}: {AddingDuplicateResultException.DEFAULT_MESSAGE}")
                )
            self.items.append(result)
            return InsertionResult.success(payload=result)
        except Exception as ex:
            return InsertionResult.failure(
                ResultStackException(ex=ex, message=f"{method}: {ResultStackException.DEFAULT_MESSAGE}")
            )
    
    @LoggingLevelRouter.monitor
    def undo_result_push(self) -> DeletionResult[T]:
        method = "ResultStack.undo_result_push"
        try:
            if self._items == 0:
                return DeletionResult.failure(
                    PoppingEmptyStackException(f"{method}: {PoppingEmptyStackException.DEFAULT_MESSAGE}")
                )
            item = self._items.pop()
            return DeletionResult.success(payload=item)
        except Exception as ex:
            return DeletionResult.failure(
                ResultStackException(ex=ex, message=f"{method}: {ResultStackException.DEFAULT_MESSAGE}")
            )
        
        
    @LoggingLevelRouter.monitor
    def errors(self) -> List[Exception]:
        return [result for result in self.items if result.exception is not None]
    
    @LoggingLevelRouter.monitor
    def payloads(self) -> List[T]:
        return [result for result in self.items if result.payload is not None]