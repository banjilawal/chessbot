# src/collection/chain/chain.py

"""
Module: collection.chain.chain
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, TypeVar, cast

from assurance import NumberValidator
from collection import DomainObjectCollection
from domain import Node
from result import BuildResult, DeletionResult, InsertionResult, SearchResult, ValidationResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Node")


class Chain(DomainObjectCollection, ABC, Generic[T]):
    _number_validator: NumberValidator
    _iterator: ChainIterator
    
    _head: T
    _tail: T
    _size: int
    
    def __init__(
            self,
            head: Optional[T] | None = None,
            tail: Optional[T] | None = None,
            number_validator: Optional[NumberValidator] | None = None
    ):
        super().__init__()
        self._number_validator = number_validator or NumberValidator()
        self._head = head
        self._tail = tail
        
        self._head.previous = None
        self._tail.next = None
        
        self._head.next = self._tail
        self._tail.previous = self._head
        self._size = 0
        self._iterator = ChainIterator(self)
        
    @property
    def head(self) -> T:
        return self._head
    
    @property
    def tail(self) -> T:
        return self._tail
    
    @property
    def size(self) -> int:
        return self._size
    
    @size.setter
    def size(self, other: int):
        self._size = self._size + other
    
    @property
    def is_empty(self) -> bool:
        return (
                self._head.next == self._tail and
                self._tail.previous == self._head and
                self._size == 0
        )
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def iterator(self) -> ChainIterator:
        return self._iterator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def add_node(self, node: T) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def remove_node(self, node: T) -> DeletionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def find_node(self, node: Node[T]) -> SearchResult[List[T]]:
        pass
        
    @LoggingLevelRouter.monitor
    def get_at_offset(self, index: int) -> SearchResult[List[T]]:
        method = f"{self.__class__.__name__}.get_by_index"
        
        counter: int = 0
        cursor = self._head
        node: Node[T] = Node[T]()
        
        if self.is_empty:
            return SearchResult.empty()
        
        if index is None or index == 0:
            return SearchResult[[self._head.next]]

        if index == -1 or index == self._size - 1:
            return SearchResult[[self._tail.previous]]
            
        while counter < index and cursor.next is not None:
            cursor = cursor.next
            counter = counter + 1
        return SearchResult.success([cursor])
    
    
    @LoggingLevelRouter.monitor
    def remove_at_offset(self, offset: int) -> DeletionResult[T]:
        method = f"{self.__class__.__name__}.execute"
        
        # Hand off get the node to the finder
        search = self.get_at_offset(offset)
        
        # Handle the case that, the search fails.
        if search.is_failure:
            # Send the exception in the result.
            return DeletionResult.failure(
                ChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChainException.MSG,
                    err_code=ChainException.ERR_CODE,
                    ex=search.exception
                )
            )
        # Handle the case that there is nothing at the index.
        if search.is_empty:
            return DeletionResult.nothing_to_delete()
        
        node = cast(Node[T], search.payload[0])
        node.previous.next = node.next
        node.next.previous  = node.previous
        self._size = self._size - 1
        
        node.previous = None
        node.next = None
        
        return DeletionResult.success(node)
    
    @LoggingLevelRouter.monitor
    def trim_head(self, offset: int) -> BuildResult[Chain[T]]:
        method = f"{self.__class__.__name__}.execute"
        
        validation = self.offset_validator(offset)
        # Handle the case that, the search fails.
        if valdation.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                ChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChainException.MSG,
                    err_code=ChainException.ERR_CODE,
                    ex=validation.exception
                )
            )
        counter = 0
        cursor = self.iterator.next()
        while self.iterator.has_next and counter < offset:
            counter = counter + 1
            cursor = self.iterator.next()
        self._head.next = cursor
        cursor.previous = self._head
        self._size = self._size - offset
        return BuildResult.success(self)
    
    @LoggingLevelRouter.monitor
    def trim_tail(self, offset: int) -> BuildResult[Chain[T]]:
        method = f"{self.__class__.__name__}.execute"
        
        validation = self.offset_validator(offset)
        # Handle the case that, the search fails.
        if validation.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                ChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChainException.MSG,
                    err_code=ChainException.ERR_CODE,
                    ex=validation.exception
                )
            )
        counter = 0
        cursor = self.iterator.next()
        while self.iterator.has_next and counter < offset:
            counter = counter + 1
            cursor = self.iterator.next()
        self._tail.previous = cursor
        cursor.next = self._tail
        self._size = self._size - offset
        return BuildResult.success(self)

    def offset_validator(self, candidate: Any) -> ValidationResult[int]:
        method = f"{self.__class__.__name__}.execute"
        
        if candidate is None:
            return ValidationResult.success(0)
        
        if not isinstance(candidate, int):
            return DeletionResult.failure(
                ChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChainException.MSG,
                    err_code=ChainException.ERR_CODE,
                    ex=search.exception
                )
            )
        offset = cast(int, candidate)
        
        # Handle the case that, the index is out of bounds.
        if abs(offset) >= self.size:
            # Send the exception in the result.
            return ValidationResult.failure(
                ChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChainException.MSG,
                    err_code=ChainException.ERR_CODE,
                    ex=ListIndexOutOfBoundsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ListIndexOutOfBoundsException.MSG,
                        err_code=ListIndexOutOfBoundsException.ERR_CODE,
                    )
                )
            )
        if offset < 0:
            return ValidationResult.success(self.size - (1 + offset))
        
class ChainIterator:
    _cursor: Node
    _linked_list: Chain
    
    def __init__(self, linked_list: Chain):
        self._linked_list = linked_list
        self._cursor = self._linked_list.head
    
    @property
    def has_next(self,) -> bool:
        return self._cursor.next is None
    
    def next(self) -> Node:
        if self.has_next():
            next_node = self._cursor.next
            self._cursor = self._cursor.next
            return self._cursor.next
        else:
            return self._cursor
            
            
            
    
